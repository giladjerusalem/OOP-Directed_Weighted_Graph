import pygame as pg


class Button:
    """Taken from - https://www.youtube.com/watch?v=4_9twnEduFA"""
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rect = pg.Rect

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            self.rect = pg.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        self.rect = pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pg.font.SysFont('comicsans', 30)
            text = font.render(self.text, True, (149, 53, 83))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                if self.rect.collidepoint(event.pos):
                    return True
        return False
