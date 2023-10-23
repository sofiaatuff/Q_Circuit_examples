import qiskit
from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_bloch_multivector

# Initialize a quantum circuit
qc = QuantumCircuit(1)

# H gate
qc.h(0)
state_h = Aer.get_backend('statevector_simulator').run(transpile(qc, Aer.get_backend('statevector_simulator'))).result().get_statevector()
plot_h = plot_bloch_multivector(state_h, title="H Gate")

# S gate
qc.s(0)
state_s = Aer.get_backend('statevector_simulator').run(transpile(qc, Aer.get_backend('statevector_simulator'))).result().get_statevector()
plot_s = plot_bloch_multivector(state_s, title="S Gate")

# T gate
qc.t(0)
state_t = Aer.get_backend('statevector_simulator').run(transpile(qc, Aer.get_backend('statevector_simulator'))).result().get_statevector()
plot_t = plot_bloch_multivector(state_t, title="T Gate")

# Display the plots
plot_h.show()
plot_s.show()
plot_t.show()
