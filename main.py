import cplex
import numpy as np
import networkx as nx
import utils

STRATEGIES = [
    nx.coloring.strategy_largest_first,
    nx.coloring.strategy_random_sequential,
    nx.coloring.strategy_independent_set,
    nx.coloring.strategy_connected_sequential_bfs,
    nx.coloring.strategy_connected_sequential_dfs,
    nx.coloring.strategy_saturation_largest_first
]


def get_complement_edges(graph: nx.Graph) -> list:
    complement_g = nx.complement(graph)
    adj_matrix = nx.adjacency_matrix(complement_g).todense()
    adj_matrix = np.triu(adj_matrix, k=1)
    pairs = np.where(adj_matrix == 1)
    complement_edges = list(zip(pairs[0] + 1, pairs[1] + 1))
    # print(len(complement_edges))
    return complement_edges


def get_independent_sets(graph: nx.Graph, strategies: list) -> list:
    independent_sets = []
    for strategy in strategies:
        d = nx.coloring.greedy_color(graph, strategy=strategy)
        for color in set(color for node, color in d.items()):
            color_set = tuple(sorted([int(key) for key, value in d.items() if value == color]))
            if len(color_set) > 2:
                independent_sets.append(color_set)
    independent_sets = list(set(independent_sets))
    return independent_sets


def design_problem(graph: nx.Graph, is_integer=False) -> cplex.Cplex:
    # specify numeric type for ILP/LP problem
    one = 1 if is_integer else 1.0
    zero = 0 if is_integer else 0.0

    # get not connected edges and list of independent sets
    not_connected = get_complement_edges(graph)
    independent_sets = get_independent_sets(graph, strategies=STRATEGIES)

    # define num of decision vars by num of nodes
    # and num of constraints as num of not connected edges + num of found ind sets
    nodes = sorted(graph.nodes())
    n_vars = graph.number_of_nodes()
    n_constraints = len(not_connected) + len(independent_sets)

    # define upper and lower bounds for vars
    upper_bounds = [one] * n_vars
    lower_bounds = [zero] * n_vars
    # define objective x_1 + x_2 + ... + x_n -> max
    obj = [one] * n_vars
    # define var and constraint names
    var_names = [f'x{i}' for i in nodes]
    constraint_names = [f'c{i + 1}' for i in range(n_constraints)]
    # constraint type L is less than, i. e. x_i + x_j <= 1
    constraint_senses = ['L'] * n_constraints
    right_hand_side = [one] * n_constraints

    # initialize cplex solver
    problem = cplex.Cplex()
    # add vars, obj and bounds
    problem.variables.add(obj=obj, names=var_names, ub=upper_bounds, lb=lower_bounds)

    # collect constraints and var types
    constraints = []
    for ind_set in independent_sets:
        constraints.append([[f'x{i}' for i in ind_set], [1.0] * len(ind_set)])
    for i, j in not_connected:
        constraints.append([[f'x{i}', f'x{j}'], [1.0, 1.0]])

    _type = problem.variables.type.binary if is_integer else problem.variables.type.continuous
    for node in nodes:
        problem.variables.set_types(f'x{node}', _type)

    # add constraints and var types
    problem.linear_constraints.add(lin_expr=constraints,
                                   senses=constraint_senses,
                                   rhs=right_hand_side,
                                   names=constraint_names)
    # set objective func as maximization problem
    problem.objective.set_sense(problem.objective.sense.maximize)
    return problem


@utils.timer
def solve_problem(some_problem: cplex.Cplex):
    some_problem.solve()


if __name__ == '__main__':

    args = utils.main_arg_parser()
    ILP = True if args.solver == 'ILP' else False
    filepath = args.filepath  # 'benchmarks/DIMACS_all_ascii/C125.9.clq'
    G = utils.read_graph_file(filepath)
    max_clique_problem = design_problem(G, is_integer=ILP)
    if not args.verbose:
        max_clique_problem.set_log_stream(None)
        max_clique_problem.set_results_stream(None)
        max_clique_problem.set_warning_stream(None)
    print(f'Problem constructed for {filepath}!')

    # solve problem
    print('Start solving...')
    time_lst = solve_problem(max_clique_problem)
    solution = max_clique_problem.solution.get_values()
    obj_value = max_clique_problem.solution.get_objective_value()
    print(f'Found max clique size (obj func value): {obj_value}')
    print(*[f'x{i}={value:.2f}' for i, value in enumerate(solution) if value != 0])

    mean_time = np.mean(time_lst)
    mins, secs = divmod(mean_time, 60)
    print(f'Execution time: {mins:.0f}min {secs:.1f}sec')
    print(f'for {G.number_of_nodes()} nodes and {G.number_of_edges()} edges\n')

