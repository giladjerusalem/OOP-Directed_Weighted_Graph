import os
import sys
import unittest

myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path

path = Path(myDir)
a = str(path.parent.absolute())

sys.path.append(a)
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.Tests.GraphCreator import GraphCreator


class MyTestCase(unittest.TestCase):
    def test_connected(self):
        g1 = GraphCreator(1, 0, 0)  # Graph without Edges without nodes have to be true
        graph1 = g1.create_graph()
        g_algo1 = GraphAlgo(graph1)
        self.assertEqual(True, g_algo1.connected())
        g1 = GraphCreator(1, 10, 0)  # Graph without Edges
        graph1 = g1.create_graph()
        g_algo1 = GraphAlgo(graph1)
        self.assertEqual(False, g_algo1.connected())
        g1 = GraphCreator(1, 5, 20)  # This graph is full connected graph have to be connected
        graph1 = g1.create_graph()
        g_algo1 = GraphAlgo(graph1)
        self.assertEqual(True, g_algo1.connected())  # This graph is full connected graph have to be connected
        g1 = GraphCreator(1, 10, 90)
        graph1 = g1.create_graph()
        g_algo1 = GraphAlgo(graph1)
        self.assertEqual(True, g_algo1.connected())
        g1 = GraphCreator(1, 100, 2000)
        graph1 = g1.create_graph()
        g_algo1 = GraphAlgo(graph1)
        self.assertEqual(True, g_algo1.connected())
        # g1 = GraphCreator(1, 1000, 20000)
        # graph1 = g1.create_graph()
        # g_algo1 = GraphAlgo(graph1)
        # self.assertEqual(True, g_algo1.connected())  # Big graphs
        # g1 = GraphCreator(1, 10000, 200000)
        # graph1 = g1.create_graph()
        # g_algo1 = GraphAlgo(graph1)
        # self.assertEqual(True, g_algo1.connected())  # Big graphs
        # g1 = GraphCreator(1, 100000, 2000000)
        # graph1 = g1.create_graph()
        # g_algo1 = GraphAlgo(graph1)
        # self.assertEqual(True, g_algo1.connected())
        # g1 = GraphCreator(1, 1000000, 20000000)  # Big graphs
        # graph1 = g1.create_graph()
        # g_algo1 = GraphAlgo(graph1)
        # self.assertEqual(True, g_algo1.connected())

    def test_shortest_path(self):
        g = DiGraph()
        graph_algo = GraphAlgo(g)
        """Check when the graph is initialized but the graph is empty and there is no any nodes"""
        self.assertEqual(graph_algo.shortest_path(0, 5), (float('inf'), []))
        graph_algo.load_from_json('../../data/A0.json')
        self.assertEqual(graph_algo.shortest_path(0, 12), (float('inf'), []))  # Not exisitng
        self.assertEqual(graph_algo.shortest_path(0, 12), (float('inf'), []))
        self.assertEqual(graph_algo.shortest_path(13, 0), (float('inf'), []))
        self.assertEqual(graph_algo.shortest_path(13, 15), (float('inf'), []))
        p, g = graph_algo.shortest_path(0, 5)
        self.assertEqual((p, g), (7.683118665386805, [0, 1, 2, 3, 4, 5]))
        g = GraphCreator(0, 10000, 200000).create_graph()
        graph_algo1 = GraphAlgo(g)
        self.assertEqual(graph_algo1.shortest_path(0, 58),
                         (2.1429180470121922, [0, 9281, 1499, 1786, 189, 9865, 58]))

    def test_all_center_json_and_load(self):
        graph_algo = GraphAlgo(DiGraph())
        self.assertEqual(False, graph_algo.load_from_json('Not_Existing_Path'))
        self.assertEqual(graph_algo.centerPoint(), (-1, float('inf')))  # Empty Graph check
        self.assertEqual(True, graph_algo.load_from_json('../../data/A0.json'))
        self.assertEqual((7, 6.806805834715163), graph_algo.centerPoint())
        graph_algo1 = GraphAlgo(DiGraph())
        self.assertEqual(True, graph_algo1.load_from_json('../../data/A1.json'))
        self.assertEqual((8, 9.925289024973141), graph_algo1.centerPoint())
        graph_algo2 = GraphAlgo(DiGraph())
        self.assertEqual(True, graph_algo2.load_from_json('../../data/A2.json'))
        self.assertEqual((0, 7.819910602212574), graph_algo2.centerPoint())
        graph_algo3 = GraphAlgo(DiGraph())
        self.assertEqual(True, graph_algo3.load_from_json('../../data/A3.json'))
        self.assertEqual((2, 8.182236568942237), graph_algo3.centerPoint())
        graph_algo4 = GraphAlgo(DiGraph())
        self.assertEqual(True, graph_algo4.load_from_json('../../data/A4.json'))
        self.assertEqual((6, 8.071366078651435), graph_algo4.centerPoint())
        graph_algo5 = GraphAlgo(DiGraph())
        self.assertEqual(True, graph_algo5.load_from_json('../../data/A5.json'))
        self.assertEqual((40, 9.291743173960954), graph_algo5.centerPoint())

    # def test_save_to_json(self):
    #     graph_algo = GraphAlgo(GraphCreator(0, 1000, 20000).create_graph())
    #     self.assertEqual(True, graph_algo.save_to_json('../../compare/compare_test_1k_nodes_20k_edges.json'))
    #     graph_algo = GraphAlgo(GraphCreator(0, 10000, 200000).create_graph())
    #     self.assertEqual(True, graph_algo.save_to_json('../../compare/compare_test_10k_nodes_200k_edges.json'))

    def test_all_center_for_compare0(self):
        """50 Seconds"""
        graph_algo = GraphAlgo(GraphCreator(0, 1000, 20000).create_graph())
        self.assertEqual((898, 1.617561652543007), graph_algo.centerPoint())

        # def test_all_center_for_compare1(self):
        """Timed OUT TO MUCH TIME MORE THAN 1 HOUR!!!"""

    #     graph_algo = GraphAlgo(GraphCreator(0, 10000, 200000).create_graph())
    #     print(graph_algo.centerPoint())

    def test_tsp(self):
        graph_algo = GraphAlgo(DiGraph())
        self.assertEqual(([], -1), graph_algo.TSP([1]))  # test on empty graph
        graph_algo.load_from_json('../../data/subGraph.json')
        self.assertEqual(([], -1), graph_algo.TSP([1]))  # not Empty graph but list with only 1 node
        self.assertEqual((3.0, [1, 2, 3, 4]), graph_algo.TSP([1, 4]))
        self.assertEqual(([], -1), graph_algo.TSP([1, 9]))  # 9 id_node doesn't exit in the graph
        self.assertEqual(([0, 1, 5], 2.0), graph_algo.TSP([0, 1, 5]))  # CHECK ON CONNECTED GRAPH
        graph_algo.get_graph().remove_edge(0, 1)
        graph_algo.get_graph().remove_edge(1, 0)
        self.assertEqual(False, graph_algo.connected())  # now the graph is not connected isolate 0 node_id
        graph_algo.TSP([0, 2, 4])
        self.assertEqual(([], -1), graph_algo.TSP([0, 2, 4]))

    # def test_tsp_comparesion(self):
    #     graph_algo = GraphAlgo(DiGraph())
    #     graph_algo.load_from_json("compare_test_1m_nodes_20m_edges.json")

    # def test_save_to_json(self):
    #     graph_algo = GraphAlgo(GraphCreator(0, 1000, 20000).create_graph())
    #     self.assertEqual(True, graph_algo.save_to_json('../../compare/compare_test_1k_nodes_20k_edges.json'))
    #
    # def test_save_to_json1(self):
    #     graph_algo = GraphAlgo(GraphCreator(0, 10000, 200000).create_graph())
    #     self.assertEqual(True, graph_algo.save_to_json('../../compare/compare_test_10k_nodes_200k_edges.json'))
    #
    # def test_save_to_json2(self):
    #     graph_algo = GraphAlgo(GraphCreator(0, 100000, 2000000).create_graph())
    #     self.assertEqual(True, graph_algo.save_to_json('../../compare/compare_test_100k_nodes_2m_edges.json'))
    #
    # def test_save_to_json3(self):
    #     graph_algo = GraphAlgo(GraphCreator(0, 1000000, 20000000).create_graph())
    #     self.assertEqual(True, graph_algo.save_to_json('../../compare/compare_test_1m_nodes_20m_edges.json'))
    #
    # def test_load_from_json(self):
    #     graph_algo = GraphAlgo(DiGraph())
    #     self.assertEqual(True, graph_algo.load_from_json('../../compare/compare_test_1k_nodes_20k_edges.json'))
    #
    # def test_load_from_json1(self):
    #     graph_algo = GraphAlgo(DiGraph())
    #     self.assertEqual(True, graph_algo.load_from_json('../../compare/compare_test_10k_nodes_200k_edges.json'))
    #
    # def test_load_from_json2(self):
    #     graph_algo = GraphAlgo(DiGraph())
    #     self.assertEqual(True, graph_algo.load_from_json('../../compare/compare_test_100k_nodes_2m_edges.json'))

    # def test_load_from_json3(self):
    #     graph_algo = GraphAlgo(DiGraph())
    #     self.assertEqual(True, graph_algo.load_from_json('../../compare/compare_test_1m_nodes_20m_edges.json'))


if __name__ == '__main__':
    unittest.main()
