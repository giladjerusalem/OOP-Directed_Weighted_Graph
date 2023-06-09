import os
import sys
import unittest

myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path

path = Path(myDir)
a = str(path.parent.absolute())

sys.path.append(a)
from src.NodeData import NodeData
from GraphCreator import GraphCreator


class MyTestCase(unittest.TestCase):
    def test_graph_10kNodes_200kEdges(self):
        num_of_nodes = 10000
        num_of_edges = 200000
        graph = GraphCreator(0, num_of_nodes, num_of_edges)
        g = graph.create_graph()
        self.assertEqual(num_of_nodes, g.v_size())
        self.assertEqual(num_of_edges, g.e_size())

    # def test_graph_100kNodes_2mEdges(self):
    #     num_of_nodes = 100000
    #     num_of_edges = 2000000
    #     graph = GraphCreator(0, num_of_nodes, num_of_edges)
    #     g = graph.create_graph()
    #     self.assertEqual(num_of_nodes, g.v_size())
    #     self.assertEqual(num_of_edges, g.e_size())
    #
    # def test_graph_1MNodes_20mEdges(self):
    #     num_of_nodes = 1000000
    #     num_of_edges = 20000000
    #     graph = GraphCreator(0, num_of_nodes, num_of_edges)
    #     g = graph.create_graph()
    #     self.assertEqual(num_of_nodes, g.v_size())
    #     self.assertEqual(num_of_edges, g.e_size())

    def test_add_and_get_node(self):
        num_of_nodes = 1000
        num_of_edges = 20000
        graph = GraphCreator(0, num_of_nodes, num_of_edges)
        g = graph.create_graph()
        self.assertEqual(g.v_size(), num_of_nodes)  #
        pos = g.get_node(num_of_nodes - 1).get_pos()
        node = NodeData(num_of_nodes - 1)
        node.set_pos(pos[0], pos[1], pos[2])
        print(g.get_node(num_of_nodes - 1) == node)
        self.assertEqual(g.get_node(num_of_nodes - 1), node)
        self.assertEqual(None, g.get_node(num_of_nodes))
        g.add_node(num_of_nodes, (35.013013232, 32.13232323, 0))
        self.assertEqual(num_of_nodes + 1, g.v_size())
        self.assertEqual(False, g.add_node(22, pos))  # Already exist key

    def test_add_edge(self):
        num_of_nodes = 100
        num_of_edges = 2000
        graph = GraphCreator(0, num_of_nodes, num_of_edges)
        g = graph.create_graph()
        self.assertEqual(num_of_edges, g.e_size())
        self.assertEqual(False, g.add_edge(12, 1000, 1.2342))
        self.assertEqual(False, g.add_edge(123, 43, 1.23221))
        self.assertEqual(False, g.add_edge(101, 102, 1.234))
        self.assertEqual(False, g.add_edge(58, 99, -30))
        self.assertEqual(True, g.add_edge(58, 99, 1.232))
        self.assertEqual(False, g.add_edge(58, 99, 1000))

    def test_remove_edge(self):
        num_of_nodes = 5
        num_of_edges = 20
        graph = GraphCreator(0, num_of_nodes, num_of_edges)  # Means that the specific graph is Complete Graph
        g = graph.create_graph()
        self.assertEqual(True, g.remove_edge(0, 1))
        self.assertEqual(num_of_edges - 1, g.e_size())
        self.assertEqual(False, g.remove_edge(4, 6))
        self.assertEqual(False, g.remove_edge(6, 4))
        for key in g.get_all_v():
            for value in list(g.all_out_edges_of_node(key)):
                g.remove_edge(key, value)
        print(g.get_edge_out())
        self.assertEqual(0, g.e_size())
        self.assertEqual(False, g.remove_edge(0, 1))

    def test_remove_node(self):
        num_of_nodes = 3
        num_of_edges = 6
        graph = GraphCreator(0, num_of_nodes, num_of_edges)  # Means that the specific graph is Complete Graph
        g = graph.create_graph()
        self.assertEqual(g.v_size(), 3)
        self.assertEqual(False, g.remove_node(5))
        for node_id in list(g.get_all_v()):
            g.remove_node(node_id)
        self.assertEqual(g.v_size(), 0)
        self.assertEqual(g.e_size(), 0)
        self.assertEqual(False, g.remove_node(32))


if __name__ == '__main__':
    unittest.main()
