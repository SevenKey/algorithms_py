# 迪克斯特拉算法

class Dijkstra:

    def __init__(self):
        pass

    def build_costs_and_parents(self, nodes, start, end, costs, parents):
        queue_list = list()
        queue_list.append(start)
        while len(queue_list) > 0:
            node = queue_list.pop()
            neighbor_node_list = nodes.get(node)
            for neighbor_node in neighbor_node_list.keys():
                queue_list.append(neighbor_node)
                if (costs.get(neighbor_node) is None):
                    if (node == start):
                        costs[neighbor_node] = neighbor_node_list.get(neighbor_node)
                    else:
                        costs[neighbor_node] = -1
                if (parents.get(neighbor_node) is None):
                    if (node == start):
                        parents[neighbor_node] = node
                    else:
                        parents[neighbor_node] = -1
                if (end == neighbor_node):
                    return

    def get_lowest_node(self, costs, process):
        min_node = -1
        min_value = 100
        for node in costs.keys():
            if node not in process and costs[node] != -1 and costs[node] < min_value:
                min_node = node
                min_value = costs[node]
        process.append(min_node)
        return min_node

    def get_closest_path(self, nodes, start, end):
        costs = dict()
        parents = dict()
        process = list()
        self.build_costs_and_parents(nodes, start, end, costs, parents)

        node = self.get_lowest_node(costs, process)
        while node != -1:
            flat = False
            neighbor_node_list = nodes.get(node)
            for neighbor_node in neighbor_node_list.keys():
                if costs[neighbor_node] == -1 or costs[neighbor_node] > costs[node] + nodes[node][neighbor_node]:
                    costs[neighbor_node] = costs[node] + nodes[node][neighbor_node]
                    parents[neighbor_node] = node
                if (neighbor_node == end):
                    flat = True
                    break
            if flat:
                break
            else:
                node = self.get_lowest_node(costs, process)

        return parents