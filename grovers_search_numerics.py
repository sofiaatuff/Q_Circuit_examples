from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def grover_oracle(n=2):
    """ Oracle for marking the |00⟩ state """
    qc = QuantumCircuit(n)
    qc.cz(0, 1)  # This will flip the sign of the state |00⟩
    return qc

def grover_diffusion(n=2):
    """ Grover diffusion operator for n=2 qubits """
    qc = QuantumCircuit(n)
    qc.h(range(n))
    qc.x(range(n))
    qc.h(1)
    qc.cx(0, 1)
    qc.h(1)
    qc.x(range(n))
    qc.h(range(n))
    return qc

# Create Grover circuit
n = 2
grover_circuit = QuantumCircuit(n, n)

# Initialize state to |s⟩
grover_circuit.h(range(n))

# Apply Grover iteration
grover_circuit = grover_circuit.compose(grover_oracle(n))
grover_circuit = grover_circuit.compose(grover_diffusion(n))

# Measurement
grover_circuit.measure(range(n), range(n))

# Simulate and plot results
backend = Aer.get_backend('qasm_simulator')
result = execute(grover_circuit, backend, shots=1000).result()
counts = result.get_counts()
plot_histogram(counts)
