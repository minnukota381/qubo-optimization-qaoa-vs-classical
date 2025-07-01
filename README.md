# 🧠 QUBO Solver Comparison: Classical vs Quantum (QAOA)

This repository demonstrates how to solve **QUBO (Quadratic Unconstrained Binary Optimization)** problems using:
- ✅ Classical brute-force search
- ⚛️ Quantum Approximate Optimization Algorithm (QAOA) with Qiskit

---

## 📌 What is QUBO?

A QUBO problem seeks to minimize a cost function:

```
C(x) = x^T Q x
```

Where:
- **x**: binary vector (e.g., [0, 1])
- **Q**: matrix defining interactions and weights
- The goal is to find **x** that gives the lowest cost

---

## 🧮 Classical Solver (Brute-force)

**File**: `qubo_solver_classical.py`

- Explores all possible binary combinations
- Calculates the cost for each using `C(x) = x^T Q x`
- Returns the bitstring with **minimum cost**

### Sample Output:
```
Best solution: (0, 0)
Minimum cost: 0
```

---

## ⚛️ Quantum Solver (QAOA)

**File**: `qubo_qaoa.py`

- Uses Qiskit's `QAOA` from `qiskit-algorithms`
- Converts the QUBO to an Ising Hamiltonian
- Solves using quantum simulation (via `qiskit-aer`)

### Sample Output:
```
📉 Minimum eigenvalue: -2.21
🏆 Best bitstring: 11
🎯 Probability: 57%
```

---

## 📊 QUBO Example Used

### Matrix Q:

```
Q = [[ 1, -2],
     [-2,  4]]
```

### Classical Cost Table:

| x₀ | x₁ | Cost     |
|----|----|----------|
| 0  | 0  | 0 ✅ Best |
| 0  | 1  | 4        |
| 1  | 0  | 1        |
| 1  | 1  | 1        |

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/minnukota381/qubo-optimization-qaoa-vs-classical.git
cd qubo-optimization-qaoa-vs-classical
```

### 2. Create & activate environment (Conda recommended)

```bash
conda create -n qiskit-env python=3.10
conda activate qiskit-env
pip install -r requirements.txt
```

### 3. Run the solvers

```bash
# Classical solver
python qubo_solver_classical.py

# Quantum (QAOA) solver
python qubo_qaoa.py
```

---

## 📦 Requirements

Create a `requirements.txt` file with:

```
qiskit>=0.45.0
qiskit-algorithms>=0.2.0
qiskit-aer>=0.12.0
numpy>=1.21.0
matplotlib>=3.5.0
```

---

## 🔍 How It Works

### Classical Approach
1. Generate all possible binary combinations for variables
2. For each combination, compute `C(x) = x^T Q x`
3. Track the combination with minimum cost
4. Return optimal solution

### Quantum Approach (QAOA)
1. Convert QUBO matrix to Ising Hamiltonian
2. Initialize quantum circuit with parameterized gates
3. Use classical optimization to tune quantum parameters
4. Measure quantum states to find approximate solution
5. Return most probable low-energy state

---

## 📈 Performance Comparison

| Method | Complexity | Accuracy | Scalability |
|--------|------------|----------|-------------|
| Classical | O(2ⁿ) | Exact | Poor (n < 20) |
| QAOA | O(poly(n)) | Approximate | Good (n > 100) |

---

## 🎯 Example Problems You Can Solve

- **Max-Cut**: Find optimal graph partitions
- **Portfolio Optimization**: Minimize risk while maximizing returns
- **Traveling Salesman**: Find shortest routes
- **Vertex Cover**: Find minimum vertex sets
- **Graph Coloring**: Optimize resource allocation

---

## 📌 Notes

- The classical solver is **exact** but doesn't scale well beyond ~20 variables
- The QAOA quantum solver is **approximate** but potentially scalable to larger problems
- This project demonstrates a simple, side-by-side comparison of both approaches
- Results may vary due to quantum noise and optimization landscape complexity

---

## 🔧 Troubleshooting

### Common Issues:
1. **Import Error**: Ensure all Qiskit packages are installed
2. **Memory Error**: Reduce problem size for classical solver
3. **Convergence Issues**: Try different QAOA parameters or optimizers

### Tips:
- Start with small problems (2-4 variables) to understand behavior
- Increase QAOA repetitions (`reps`) for better approximation
- Use different classical optimizers (COBYLA, SLSQP) if default fails

---

## 📚 References

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [QUBO Primer (D-Wave)](https://www.dwavesys.com/tutorials/background-reading-series/quantum-optimization)
- [QAOA Algorithm Paper](https://arxiv.org/abs/1411.4028)
- [Quantum Optimization Overview](https://quantum-computing.ibm.com/composer/docs/iqx/guide/quantum-algorithms)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request

---

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Minnu** - [GitHub Profile](https://github.com/minnukota381)
