import pygsti
from pygsti.circuits import Circuit as C
import time

target_model_1qubit_3gates = pygsti.models.create_explicit_model_from_expressions(
    [('Q0',)], ['Gi', 'Gx', 'Gy'],
    ["I(Q0)", "X(pi/2,Q0)", "Y(pi/2,Q0)"])

target_model_1qubit_5gates = pygsti.models.create_explicit_model_from_expressions(
    [('Q0',)], ['Gi', 'Gx', 'Gy', 'Gx_pi', 'Gy_pi'],
    ["I(Q0)", "X(pi/2,Q0)", "Y(pi/2,Q0)", "X(pi,Q0)", "Y(pi,Q0)"])

f = open("circuit_lists/temp", 'w')

gate_translate = {
    "Gi": "I",
    "Gx": 'x',
    "Gy": 'y',
    "Gx_pi": 'X',
    "Gy_pi": 'Y'
}


prepfid = [C('Gi'), C('Gx'), C('Gy'), C(['Gx', 'Gx']), C(['Gx', 'Gx', 'Gx']), C(['Gy', 'Gy', 'Gy'])]
mesfid = [C('Gi'), C('Gx'), C('Gy'), C(['Gx', 'Gx']), C(['Gx', 'Gx', 'Gx']), C(['Gy', 'Gy', 'Gy'])]
germs = [C('Gi'), C('Gx'), C('Gy'), C('Gx_pi'), C('Gy_pi')]

maxLengths = [2 ** n for n in range(4 + 1)]
listOfExperiments = pygsti.circuits.create_lsgst_circuits(
    target_model_1qubit_5gates, prepfid, mesfid, germs, maxLengths)

f.write("[ \n")
circuit_count = 0
for circuit in listOfExperiments:
    f.write("  [ \n")
    gate_count = 0
    for gate in circuit:
        if gate_count == (len(circuit) - 1):
            f.write("    \"" + gate_translate[gate] + "\" \n")
        else:
            f.write("    \"" + gate_translate[gate] + "\", \n")
        gate_count += 1
    circuit_count += 1
    if circuit_count == len(listOfExperiments):
        f.write("  ] \n")
    else:
        f.write("  ], \n")

f.write("]")
f.close()

'''
For 3 gate model:
prepfid = [C({}), C('Gx'), C('Gy'), C(['Gx', 'Gx'])]
mesfid = [C({}), C('Gx'), C('Gy')]
germs = [C('Gi'), C('Gx'), C('Gy'), C(['Gi', 'Gi', 'Gi', 'Gi', 'Gi', 'Gx']), C(['Gx', 'Gy']), C(['Gi', 'Gi', 'Gi', 'Gi', 'Gx', 'Gy'])
        , C(['Gi', 'Gi', 'Gi', 'Gi', 'Gy', 'Gx']) , C(['Gi', 'Gi', 'Gy', 'Gx', 'Gx', 'Gx'])
        , C(['Gx', 'Gx', 'Gy', 'Gy', 'Gx', 'Gy']), C(['Gi', 'Gi', 'Gx', 'Gx', 'Gx', 'Gy'])]   
        
        
        
For 5 gate model:
prepfid = [C({}), C('Gx'), C('Gy'), C(['Gx_pi'])]
mesfid = [C({}), C('Gx'), C('Gy')]
germs = [C('Gi'), C('Gx'), C('Gy'), C('Gx_pi'), C('Gy_pi'), C(['Gx_pi', 'Gy_pi']),
         C(['Gi', 'Gi', 'Gi', 'Gi', 'Gy_pi', 'Gx']),
         C(['Gx', 'Gy']), C(['Gx', 'Gy', 'Gy_pi']),
         C(['Gx', 'Gx_pi', 'Gy_pi']),
         C(['Gy', 'Gy', 'Gx_pi', 'Gy', 'Gy_pi']),
         C(['Gi', 'Gi', 'Gi', 'Gi', 'Gi', 'Gx']),
         C(['Gi', 'Gi', 'Gx_pi', 'Gx', 'Gy_pi', 'Gx_pi']),
         C(['Gy', 'Gx_pi', 'Gy_pi']),
         C(['Gx', 'Gx', 'Gy', 'Gx_pi', 'Gx', 'Gx_pi']),
         C(['Gi', 'Gi', 'Gi', 'Gi', 'Gy', 'Gx_pi']),
         C(['Gx', 'Gx', 'Gy_pi', 'Gy', 'Gx', 'Gy_pi']),
         C(['Gx', 'Gx_pi', 'Gy_pi', 'Gx_pi', 'Gy']),
         C(['Gx', 'Gx_pi', 'Gx_pi', 'Gx', 'Gy_pi']),
         C(['Gi', 'Gi', 'Gi', 'Gx_pi', 'Gx', 'Gy'])]
'''
