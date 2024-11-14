# Quantum Circuit Simulation: Tensor Multiplication

Tensors generalize vectors and matrices to any number of dimensions. Instead of
representing an $n$-qubit state as a vector of length $ 2^n $, it may be
more natural to write it as a rank-$n$ tensor with shape $(2, 2,
\ldots, 2)$. Transformations between these two representations are easily
achieved using `np.reshape` and `np.flatten`.

Using tensor multiplication (e.g., `np.tensordot` or `np.einsum`), you can apply
a 1- or 2-qubit gate to the quantum state tensor by multiplying along the
relevant qubit axes.

## Instructions
1. Define a quantum circuit consisting of 1- and 2-qubit matrix representations
   of the $X$, $H$, and CNOT gates.
2. Apply these gates sequentially to the quantum state tensor using tensor
   multiplication.
3. Plot the runtime of your code as a function of the number of qubits $n$.

## Questions
1. How does the maximum number of qubits you can simulate using this method?
