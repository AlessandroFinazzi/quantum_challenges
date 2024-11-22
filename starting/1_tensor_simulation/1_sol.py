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
                 [0, 0, 1, 0]]).reshape(2, 2, 2, 2) # reshaped for tensor operations
                 
def n_qbit(n):
    """
    Create an n-qubit state initialized to |0>^n.
    """
    reg = zero
    for _ in range(n - 1):
        reg = np.tensordot(reg, zero, 0)
    return reg
    
def h(state, index):
    """
    Apply the Hadamard gate to a specific qubit using tensordot.
    """
    new_state = np.tensordot(H, state, (1, index))
    return np.moveaxis(new_state, 0, index)

def x(state, index):
    """
    Apply the Pauli-X gate to a specific qubit using tensordot.
    """
    new_state = np.tensordot(X, state, (1, index))
    return np.moveaxis(new_state, 0, index)

def cnot(state, control, target):
    """
    Apply the CNOT gate to a specific pair of qubits using tensordot.
    """
    new_state = np.tensordot(CNOT, state, ((2, 3), (control, target)))
    return np.moveaxis(new_state, (0, 1), (control, target))


n_values = list(range(2, 27)) # Test for 2 to 26 qubits
                              # Using tensordot, it can run with double n-qbit state in comparable time, manteining same memory and same quantum circuit
runtimes = [] # List to store the runtimes for each n
results = [] # List to store the result states for each n

for n in n_values:
    start_time = time.time()

    state = n_qbit(n)
    state = x(state, n - 1)   # apply X
    state = h(state, 0)       # apply H
    state = cnot(state, 0, 1) # apply CNOT
    results.append(state.flatten()) # Flatten to obtain a vector

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

