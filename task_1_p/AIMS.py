# let emplement class
from tabulate import tabulate
class Network:
    def __init__(self, input_network):
        self.network_matrix = self.parse_network(input_network)

    def parse_network(self, input_network):
        lines = input_network.strip().splitlines()
        return [[self.parse_cell(cell) for cell in row.split(',')] for row in lines if row.strip()]

    def parse_cell(self, cell):
        if cell.isdigit():
            return int(cell)
        else:
            return cell

    def Parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.Parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.Parent(parent, x)
        y_root = self.Parent(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
    # funcion to implement kruslal algorithm
    def kruskal_aloritm(self):
        num_nodes = len(self.network_matrix)
        parent = [i for i in range(num_nodes)]
        rank = [0] * num_nodes
        edges = []

        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if self.network_matrix[i][j] != '-':
                    edges.append((i, j, self.network_matrix[i][j]))

        edges.sort(key=lambda x: x[2])
        min_spanning_tree = []

        for edge in edges:
            root_x = self.Parent(parent, edge[0])
            root_y = self.Parent(parent, edge[1])

            if root_x != root_y:
                min_spanning_tree.append(edge)
                self.union(parent, rank, root_x, root_y)

        return min_spanning_tree
    # funcion to remove redundaty edjes
    def redundant_edges(self):
        min_spanning_tree = self.kruskal_aloritm()

        for i in range(len(self.network_matrix)):
            for j in range(len(self.network_matrix[i])):
                if self.network_matrix[i][j] != '-' and (i, j, self.network_matrix[i][j]) not in min_spanning_tree:
                    self.network_matrix[i][j] = '-'

    def calculate_saving(self):
        tot_cost = 0
        for i in range(len(self.network_matrix)):
            for j in range(i + 1, len(self.network_matrix[i])):
                if self.network_matrix[i][j] != '-':
                    tot_cost =tot_cost + self.network_matrix[i][j]
        return tot_cost

    def maximum_saving(self):
        self.redundant_edges()
        max_saving = self.calculate_saving()
        return max_saving

    def display_matrix(self):
        headers = [""] + ["A", "B", "C", "D", "E", "F", "G"]
        table = tabulate(self.network_matrix, headers=headers, tablefmt="pretty", stralign="center")
        print(table)
input_network = """-,14,10,19,-,-,-
14,-,-,15,18,-,-
10,-,-,26,-,29,-
19,15,26,-,16,17,21
-,-,18,16,-,-,9
-,-,29,17,-,-,25
-,-,29,17,-,-,25
-,-,-,21,9,25,-"""



net= Network(input_network)

print("Original Network:")
net.display_matrix()

max_saving = net.maximum_saving()
print("Orgin Saving:", max_saving)

net.redundant_edges()
updated_saving = net.calculate_saving()

print("\nUpdated Network:")
net.display_matrix()

print("Finall  savings:", updated_saving)
