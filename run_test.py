from main import *

EASY = {
    'benchmarks/DIMACS_all_ascii/johnson8-2-4.clq': 4,
    'benchmarks/DIMACS_all_ascii/johnson16-2-4.clq': 8,
    'benchmarks/DIMACS_all_ascii/MANN_a9.clq': 16,
    'benchmarks/DIMACS_all_ascii/keller4.clq': 11,
    'benchmarks/DIMACS_all_ascii/hamming8-4.clq': 16,
}

MEDIUM = {
    'benchmarks/DIMACS_all_ascii/C125.9.clq': 34,
    'benchmarks/DIMACS_all_ascii/gen200_p0.9_44.clq': 44,
    'benchmarks/DIMACS_all_ascii/gen200_p0.9_55.clq': 55,
    'benchmarks/DIMACS_all_ascii/brock200_1.clq': 21,
    'benchmarks/DIMACS_all_ascii/brock200_2.clq': 12,
    'benchmarks/DIMACS_all_ascii/brock200_3.clq': 15,
    'benchmarks/DIMACS_all_ascii/brock200_4.clq': 17,
    # 'benchmarks/DIMACS_all_ascii/p_hat1000-1.clq': 10,
    # 'benchmarks/DIMACS_all_ascii/san1000.clq': 15,
}

HARD = {
    'benchmarks/DIMACS_all_ascii/brock400_1.clq': 27,
    'benchmarks/DIMACS_all_ascii/brock400_2.clq': 29,
    'benchmarks/DIMACS_all_ascii/brock400_3.clq': 31,
    'benchmarks/DIMACS_all_ascii/brock400_4.clq': 33,
    'benchmarks/DIMACS_all_ascii/MANN_a27.clq': 126,
    'benchmarks/DIMACS_all_ascii/MANN_a45.clq': 345,
    'benchmarks/DIMACS_all_ascii/sanr400_0.7.clq': 21,
    'benchmarks/DIMACS_all_ascii/sanr400_0.9.clq': 42,
    'benchmarks/DIMACS_all_ascii/p_hat1000-2.clq': 46,
    'benchmarks/DIMACS_all_ascii/p_hat500-3.clq': 50,
    'benchmarks/DIMACS_all_ascii/p_hat1500-1.clq': 12,
    'benchmarks/DIMACS_all_ascii/p_hat300-3.clq': 36,
}


def run_tests(benchmarks: list):
    total_time = 0
    method_dct = {False: 'LP', True: 'ILP'}
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
            total_time += mean_time
            mins, secs = divmod(mean_time, 60)
            print(f'Execution time: {mins:.0f}min {secs:.1f}sec')
            print(f'for {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges')
            print(f'And clique of size {benchmarks[filepath]}!\n')

    mins, secs = divmod(total_time, 60)
    print(f"\n\n*****Total time is {mins:.1f}min {secs:.1f}sec ******")


if __name__ == '__main__':
    run_tests(MEDIUM)
