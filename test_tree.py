import unittest

from node import Node
from tree import Tree


class TreeTestCase(unittest.TestCase):
    def test_find_1(self):
        tree = Tree()

        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)
        tree.printTree()
        self.assertEqual(tree.find(4).data, 4)

    def test_find_2(self):
        tree = Tree()

        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)
        tree.printTree()
        self.assertEqual(tree.find(9), None)


if __name__ == '__main__':
    unittest.main()
