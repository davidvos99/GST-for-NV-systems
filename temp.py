import json
import pygsti
import gst_model_set

from pygsti.circuits import Circuit as C

gate_names_rev = ["I", "X", "Y", "x", "y"]
gate_translate_rev = {
    "null": "",
    "I": (("Gi", 0),),
    "X": (("Gxpi", 0),),
    "Y": (("Gypi", 0),),
    "x": (("Gxpi2", 0),),
    "y": (("Gypi2", 0),),

}
keys_rev = gate_names_rev

# load gate set
folder_name = 'temp'
gate_set_name = '1_qubit_3_gates_paper_germs_real'
gate_set_name_tot = folder_name + gate_set_name + '\\' + gate_set_name + '.json'

if gate_set_name == '1_qubit_3_gates_paper_germs':
    gate_translate = {
        "null": "",
        "I": "Gi",
        "X": "Gx_pi",
        "Y": "Gy_pi",
        "x": "Gx",
        "y": "Gy",

    }

'''''
with open(gate_set_name_tot, 'w') as f:
    gate_seq = json.load(f)

gate_seq_r = []
for i in range(len(gate_seq)):
    exp_len = len(gate_seq[i])
    exp_seq = []
    if exp_len >= 0:
        for j in range(exp_len):
            exp_seq.append(gate_translate_rev[gate_seq[i][j][0]])
    else:
        exp_seq.append(gate_translate[""])
    gate_seq_r.append(C(exp_seq))
'''

if gate_set_name == '1_qubit_3_gates':

    target_model_1qubit_3gates = pygsti.models.create_explicit_model_from_expressions(
        [('Q0',)], ['Gi', 'Gx', 'Gy'],
        ["I(Q0)", "X(pi/2,Q0)", "Y(pi/2,Q0)"])
    mdl = target_model_1qubit_3gates
    prep_fid = [C({}), C('Gx'), C('Gy'), C(['Gx', 'Gx'])]
    meas_fid = [C({}), C('Gx'), C('Gy')]
    germs = [C('Gi'), C('Gx'), C('Gy'), C(['Gi', 'Gi', 'Gi', 'Gi', 'Gi', 'Gx']), C(['Gx', 'Gy']),
             C(['Gi', 'Gi', 'Gi', 'Gi', 'Gx', 'Gy'])
        , C(['Gi', 'Gi', 'Gi', 'Gi', 'Gy', 'Gx']), C(['Gi', 'Gi', 'Gy', 'Gx', 'Gx', 'Gx'])
        , C(['Gx', 'Gx', 'Gy', 'Gy', 'Gx', 'Gy']), C(['Gi', 'Gi', 'Gx', 'Gx', 'Gx', 'Gy'])]

    maxLengths = [2 ** n for n in range(4 + 1)]
    listOfExperiments = pygsti.circuits.create_lsgst_circuits(
        target_model_1qubit_3gates, prep_fid, meas_fid, germs, maxLengths)

    gate_translate = {
        "": "null",
        "Gi": "I",
        "Gx_pi": "X",
        "Gy_pi": "Y",
        "Gx": "x",
        "Gy": "y",
    }

elif gate_set_name == '1_qubit_3_gates_paper_germs':

    target_model_1qubit_3gates = pygsti.models.create_explicit_model_from_expressions(
        [('Q0',)], ['Gi', 'Gx', 'Gy'],
        ["I(Q0)", "X(pi/2,Q0)", "Y(pi/2,Q0)"])
    mdl = target_model_1qubit_3gates
    prep_fid = [C({}), C('Gx'), C('Gy'), C(['Gx', 'Gx']), C(['Gx', 'Gx', 'Gx']), C(['Gy', 'Gy', 'Gy'])]
    meas_fid = [C({}), C('Gx'), C('Gy'), C(['Gx', 'Gx']), C(['Gx', 'Gx', 'Gx']), C(['Gy', 'Gy', 'Gy'])]
    germs = [C('Gi'), C('Gx'), C('Gy'), C(['Gi', 'Gi', 'Gi', 'Gi', 'Gi', 'Gx']), C(['Gx', 'Gy']),
             C(['Gi', 'Gi', 'Gi', 'Gi', 'Gx', 'Gy'])
        , C(['Gi', 'Gi', 'Gi', 'Gi', 'Gy', 'Gx']), C(['Gi', 'Gi', 'Gy', 'Gx', 'Gx', 'Gx'])
        , C(['Gx', 'Gx', 'Gy', 'Gy', 'Gx', 'Gy']), C(['Gi', 'Gi', 'Gx', 'Gx', 'Gx', 'Gy'])]

    maxLengths = [2 ** n for n in range(4 + 1)]
    listOfExperiments = pygsti.circuits.create_lsgst_circuits(
        target_model_1qubit_3gates, prep_fid, meas_fid, germs, maxLengths)

    gate_translate = {
        "": "null",
        "Gi": "I",
        "Gx_pi": "X",
        "Gy_pi": "Y",
        "Gx": "x",
        "Gy": "y",
    }



elif gate_set_name == '1_qubit_3_gates_paper_germs_real':

    target_model_1qubit_3gates = pygsti.models.create_explicit_model_from_expressions(
        [('Q0',)], ['Gi', 'Gx', 'Gy'],
        ["I(Q0)", "X(pi/2,Q0)", "Y(pi/2,Q0)"])
    mdl = target_model_1qubit_3gates
    prep_fid = [C({}), C('Gx'), C('Gy'), C(['Gx', 'Gx']), C(['Gx', 'Gx', 'Gx']), C(['Gy', 'Gy', 'Gy'])]
    meas_fid = [C({}), C('Gx'), C('Gy'), C(['Gx', 'Gx']), C(['Gx', 'Gx', 'Gx']), C(['Gy', 'Gy', 'Gy'])]
    germs = [C('Gi'), C('Gx'), C('Gy'), C(['Gi', 'Gi', 'Gi', 'Gi', 'Gi', 'Gx']), C(['Gx', 'Gy']),
             C(['Gi', 'Gi', 'Gi', 'Gi', 'Gx', 'Gy'])
        , C(['Gi', 'Gi', 'Gi', 'Gi', 'Gy', 'Gx']), C(['Gi', 'Gi', 'Gy', 'Gx', 'Gx', 'Gx'])
        , C(['Gx', 'Gx', 'Gy', 'Gy', 'Gx', 'Gy']), C(['Gi', 'Gi', 'Gx', 'Gx', 'Gx', 'Gy'])]

    maxLengths = [2 ** n for n in range(4 + 1)]
    listOfExperiments = pygsti.circuits.create_lsgst_circuits(
        target_model_1qubit_3gates, prep_fid, meas_fid, germs, maxLengths)

    gate_translate = {
        "": "null",
        "Gi": "I",
        "Gx_pi": "X",
        "Gy_pi": "Y",
        "Gx": "x",
        "Gy": "y",
    }


elif gate_set_name == '1_qubit_5_gates':

    target_model_1qubit_5gates = pygsti.models.create_explicit_model_from_expressions(
        [('Q0',)], ['Gi', 'Gx', 'Gy', 'Gx_pi', 'Gy_pi'],
        ["I(Q0)", "X(pi/2,Q0)", "Y(pi/2,Q0)", "X(pi,Q0)", "Y(pi,Q0)"])

    mdl = target_model_1qubit_5gates
    prep_fid = [C({}), C('Gx'), C('Gy'), C(['Gx_pi'])]
    meas_fid = [C({}), C('Gx'), C('Gy')]
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

    maxLengths = [2 ** n for n in range(4 + 1)]
    listOfExperiments = pygsti.circuits.create_lsgst_circuits(
        target_model_1qubit_5gates, prep_fid, meas_fid, germs, maxLengths)

    gate_translate = {
        "": "null",
        "Gi": "I",
        "Gx_pi": "X",
        "Gy_pi": "Y",
        "Gx": "x",
        "Gy": "y",
    }

elif gate_set_name == '1_qubit_5_gates_single_gate_germs':

    mdl = gst_model_set.target_model()
    germs, prep_fid, meas_fid = (
        gst_model_set.germs(),
        gst_model_set.prep_fiducials(),
        gst_model_set.meas_fiducials(),
    )

    maxLengths = [2 ** n for n in range(4 + 1)]
    listOfExperiments = pygsti.circuits.create_lsgst_circuits(
        mdl, prep_fid, meas_fid, germs, maxLengths)

    gate_translate = {
        "": "null",
        "Gi": "I",
        "Gxpi": "X",
        "Gypi": "Y",
        "Gxpi2": "x",
        "Gypi2": "y",
    }

print(len(listOfExperiments))