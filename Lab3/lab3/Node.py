import random

class Node():

    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.neighbours = []

    def edge(self, node):
        self.neighbours.append(node)

    def __str__(self):
        return f'({self.vertex_number})'

    def get_out_degree(self):
        return len(self.neighbours)

def create_graph(file_path):
    nodes_dict = {}

    with open(file_path, 'r') as f:
        lines = f.readlines()

        for line in lines[1:]:
            n1, n2 = line.strip().split()

            if n1 not in nodes_dict:
                nodes_dict[n1] = Node(n1)
            if n2 not in nodes_dict:
                nodes_dict[n2] = Node(n2)

            nodes_dict[n1].edge(nodes_dict[n2])
    return list(nodes_dict.values())

def print_graph(graph):
    for node in graph:
        for neighbour in node.neighbours:
            print(f"{node} -> {neighbour}")

def highest_out_degree(graph):
    if not graph:
        return None
    return max(graph, key=lambda n: n.get_out_degree())

def create_random_subgraph(graph):
    num_nodes = max(1, int(len(graph)*0.6))
    selected_nodes = random.choices(graph, k=num_nodes)

    subgraph_dict = {node.vertex_number: Node(node.vertex_number) for node in selected_nodes}

    for old_node in selected_nodes:
        num_edges = int(old_node.get_out_degree() * 0.8)

        if num_edges > 0:
            selected_edges = random.choices(old_node.neighbours, k=num_edges)

            for target_node in selected_edges:
                if target_node.vertex_number in subgraph_dict:
                    source = subgraph_dict[old_node.vertex_number]
                    target = subgraph_dict[target_node.vertex_number]
                    source.edge(target)

    return list(subgraph_dict.values())


if __name__ == "__main__":
    graf_lista = create_graph("graph1.txt")

    print("GRAFUL INITIAL:")
    print_graph(graf_lista)

    nod_max = highest_out_degree(graf_lista)
    print(f"\nNodul cu cel mai mare out-degree: {nod_max} (are {nod_max.get_out_degree()} vecini)")

    subgraf = create_random_subgraph(graf_lista)
    print("\nSUBGRAFUL GENERAT ALEATOR:")
    print_graph(subgraf)