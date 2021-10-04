# Max clique problem  via CPLEX

Альперович Вадим <br>
ИАД21

### Пример запуска:

LP problem:

```python

python main.py --filepath benchmarks\DIMACS_all_ascii\C125.9.clq --solver LP

```
 ILP problem:
 
```python

python main.py --filepath benchmarks\DIMACS_all_ascii\C125.9.clq --solver ILP

```

### Запуск тестов:

LP problem:

```python

python run_test.py

```

**Пример вывода:**
```
$ python .\main.py --filepath .\benchmarks\DIMACS_all_ascii\brock200_2.cl
q --solver ILP

Problem constructed for .\benchmarks\DIMACS_all_ascii\brock200_2.clq!
Start solving...
Found max clique size (obj func value): 12.0
x26=1.0 x47=1.0 x54=1.0 x69=1.0 x104=1.0 x119=1.0 x120=1.0 x134=1.0 x144=1.0 x148=1.0 x157=1.0 x182=1.0
Execution time: 0min 26.8sec
for 200 nodes and 9876 edges

```
