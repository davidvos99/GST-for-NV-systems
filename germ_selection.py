import pygsti
import pygsti.algorithms.fiducialselection as fidsel
import pygsti.algorithms.germselection as germsel
from pygsti.circuits import Circuit as C

target_model_1qubit_3gates = pygsti.models.create_explicit_model_from_expressions(
    [('Q0',)], ['Gi', 'Gx', 'Gy'],
    ["I(Q0)", "X(pi/2,Q0)", "Y(pi/2,Q0)"])

target_model_1qubit_5gates = pygsti.models.create_explicit_model_from_expressions(
    [('Q0',)], ['Gi', 'Gx', 'Gy', 'Gx_pi', 'Gy_pi'],
    ["I(Q0)", "X(pi/2,Q0)", "Y(pi/2,Q0)", "X(pi,Q0)", "Y(pi,Q0)"])

#global variables
use_own_fiducials_and_germs = True
target_model = target_model_1qubit_3gates

# create fiducials and germs with set found in paper
if (use_own_fiducials_and_germs):
    prepFiducials = [C({}), C('Gx'), C('Gy'), C(['Gx', 'Gx']), C(['Gx', 'Gx', 'Gx']), C(['Gy', 'Gy', 'Gy'])]
    measFiducials = [C({}), C('Gx'), C('Gy'), C(['Gx', 'Gx']), C(['Gx', 'Gx', 'Gx']), C(['Gy', 'Gy', 'Gy'])]
    germs = [C('Gi'), C('Gx'), C('Gy'), C(['Gx', 'Gy']), C(['Gx', 'Gy', 'Gi']), C(['Gx', 'Gi', 'Gy'])
        , C(['Gx', 'Gi', 'Gi']), C(['Gy', 'Gi', 'Gi']), C(['Gx', 'Gx', 'Gi', 'Gy']), C(['Gx', 'Gy', 'Gy', 'Gi']),
             C(['Gx', 'Gx', 'Gy', 'Gx', 'Gy', 'Gy'])]
else:
    prepFiducials, measFiducials = fidsel.find_fiducials(target_model, max_fid_length=4)
    germs = germsel.find_germs(target_model)

print(prepFiducials)
print(measFiducials)
maxLengths = [2 ** n for n in range(4 + 1)]
listOfExperiments = pygsti.circuits.create_lsgst_circuits(
    target_model, prepFiducials, measFiducials, germs, maxLengths)
header = "1 qubit 5 gates. " + "Circuit depth: " + str(maxLengths)
print(len(listOfExperiments))

#pygsti.io.write_circuit_list("circuit_lists/1_qubit_5_gates.txt", listOfExperiments, header)

'''
FOR FUTURE WORK (GET HYPED :) )
target_model_2qubit_4gates = pygsti.models.create_explicit_model_from_expressions(
    (0, 1),
    ['Gi',
     ('Gx ', 0), ('Gy ', 0),
     ('Gx ', 1), ('Gy ', 1),
     ('Gcnot ', 0, 1)],
    ["I(0,1)",
     "X(pi/2,0)", "Y(pi/2,0)",
     "X(pi/2,1)", "Y(pi/2,1)",
     "CNOT(0,1)"])

target_model_2qubit_10gates = pygsti.models.create_explicit_model_from_expressions(
    (0, 1),
    ['Gi',
     ('Gx ', 0), ('Gy ', 0), ('Gx_pi ', 0), ('Gy_pi ', 0),
     ('Gx ', 1), ('Gy ', 1), ('Gx_pi ', 1), ('Gy_pi ', 1),
     ('Gcnot', 0, 1)],
    ["I(0,1)",
     "X(pi/2,0)", "Y(pi/2,0)", "X(pi, 0)", "Y(pi, 0)",
     "X(pi/2,1)", "Y(pi/2,1)", "X(pi, 1)", "Y(pi, 1)",
     "CNOT(0,1)"])
'''
