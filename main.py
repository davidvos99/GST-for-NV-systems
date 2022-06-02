
import helper_functions as helper
import model_1_qubit_3_gates_paper_germs as model
import pygsti

if __name__ == '__main__':
    target_model = model.target_model("CPTP")
    file_path_0_count = "datasets/1_qubit_3_gates_paper_germs/experimental data/1_qubit_3_gates_paper_germ_with_XY4_init_0/ssro_resultscount_0_arr.npy"
    file_path_1_count = "datasets/1_qubit_3_gates_paper_germs/experimental data/1_qubit_3_gates_paper_germ_with_XY4_init_0/ssro_resultscount_1_arr.npy"
    file_path_circuit_json = "GS"

    # Step 1: create an "experiment design" for doing GST on the std1Q_XYI gate set
    exp_design = model.create_gst_experiment_design(max_max_length=16)

    # TODO: get correct dataset without writing and reading like an idiot
    ds1 = helper.get_data(file_path_0_count, file_path_1_count, file_path_circuit_json)

 #   pygsti.protocols.ProtocolData(exp_design, ds1).write("temp/dataset")
  #  ds2 = pygsti.io.read_data_from_dir("temp/dataset")

    #proto = pygsti.protocols.StandardGST('CPTP')
  #  proto = pygsti.protocols.GateSetTomography(target_model)
   # results = proto.run(ds2)

 #   results.write("results/sim_3_gates_paper_germs/exp/echo/init_state=1")

    #report
#    report = pygsti.report.construct_standard_report(
 #       results, title="GST experimental data, 3 gates, paper germs, init state=1, echo", verbosity=2)
 #   report.write_html("reports/sim_3_gates_paper_germs_real/exp/echo/init_state=0", verbosity=2)
