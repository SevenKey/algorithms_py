import unittest
from classical import Dijkstra


class TestClassical(unittest.TestCase):

    def test_dijkstra(self):
        maps = dict()

        maps[1] = dict()
        maps[1][2] = 3
        maps[1][3] = 7

        maps[2] = dict()
        maps[2][3] = 1
        maps[2][4] = 1

        maps[3] = dict()
        maps[3][4] = 6

        maps[4] = dict()
        maps[4][5] = 2

        start = 2
        end = 5
        dijkstra = Dijkstra.Dijkstra()
        parents = dijkstra.get_closest_path(nodes=maps, start=start, end=end)
        node_list = list()
        temp = end
        while (temp != start):
            for node in parents.keys():
                if (node == temp):
                    node_list.append(node)
                    temp = parents[node]
        node_list.append(start)
        node_list.reverse()
        true_list = [2, 4, 5]
        self.assertListEqual(node_list, true_list)


if __name__ == '__main__':
    unittest.main()
