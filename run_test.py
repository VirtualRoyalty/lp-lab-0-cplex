from main import *

method_dct = {False: 'LP', True: 'ILP'}


def run_tests(benchmarks: list):
    for filepath in benchmarks:
        try:
            graph = utils.read_graph_file(filepath, verbose=False)
        except Exception as e:
            print(e)
            continue
        for is_integer in [False, True]:
            max_clique_problem = design_problem(graph, is_integer=is_integer)
            max_clique_problem.set_log_stream(None)
            max_clique_problem.set_results_stream(None)
            max_clique_problem.set_warning_stream(None)
            print(f'Problem constructed for {filepath}!')

            print(f'Start solving {method_dct[is_integer]}...')
            time_lst = solve_problem(max_clique_problem)
            solution = max_clique_problem.solution.get_values()
            obj_value = max_clique_problem.solution.get_objective_value()
            print(f'Found max clique size (obj func value): {obj_value}')
            print(*[f'x{i}={value:.2f}' for i, value in enumerate(solution) if value != 0])
            mean_time = np.mean(time_lst)
            mins, secs = divmod(mean_time, 60)
            print(f'Execution time: {mins:.0f}min {secs:.1f}sec')
            print(f'for {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges\n')


if __name__ == '__main__':
    benches = ['benchmarks/DIMACS_all_ascii/hamming6-4.clq',
               'benchmarks/DIMACS_all_ascii/C125.9.clq',
               'benchmarks/DIMACS_all_ascii/brock200_1.clq',
               'benchmarks/DIMACS_all_ascii/brock200_2.clq'
               ]
    run_tests(benches)
