import numpy as np
import itertools
import matplotlib.pyplot as plt

# Define the QUBO matrix (2-variable example)
# You can change this matrix to try other problems
Q = np.array([[1, -2],
              [-2, 4]])

def qubo_cost(x, Q):
    """Calculate the QUBO cost: x^T Q x"""
    x = np.array(x)
    return x.T @ Q @ x

def solve_qubo_brute_force(Q):
    n = Q.shape[0]
    best_solution = None
    min_cost = float('inf')
    all_results = []

    # Try all 2^n binary combinations
    for bits in itertools.product([0, 1], repeat=n):
        cost = qubo_cost(bits, Q)
        all_results.append((bits, cost))
        if cost < min_cost:
            min_cost = cost
            best_solution = bits

    return best_solution, min_cost, all_results

# Solve QUBO
solution, cost, all_results = solve_qubo_brute_force(Q)

print("Best solution:", solution)
print("Minimum cost:", cost)

# Optional: Plot energy landscape
bitstrings = [''.join(map(str, x)) for x, _ in all_results]
energies = [c for _, c in all_results]

plt.figure(figsize=(8, 4))
plt.bar(bitstrings, energies, color='skyblue')
plt.xlabel("Bitstring")
plt.ylabel("QUBO Cost")
plt.title("QUBO Energy Landscape")
plt.grid(True)
plt.tight_layout()
plt.show()
