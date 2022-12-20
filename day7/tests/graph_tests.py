import unittest
from node import Node


class GraphTests(unittest.TestCase):
    def test_nodes_are_equal(self):
        node_A = Node('A')
        node_A.leaves = []
        node_A.children = []

        node_B = Node('A')
        node_B.leaves = []
        node_B.children = []

        self.assertEqual(node_A, node_B)

    def test_nodes_are_not_equal_leaves(self):
        node_A = Node('A')
        node_A.leaves = []
        node_A.children = []

        node_B = Node('A')
        node_B.leaves = [5]
        node_B.children = []

        self.assertNotEqual(node_A, node_B)

    def test_nodes_are_not_equal_children(self):
        node_B = Node('B')
        node_B.leaves = []
        node_B.children = []

        node_A = Node('A')
        node_A.leaves = []
        node_A.children = [Node('B')]

        self.assertNotEqual(node_A, node_B)

    def test_nodes_are_not_equal_label(self):
        node_A = Node('A')
        node_A.leaves = []
        node_A.children = []

        node_B = Node('B')
        node_B.leaves = []
        node_B.children = []

        self.assertNotEqual(node_A, node_B)

    def test_node_to_str(self):
        node_A = Node('A')
        node_A.leaves = ['a']
        node_A.children = [Node('B')]

        expected_string = "Node Label: A, Leaves: ['a'], Children: ['B']\nNode Label: B, Leaves: [], Children: []"
        self.assertEqual(expected_string, str(node_A))
