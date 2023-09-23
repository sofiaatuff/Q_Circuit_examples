from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram
from math import sqrt

# Define the states u and v (for demonstration, we'll use 1-qubit states)
# For |u> = |0> and |v> = |0>
u = [1, 0]
v = [1, 0]

# Initialize quantum circuit
n = 1  # Number of qubits in u and v
qc = QuantumCircuit(n * 2 + 1, 1)

# Initialize states u and v
qc.initialize(u, 1)
qc.initialize(v, 2)

# Apply Hadamard gate on ancillary qubit (qubit 0)
qc.h(0)

# Apply controlled-SWAP
qc.cswap(0, 1, 2)

# Apply Hadamard on ancillary qubit again
qc.h(0)

# Measure the ancillary qubit
qc.measure(0, 0)

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()

# Get measurement results and calculate probability of measuring '0'
counts = result.get_counts()
prob_0 = counts.get('0', 0) / sum(counts.values())

# Calculate <u|v> from the probability of measuring '0'
inner_product_squared = 2 * prob_0 - 1

# Display results
print(f"Counts: {counts}")
print(f"P(0): {prob_0}")
print(f"|<u|v>|^2: {inner_product_squared}")

# Plot the measurement results
plot_histogram(counts).show()
