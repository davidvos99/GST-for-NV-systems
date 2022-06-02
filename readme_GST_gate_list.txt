=======================================================

Information on the gate set we used
Gate set is in GST_gate_list.json file
gst_model_set.py needed.

======================================================
    import gst_model_set
    target_model = gst_model_set.target_model()

    _germs = [
        (("Gi", 0),),
        (("Gxpi2", 0),),
        (("Gypi2", 0),),
        (("Gxpi", 0),),
        (("Gxpi", 0),),
    ]


    _fiducials = [
        (("Gi", 0),),
        (("Gxpi2", 0),),
        (("Gypi2", 0),),
        (("Gxpi2", 0), ("Gxpi2", 0)),
        (("Gxpi2", 0), ("Gxpi2", 0), ("Gxpi2", 0)),
        (("Gypi2", 0), ("Gypi2", 0), ("Gypi2", 0)),
    ]


     maxLengths = [1, 2, 4, 8, 16]

==============================================================================================

Code to interpret this list so that pygsti can understand. 
Read "GST_gate_list.json" and output gate_seq, which is the list that pygsti can use directly.(Circuit format)

==============================================================================================

import pygsti
import json
from pygsti.circuits import Circuit

gate_names_rev = ["I", "X", "Y", "x", "y"]
gate_translate_rev = {
    "null": "",
    "I": (("Gi", 0),),
    "X": (("Gxpi2", 0),),
    "Y": (("Gypi",0),),
    "x": (("Gxpi2",0),),
    "y": (("Gypi2",0),),
    
}
keys_rev = gate_names_rev

# load gate set

gate_set_name = 'GST_gate_list.json'
with open(gate_set_name,'r') as f:
    gate_seq_r = json.load(f)
 

gate_seq = []
for i in range(len(gate_seq_r)):
    exp_len = len(gate_seq_r[i])
    exp_seq = []
    if exp_len > 0:
        for j in range(exp_len):
            exp_seq.append(gate_translate_rev[gate_seq_r[i][j][0]])
    else:
        exp_seq.append(gate_translate[""])
    gate_seq.append(Circuit(exp_seq))



=================================================================

To actually feed experimental data to pygsti, you have to combine the gate list of 
"GST_gate_list.json" and the measured data of "ssro_resultscount_0_arr.npy"
using the following code.

===============================================================


    count_0_arr = np.load('ssro_resultscount_0_arr.npy')
    count_1_arr = np.load('ssro_resultscount_1_arr.npy')

    for i in range(len(gate_seq)):

        ds1.add_count_dict(
            gate_seq[i],
            {"0": round(abs(count_0_arr[i])), "1": round(abs(count_1_arr[i]))},
            
            
        )


=================================================================

