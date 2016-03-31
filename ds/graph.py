import logging
from collections import Hashable

class Node(object):
    """ Node that can be used in a directed graph"""

    def __init__(self, node_id, children=None, parents=None):
        self.id = node_id
        self.children = children
        self.parents = parents

class DirectedGraph(object):
    """ A simple base class for directed graphs """

    def __init__(self, node_t=Node):
        """
        :param node_t: (optional) class type to use when initializing the nodes of the graph,
            should have attributes: children and parents of type {node_id:(weight,referenced_node)}
            class members:
            __init__(self, node_id, children=None, parents=None)
        :return:
        """
        self._node_t = node_t
        self.nodes = {}

    def add_vertex(self, from_id, to_id, w):
        if from_id not in self.nodes:
            self.nodes[from_id] = self._node_t(from_id, parents={}, children={})
        if to_id not in self.nodes:
            self.nodes[to_id] = self._node_t(to_id, parents={}, children={})
        self.nodes[from_id].children[to_id] = [w, self.nodes[to_id]]
        self.nodes[to_id].parents[from_id] = [w, self.nodes[from_id]]

    def delete_vertex(self, from_id, to_id):
        if from_id not in self.nodes or to_id not in self.nodes:
            logging.warning("no vertex is found for deletion")
            return
        d1 = self.nodes[from_id].children.pop(to_id, d=None)
        d2 = self.nodes[to_id].parents.pop(from_id, d=None)
        if d1 is None or d2 is None:
            logging.warning("no vertex is found for deletion")

    def add_node(self, node):
        self.nodes[node.id] = node

    def delete_node(self, node_id):
        if node_id not in self.nodes:
            logging.warning("no node is found for deletion")
            return
        for child in self.nodes[node_id].children:
            self.delete_vertex(node_id, child.id)
        for parent in self.nodes[node_id].parents:
            self.delete_vertex(parent.id, node_id)
        self.nodes.pop(node_id, d=None)



class SinglyLinkedNode(object):
    """ lightweight node to contstruct simple chains and trees"""

    def __init__(self, node_id, linked_node=None):
        self.id = node_id
        self.link = linked_node


"""def has_disconnected_cycles(self, direction=-1):
        safe_nodes = set()
        if direction==-1:
            safe_dict = self.backward_root.parents
        elif direction==1:
            safe_dict = self.forward_root.children
        for _, node in safe_dict.items():
            safe_nodes.add(node.i)
        return len()"""
