import time
import functools
import networkx as nx
import argparse


def read_graph_file(file_path, verbose=True):
    edges = []
    file = open(file_path, 'r')
    for line in file:
        if line.startswith('c'):  # graph description
            if verbose:
                print(*line.split()[1:])
        elif line.startswith('p'):
            _, _, n_nodes, n_edges = line.split()
            if verbose:
                print(f'Nodes:  {n_nodes} Edges: {n_edges}')
        elif line.startswith('e'):
            _, node_i, node_j = line.split()
            edges.append((int(node_i), int(node_j)))
        else:
            continue
    g = nx.Graph(edges)
    assert int(n_nodes) == g.number_of_nodes()
    assert int(n_edges) == g.number_of_edges()
    return g


def timer(func, n_times=1):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        time_lst = []
        for i in range(n_times):
            tic = time.perf_counter()
            _ = func(*args, **kwargs)
            toc = time.perf_counter()
            elapsed_time = toc - tic
            time_lst.append(elapsed_time)
        return time_lst

    return wrapper_timer


def main_arg_parser():
    parser = argparse.ArgumentParser(description='Solve maximum clique problem by CPLEX solver')
    parser.add_argument('--filepath', type=str, required=True,
                        help='Path to DIMACS-format file')
    parser.add_argument('--solver', type=str, required=True,
                        choices=["LP", "ILP"],
                        help='Solve problem via  LP or ILP manner')
    parser.add_argument('--verbose', type=bool, default=False,
                        help='Whether to stream solver logs')
    return parser.parse_args()
