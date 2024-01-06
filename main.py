'''
This program is to run a basic Quantum Program 
The four steps to writing a quantum program are

Step 1 -> Map the problem to a quantum-native format
Step 2 -> Optimize the circuits and operators
Step 3 -> Execute using a quantum primitive function
Step 4 -> Analyze the results

Author - Aniket Mishra
'''

from qiskit import QuantumCircuit
from qiskit.quantum_info import Pauli

# two qubits
qc = QuantumCircuit(2)

# Hadamard gate to qubit 0
qc.h(0)

# Controlled-X gate on qubit 1, controlled by qubit 0
qc.cx(0,1)
 
ZZ = Pauli('ZZ')
ZI = Pauli('ZI')
IZ = Pauli('IZ')
XX = Pauli('XX')
XI = Pauli('XI')
IX = Pauli('IX')

print(qc.draw())