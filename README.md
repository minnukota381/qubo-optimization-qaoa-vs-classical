# 🧠 QUBO Solver (Classical)

This is a simple Python demo that solves a small **QUBO (Quadratic Unconstrained Binary Optimization)** problem using brute-force on a classical computer.

---

## 🔸 What is QUBO?

QUBO stands for **Quadratic Unconstrained Binary Optimization**.

It is used to solve problems where:
- You have binary variables (0 or 1),
- You want to **minimize a quadratic cost function** of the form:

\[
C(x) = x^T Q x
\]

where:
- `x` is a vector of binary variables (e.g., `[x₀, x₁, x₂, ...]`)
- `Q` is a matrix defining the cost/energy
- Your goal is to find the bitstring `x` that gives the **minimum value** for this expression

---

## 🛠️ How It Works

The script:
1. Defines a small QUBO matrix
2. Enumerates all binary combinations (e.g., `[0, 0]`, `[0, 1]`, etc.)
3. Calculates the cost for each
4. Returns the combination with the **lowest cost**
5. Optionally shows a bar plot of all costs

---

## 🔢 Example: 2-variable QUBO

### QUBO Matrix Used

\[
Q = \begin{bmatrix}
1 & -2 \\
-2 & 4
\end{bmatrix}
\]

This defines the cost function:

\[
C(x_0, x_1) = x_0 - 2x_0x_1 + 4x_1
\]

### Brute-force Evaluation:

| x₀ | x₁ | Cost  |
|----|----|-------|
| 0  | 0  | 0 ✅ Best |
| 0  | 1  | 4     |
| 1  | 0  | 1     |
| 1  | 1  | 1     |

### Output:
