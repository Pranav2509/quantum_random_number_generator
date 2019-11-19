from qiskit import IBMQ
import qiskit
import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram

# Please get the API key from IBM Q Experience
IBMQ.save_account('<YOUR IBMQ Key Here>')

# Function to convert binary number to decimal number
def binaryToDecimal(binary1): 
    binary = int(binary1)
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print(decimal)    



# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(1, 1)
number = ''
for i in range(0, 15):
    # Add a H gate on qubit 0
    circuit.h(0)

    # Map the quantum measurement to the classical bits
    circuit.measure([0,], [0,])

    # Execute the circuit on the qasm simulator
    job = execute(circuit, simulator, shots=1000)

    # Grab results from the job
    result = job.result()

    # Returns counts
    counts = result.get_counts(circuit)

    if counts.get('1') > counts.get('0'):
        number+='1'
    else:
        number+='0'

binaryToDecimal(number)
