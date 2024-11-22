import numpy as np
import time
import matplotlib.pyplot as plt

zero = np.array([1, 0]) # |0> state
one = np.array([0, 1])  # |1> state

X = np.array([[0, 1],
              [1, 0]])

H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])

CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])
                 
def n_qbit(n):
    """
    Create an n-qubit state initialized to |0>^n.
    """
    reg = zero
    for _ in range(n - 1):
        reg = np.kron(reg, zero)
    return reg

def h(n, state, index):
    """
    Apply the Hadamard gate to a specific qubit.
    """
    assert index < n, "Index out of range"
    I = np.eye(2, dtype=int)
    gates = [I] * n
    gates[index] = H
    gate = gates[0]
    for i in range(1, n):
        gate = np.kron(gate, gates[i])
    return np.dot(gate, state)

def x(n, state, index):
    """
    Apply the Pauli-X gate to a specific qubit.
    """
    assert index < n, "Index out of range"
    I = np.eye(2, dtype=int)
    gates = [I] * n
    gates[index] = X
    gate = gates[0]
    for i in range(1, n):
        gate = np.kron(gate, gates[i])
    return np.dot(gate, state)

def cnot(n, state, index):
    """
    Apply the CNOT gate to a specific pair of qubits. (index as control, index+1 as target)
    """
    assert index < n-1, "Index out of range"
    I = np.eye(2, dtype=int)
    gates = [I] * (n-1)
    gates[index] = CNOT
    gate = gates[0]
    for i in range(1, n-1):
        gate = np.kron(gate, gates[i])
    return np.dot(gate, state)


n_values = list(range(2, 14)) # Test for 2 to 13 qubits
runtimes = [] # List to store the runtimes for each n
results = []  # List to store the final state for each n

for n in n_values:
    start_time = time.time()

    state = n_qbit(n)
    state = x(n, state, n - 1)  # apply X
    state = h(n, state, 0)      # apply H
    state = cnot(n, state, 0)   # apply CNOT
    results.append(state)

    end_time = time.time()
    runtimes.append(end_time - start_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, runtimes, marker='o', label="Simulation Runtime")
plt.xlabel("Number of Qubits (n)")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime of Quantum Circuit Simulation vs Number of Qubits")
plt.grid(True)
plt.legend()
plt.show()


def sample_state(state_vector, num_samples=1):
    """
    Sample states from a quantum state vector based on their probabilities.
    """
    probabilities = np.abs(state_vector) ** 2
    states = np.arange(len(state_vector))
    return np.random.choice(states, size=num_samples, p=probabilities)

def expectation_value(state_vector, operator):
    """
    Calculate the expectation value of a given operator in a quantum state.
    """
    bra = np.conj(state_vector)
    ket = np.dot(operator, state_vector)
    return np.dot(bra, ket)

