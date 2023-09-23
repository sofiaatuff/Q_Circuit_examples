import numpy as np
import itertools

# 1. Lets start by defining the constants and native gates
omega = np.exp(2j * np.pi / 10)
tau = (1 + np.sqrt(5)) / 2

M1 = np.array([[omega**(-4), 0], [0, omega**3]])
M1_inv = np.linalg.inv(M1)

M2 = (1 / np.sqrt(tau)) * np.array([[1, 1], [1, -1]])
M2 = M2 @ M1 @ M2.T.conj()
M2_inv = np.linalg.inv(M2)


# 2. The goal matrix ignoring the diagonal terms
goal = np.array([[0, 1], [1, 0]])

# 3. Initializing the state
best_score = 0
best_sequence = []

gates = [M1, M1_inv, M2, M2_inv]
gate_names = ['M1', 'M1_inv', 'M2', 'M2_inv']

# 4. Lets create a fn for evaluating how close a given matrix is to the goal matrix
def evaluate(matrix, goal):
    return np.abs(matrix[0, 1]) + np.abs(matrix[1, 0])

# 5. And a fn to get the gate name from a gate matrix
def get_gate_name(gate_matrix, gates, gate_names):
    for i, ref_gate in enumerate(gates):
        if np.array_equal(gate_matrix, ref_gate):
            return gate_names[i]
    return "Unknown"

# 6. Lets loopty loop over sequences of gates up to length 8
for n in range(1, 9):
    for sequence in itertools.product(gates, repeat=n):
        result = np.eye(2)
        for gate in sequence:
            result = gate @ result
        
        score = evaluate(result, goal)
        
        if score > best_score:
            best_score = score
            best_sequence = [get_gate_name(gate, gates, gate_names) for gate in sequence]
            print("New best sequence:", best_sequence)
            print("New best score:", best_score)



# **Extra credit**: Can you find a method for getting arbitrarily close to the goal? => Fidelity?

# 1. We need a target gate
target = np.array([[0, 1], [1, 0]])

# 2. Lets initialize
best_fidelity = 0
best_sequence = []

# 3. Create the available gates
gates = [M1, np.linalg.inv(M1), M2, np.linalg.inv(M2)]

# 4. Then we can calculate the fidelity of the approximation and iterate through the sequences
def fidelity(approx, target):
    return np.abs(np.trace(np.dot(approx.conj().T, target))) / 2

for n in range(1, 9): 
    for sequence in itertools.product(gates, repeat=n):
        result = np.eye(2)
        for gate in sequence:
            result = np.dot(gate, result)

        current_fidelity = fidelity(result, target)
        
        if current_fidelity > best_fidelity:
            best_fidelity = current_fidelity
            best_sequence = sequence
            print(f"New best sequence of length {n} with fidelity {best_fidelity}")
            
        if np.isclose(best_fidelity, 1, atol=1e-9):  
            break

    if np.isclose(best_fidelity, 1, atol=1e-9):
        break

print("Best sequence:")
print(best_sequence)
print("Best fidelity:")
print(best_fidelity)

