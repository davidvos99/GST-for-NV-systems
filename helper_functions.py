import pygsti
import numpy as np
import json
from pygsti.circuits import Circuit


def get_data(count_0_file_name, count_1_file_name, gate_list_file_name):
    count_0_arr = np.load(count_0_file_name)
    count_1_arr = np.load(count_1_file_name)
    gate_set_name = gate_list_file_name
    #code to delete first entry in array to fix twice identity gate mistake
    #count_0_arr = np.delete(count_0_arr, 0)
    #count_1_arr = np.delete(count_1_arr, 0)
    #np.save(count_0_file_name, count_0_arr)
    #np.save(count_1_file_name, count_1_arr)
    print(len(count_0_arr))
    print(len(count_1_arr))
    ds1 = pygsti.data.DataSet(outcome_labels=['0', '1'])
    # load gate set
    gate_translate_rev = {
        "": (("", 0),),
        "I": (("Gi", 0),),
        "X": (("Gxpi", 0),),
        "Y": (("Gypi", 0),),
        "x": (("Gxpi2", 0),),
        "y": (("Gypi2", 0),),
        "null": (("Gi", 0),),
        "ex": (("Gxpi2", 0),),
        "ey": (("Gypi2", 0),),
        "eI": (("Gi", 0),)
    }
    with open(gate_set_name, 'r') as f:
        gate_seq_r = json.load(f)

    gate_seq = []
    print(len(gate_seq_r))

    for i in range(len(gate_seq_r)):
        exp_len = len(gate_seq_r[i])
        exp_seq = []
        if exp_len >= 0:
            for j in range(exp_len):
                exp_seq.append(gate_translate_rev[gate_seq_r[i][j]])
        else:
            exp_seq.append([" "])
        gate_seq.append(Circuit(exp_seq))
    for i in range(len(gate_seq)):
        ds1.add_count_dict(
            gate_seq[i],
            {"0": round(abs(count_0_arr[i])), "1": round(abs(count_1_arr[i]))},
        )

    ds1.done_adding_data()
    return ds1
