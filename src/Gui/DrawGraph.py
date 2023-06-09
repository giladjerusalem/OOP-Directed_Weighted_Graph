
import os
import random
from tkinter import messagebox, Tk
from tkinter.filedialog import askopenfilename

import pygame

from src.GraphAlgo import GraphAlgo
from src.Gui.Button import Button
from src.Gui.InputBox import InputBox
from src.Gui.Range import Range
from src.Gui.Range2D import Range2D
from src.Gui.Range2Range import Range2Range
from src.NodeData import NodeData

NO_PATH_ERROR = 'There is no path between this nodes'
BUTTON_COLOR = (0, 255, 0)
WIDTH, HEIGHT = 1000, 700
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
FPS = 60


def init(g: GraphAlgo):
    gui = GraphDraw(g)
    gui.run_gui()


def path_builder(node_lst: list) -> str:
    ans = 'Path: '
    for node in node_lst[:-1]:
        ans += str(node) + '->'
    ans += str(node_lst[len(node_lst) - 1]) + '\n'
    return ans


def text_boxes(screen, text: str, font_size, pos, color=None, width=None, height=None):
    text_rect = None
    font = pygame.font.Font(None, font_size)
    if color is None:
        text_out = font.render(text, True, (0, 0, 0), (255, 255, 255))  # font used
    else:
        text_out = font.render(text, True, (0, 0, 0), color)  # font used
    if width is None and height is None:
        text_rect = text_out.get_rect()  # creating frame box for the text
        text_rect.bottomleft = pos  # bottom left corner of the text box

    screen.blit(text_out, text_rect)  # print to screen


def is_valid_input(final):
    try:
        counter = 0
        for c in final:
            if counter % 2 == 0:
                val = int(c)
            else:
                val = str(c)
            counter += 1
        return True
    except ValueError:
        return False


class GraphDraw:

    def __init__(self, g: GraphAlgo):
        self.g = g
        self.range: Range2Range

    def run_gui(self):
        pygame.init()
        icon_image = pygame.image.load(os.path.join('resources/05-nodes_network.png'))
        back_ground_image = pygame.image.load(os.path.join('resources/nowayhome.jpg'))
        connected_button = Button(BUTTON_COLOR, 800, 50, 200, 25, 'Is Connected?')
        shortest_path_button = Button(BUTTON_COLOR, 800, 80, 200, 25, 'Shortest Path')
        center_button = Button(BUTTON_COLOR, 800, 110, 200, 25, 'Graph Center')
        tsp_button = Button(BUTTON_COLOR, 800, 140, 200, 25, 'TSP')
        load_button = Button(BUTTON_COLOR, 800, 170, 200, 25, 'Load Graph')

        input_box_tsp = InputBox(800, 470, 100, 32)
        input_box_shortest = InputBox(800, 540, 100, 32)
        clock = pygame.time.Clock()

        shortest_path_bool = False
        tsp_bool = False

        messagebox_bool1 = True
        messagebox_bool2 = True

        pygame.display.set_icon(icon_image)
        pygame.display.set_caption('Graph')

        window = pygame.display.set_mode((WIDTH, HEIGHT))
        back_ground_image = pygame.transform.scale(back_ground_image, (WIDTH, HEIGHT))
        window.blit(back_ground_image, (0, 0))

        run = True
        while run:
            for event in pygame.event.get():
                text_boxes(window, 'Algorithms', 40, (800, 40), (128, 0, 128))
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    run = False

                elif shortest_path_button.is_over(pos, event):
                    shortest_path_bool = True
                    input_box_shortest.draw(window)
                    pygame.display.update()
                elif tsp_button.is_over(pos, event):
                    tsp_bool = True
                    input_box_tsp.draw(window)
                    pygame.display.update()
                elif load_button.is_over(pos, event):
                    try:
                        tk_root = Tk()
                        tk_root.withdraw()
                        string = askopenfilename(filetypes=[("json", "*.json")])
                        if string != '':
                            self.g.load_from_json(string)
                            self.draw_graph(window, WIDTH, HEIGHT, back_ground_image)
                    except IOError as ios:
                        print('File dont exist or the file is not type of json')
                elif connected_button.is_over(pos, event):
                    if self.g.connected():
                        Tk().wm_withdraw()
                        messagebox.showinfo('Connected', 'The graph is connected')
                    else:
                        Tk().wm_withdraw()
                        messagebox.showinfo('Connected', 'The graph is not connected')
                    pygame.display.update()
                elif center_button.is_over(pos, event):
                    if self.g.centerPoint()[0] == -1:
                        Tk().wm_withdraw()
                        messagebox.showinfo('Center Point',
                                            'There is no center point')
                    else:
                        str_input = 'Center node: ' + str(self.g.centerPoint()[0]) + '' \
                                                                                     '\n Radius: ' + str(
                            self.g.centerPoint()[1])
                        Tk().wm_withdraw()
                        messagebox.showinfo('Center Point',
                                            str_input)
                    pygame.display.update()
                input_box_shortest.handle_event(event)
                input_box_tsp.handle_event(event)

            window.fill(COLOR_WHITE, input_box_shortest)
            window.fill(COLOR_WHITE, input_box_tsp)
            input_box_shortest.update()
            input_box_tsp.update()

            if tsp_bool:
                shortest_path_bool = False
                if messagebox_bool1:
                    messagebox_bool1 = False
                    Tk().wm_withdraw()
                    messagebox.showinfo('TSP',
                                        'Enter node ids and backspace in the input box between them '
                                        'for example: 3 5 10')

                text_boxes(window, "TSP Input box:", 15, (800, 465))
                input_box_tsp.draw(window)

            if shortest_path_bool:
                tsp_bool = False
                if messagebox_bool2:
                    messagebox_bool2 = False
                    Tk().wm_withdraw()
                    messagebox.showinfo('Shortest Path',
                                        'Enter source and dest in the input box with backspace between them '
                                        'for example: 3 5')

                text_boxes(window, "Shortest Input box:", 15, (800, 530))
                input_box_shortest.draw(window)

            if input_box_shortest.final != '':
                str_arr = str.split(input_box_shortest.final, ' ')
                if is_valid_input(str_arr) and 1 < len(str_arr) < 3:
                    src, dest = int(str_arr[0]), int(str_arr[1])
                    if self.g.shortest_path(src, dest)[0] != float('inf'):
                        path = path_builder(self.g.shortest_path(src, dest)[1])
                        Tk().wm_withdraw()
                        messagebox.showinfo('Shortest Path',
                                            path + 'Distance: ' + str(self.g.shortest_path(src, dest)[0]))
                    else:
                        Tk().wm_withdraw()
                        messagebox.showinfo('Shortest Path', NO_PATH_ERROR)
                    shortest_path_bool = False
                    messagebox_bool2 = True
                self.draw_graph(window, WIDTH, HEIGHT, back_ground_image)
                # window.fill(COLOR_WHITE, (800, 515, 110, 20))

            if input_box_tsp.final != '':
                str_arr = str.split(input_box_tsp.final, ' ')
                print(str_arr)
                int_arr = []
                if is_valid_input(str_arr):
                    for i in str_arr:
                        int_arr.append(int(i))

                    if self.g.TSP(int_arr)[1] != -1:
                        path = path_builder(self.g.TSP(int_arr)[0])
                        Tk().wm_withdraw()
                        messagebox.showinfo('TSP', path + 'Distance: ' + str(self.g.TSP(int_arr)[0]))
                    else:
                        Tk().wm_withdraw()
                        messagebox.showinfo('TSP', NO_PATH_ERROR)
                    tsp_bool = False
                    messagebox_bool1 = True
                self.draw_graph(window, WIDTH, HEIGHT, back_ground_image)
                # window.fill(COLOR_WHITE, (800, 445, 100, 18))

            self.draw_graph(window, WIDTH, HEIGHT)
            input_box_shortest.clear_final_string()
            input_box_tsp.clear_final_string()
            load_button.draw(window)
            connected_button.draw(window)
            shortest_path_button.draw(window)
            center_button.draw(window)
            tsp_button.draw(window)
            pygame.display.flip()
            clock.tick(FPS)
        del window
        pygame.quit()

    def draw_graph(self, window, width, height, back_ground_image=None) -> None:
        self.resize(width, height)
        if back_ground_image is not None:
            window.blit(back_ground_image, (0, 0))
        for node in self.g.get_graph().get_all_v():
            for edge in self.g.get_graph().all_out_edges_of_node(node):
                self.draw_edge(window, self.g.get_graph().get_node(node), self.g.get_graph().get_node(edge))
        for node in self.g.get_graph().get_all_v().values():
            self.draw_node(window, node)

    def resize(self, width, height):
        rx = Range(90, width - 300)
        ry = Range(height - 50, 80)
        frame = Range2D(rx, ry)
        self.range = Range2Range(self.graph_range(), frame)

    def graph_range(self) -> Range2D:
        x0, x1, y0, y1 = 0, 0, 0, 0
        if self.g.get_graph().get_with_pos():
            first = True
            for node in self.g.get_graph().get_all_v().values():
                pos = node.get_pos()
                if first:
                    x0 = pos[0]
                    x1 = x0
                    y0 = pos[1]
                    y1 = y0
                    first = False
                else:
                    if pos[0] < x0:
                        x0 = pos[0]
                    if pos[0] > x1:
                        x1 = pos[0]
                    if pos[1] < y0:
                        y0 = pos[1]
                    if pos[1] > y1:
                        y1 = pos[1]
        else:
            x0, x1, y0, y1 = 31, 32, 35, 36
        xr = Range(x0, x1)
        yr = Range(y0, y1)
        return Range2D(xr, yr)

    def draw_edge(self, window, src: NodeData, dest: NodeData):
        if not self.g.get_graph().get_with_pos():
            max_range_x, max_range_y = self.range.get_world().get_x_range().get_max(), self.range.get_world().get_y_range().get_max()
            min_range_x, min_range_y = self.range.get_world().get_x_range().get_min(), self.range.get_world().get_y_range().get_min()
            src_random_pos = (random.uniform(min_range_x, max_range_x), random.uniform(min_range_y, max_range_y), 0)
            dest_random_pos = (random.uniform(min_range_x, max_range_x), random.uniform(min_range_y, max_range_y), 0)
            if src.get_pos() is None:
                src.set_pos(src_random_pos[0], src_random_pos[1], src_random_pos[2])
            if dest.get_pos() is None:
                dest.set_pos(dest_random_pos[0], dest_random_pos[1], dest_random_pos[2])
        src_pos, dest_pos = src.get_pos(), dest.get_pos()
        src_pos_loc, dest_pos_loc = self.range.world2frame(src_pos), self.range.world2frame(dest_pos)

        x1, x2, y1, y2 = int(src_pos_loc[0]), int(dest_pos_loc[0]), int(src_pos_loc[1]), int(dest_pos_loc[1])
        start, end = (x1, y1), (x2, y2)

        pygame.draw.line(window, (155, 0, 155), start, end, 3)

    def draw_node(self, window, node: NodeData):
        pos = node.get_pos()
        frame_pos = self.range.world2frame(pos)
        font = pygame.font.SysFont('MV Boli', 30)
        node_image = pygame.image.load(os.path.join('resources/new.png'))
        label = font.render(str(node.get_key()), True, (0, 255, 0))
        if node.get_info() == 'Paint':
            pygame.draw.circle(window, COLOR_RED, (int(frame_pos[0] + 5), int(frame_pos[1]) + 2), 20, 3)
        window.blit(label, (int(frame_pos[0] ), int(frame_pos[1]) - 55))
        window.blit(node_image, (int(frame_pos[0] - 10), int(frame_pos[1]) - 15))

