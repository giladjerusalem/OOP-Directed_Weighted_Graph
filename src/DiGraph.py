from GraphInterface import GraphInterface
from NodeData import NodeData


class DiGraph(GraphInterface):
    """This is the main class which represent graphs """

    def __init__(self):
        self._edgeOut = {}
        self._edgeIn = {}
        self._nodes = {}
        self._with_pos = False
        self._edge_size = 0
        self._mc = 0

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        if self._nodes and id1 in self._nodes:
            return self._edgeIn[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        if self._nodes and id1 in self._nodes:
            return self._edgeOut[id1]

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        if self._nodes:
            return self._nodes

    def v_size(self) -> int:
        """
         Returns the number of vertices in this graph
         @return: The number of vertices in this graph
         """
        return len(self._nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self._edge_size

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self._mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 != id2 and id1 in self._nodes and id2 in self._nodes and id2 not in self._edgeOut[id1] and weight > 0:
            self._edgeOut[id1][id2] = weight
            self._edgeIn[id2][id1] = weight
            self._edge_size = self._edge_size + 1
            self._mc = self._mc + 1
            return True
        return False

    def get_node(self, node_id: int) -> NodeData:
        """
         Return object type NodeData
         @param node_id: Integer value which represent node in the graph
         @return: NodeData if the node_id exist in the dict
        """
        if node_id in self._nodes:
            return self._nodes.get(node_id)

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if node_id in self._nodes:
            return False
        node = NodeData(node_id)
        if pos:
            node.set_pos(float(pos[0]), float(pos[1]), float(pos[2]))
            self._with_pos = True
        else:
            self._with_pos = False
        self._nodes[node_id] = node
        self._edgeOut[node_id] = {}
        self._edgeIn[node_id] = {}
        self._mc = self._mc + 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if node_id in self._nodes:
            for vert_out in list(self.all_out_edges_of_node(node_id)):
                self.remove_edge(node_id, vert_out)
            for vert_in in list(self.all_in_edges_of_node(node_id)):
                self.remove_edge(vert_in, node_id)
            self._nodes.pop(node_id)
            self._edgeIn.pop(node_id)
            self._edgeOut.pop(node_id)
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 in self._nodes and node_id2 in self._nodes and self._edgeOut.get(node_id1).get(node_id2):
            self._edgeOut.get(node_id1).pop(node_id2)
            self._edgeIn.get(node_id2).pop(node_id1)
            self._edge_size = self._edge_size - 1
            self._mc = self._mc + 1
            return True
        return False

    def get_edge_out(self) -> dict:
        return self._edgeOut

    def get_edge_in(self) -> dict:
        return self._edgeIn

    def get_with_pos(self):
        return self._with_pos

    def __repr__(self):
        """
        Comfortable representation of the graph
        """
        ans = "Graph: |V|=" + str(len(self._nodes)) + " |E|: " + str(self._edge_size) + "\n"
        ans += "{"
        counter = 0
        for node in self._nodes:
            counter += 1

            ans += str(node) + ": " + str(node) + ' |edges out| ' + str(self.all_out_edges_of_node(node)) + '' \
                                                                                                            '|edges in| ' + str(
                self.all_in_edges_of_node(node))
            if counter < len(self._nodes) - 1:
                ans += ', '
            else:
                ans += '}'
        return ans



