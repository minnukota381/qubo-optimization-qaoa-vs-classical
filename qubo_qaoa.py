from qiskit_algorithms.minimum_eigensolvers import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import Sampler
from qiskit_aer.primitives import Sampler as AerSampler

# Define a simple 2-variable QUBO:
# Minimize: x1 + x2 - 2*x1*x2
# QUBO matrix: [[1, -1], [-1, 1]]
# Convert to equivalent Ising (Z) operator: H = ZI + IZ - 2 * ZZ

qubo_pauli = SparsePauliOp.from_list([
    ("ZI", 1.0),
    ("IZ", 1.0),
    ("ZZ", -2.0)
])

# Set up the QAOA solver
optimizer = COBYLA(maxiter=100)
sampler = Sampler()  # or AerSampler() for simulation backend
qaoa = QAOA(sampler, optimizer, reps=1)

# Solve the problem
result = qaoa.compute_minimum_eigenvalue(qubo_pauli)

# Output the result
print("📉 Minimum eigenvalue:", result.eigenvalue)
print("🏆 Best bitstring:", result.best_measurement['bitstring'])
print("🎯 Probability:", result.best_measurement['probability'])
