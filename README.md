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
$ python .\main.py --filepath .\benchmarks\DIMACS_all_ascii\brock200_2.clq --solver LP


Problem constructed for .\benchmarks\DIMACS_all_ascii\brock200_2.clq!
Start solving...
Found max clique size (obj func value): 30.28527190460359
x0=0.21 x3=0.15 x4=0.40 x6=0.07 x9=0.07 x10=0.09 x11=0.47 x13=0.29 x14=0.06 x15=0.13 x16=0.40 x17=0.08 x18=0.48 x19=0.18 x20=0.19 x21=0.08 x22=0.01 x25=0.07 x26=0.11 x27=0.03 x28=0.21 x30=0.14 x33=0.21 x34=0.01 x38=0.10 x39=0.43 x42=0.29 x43=0.15 x44=0.01 x47=0.34 x49=0.11 x51=0.17 x52=0.45 x53=0.45 x54=0.11 x56=0.18 x57=0.07 x58=0.11 x60=0.52 x61=0.20 x62=0.07 x63=0.01 x64=0.13 x66=0.23 x67=0.17 x69=0.24 x71=0.09 x72=0.43 x74=0.25 x75=0.20 x76=0.31 x78=0.07 x79=0.04 x80=0.20 x82=0.37 x83=0.55 x84=0.17 x86=0.52 x87=0.08 x88=0.11 x90=0.26 x95=0.34 x96=0.12 x99=0.03 x100=0.40 x101=0.03 x102=0.19 x103=0.01 x106=0.09 x108=0.29 x109=0.26 x110=0.08 x111=0.36 x113=0.32 x114=0.09 x115=0.26 x116=0.32 x117=0.48 x118=0.08 x119=0.07 x120=0.23 x121=0.04 x122=0.08 x123=0.41 x124=0.10 x128=0.30 x129=0.11 x131=0.11 x132=0.11 x133=0.27 x134=0.00 x135=0.22 x137=0.21 x138=0.12 x139=0.00 x141=0.28 x142=0.03 x143=0.27 x144=0.20 x145=0.34 x146=0.11 x147=0.52 x148=0.14 x149=0.32 x152=0.15 x154=0.08 x155=0.38 x157=0.15 x158=0.37 x159=0.23 x160=0.17 x161=0.06 x163=0.42 x164=0.19 x165=0.31 x166=0.05 x167=0.47 x169=0.28 x170=0.45 x171=0.40 x172=0.45 x174=0.02 x175=0.23 x176=0.08 x177=0.40 x178=0.41 x179=0.28 x180=0.32 x182=0.40 x183=0.20 x184=0.22 x185=0.24 x186=0.13 x187=0.22 x188=0.14 x189=0.15 x190=0.18 x191=0.09 x193=0.16 x194=0.27 x195=0.05 x196=0.15 x197=0.48 x199=0.20
Execution time: 0min 0.2sec
for 200 nodes and 9876 edges
```

```
$ python .\main.py --filepath .\benchmarks\DIMACS_all_ascii\brock200_2.clq --solver ILP

Problem constructed for .\benchmarks\DIMACS_all_ascii\brock200_2.clq!
Start solving...
Found max clique size (obj func value): 12.0
x26=1.0 x47=1.0 x54=1.0 x69=1.0 x104=1.0 x119=1.0 x120=1.0 x134=1.0 x144=1.0 x148=1.0 x157=1.0 x182=1.0
Execution time: 0min 26.8sec
for 200 nodes and 9876 edges

```
