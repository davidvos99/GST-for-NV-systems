
import helper_functions as helper
import model_zoya as model
import pygsti

if __name__ == '__main__':
    target_model = model.target_model()
    file_path_0_count = "zoya/with_echo_Gi_correct/sim_init0_with_echo_Gi_correct_Ninit_fidelity_0.95_no_XY4__ssro_resultscount_0_arr.npy"
    file_path_1_count = "zoya/with_echo_Gi_correct/sim_init0_with_echo_Gi_correct_Ninit_fidelity_0.95_no_XY4__ssro_resultscount_1_arr.npy"
    file_path_circuit_json = "zoya/with_echo_Gi_correct/with_echo_Gi_correct.JSON"

    # Step 1: create an "experiment design" for doing GST on the std1Q_XYI gate set
    exp_design = model.create_gst_experiment_design(max_max_length=64)

    # TODO: get correct dataset without writing and reading like an idiot
    ds1 = helper.get_data(file_path_0_count, file_path_1_count, file_path_circuit_json)

    pygsti.protocols.ProtocolData(exp_design, ds1).write("temp/dataset")
    ds2 = pygsti.io.read_data_from_dir("temp/dataset")

    proto = pygsti.protocols.StandardGST('full TP,CPTP')
    #proto = pygsti.protocols.GateSetTomography(target_model)
    results = proto.run(ds2)

    results.write("zoya/temp_res")

    #report
    report = pygsti.report.construct_standard_report(
        results, title="fid = 0.95", verbosity=2)
    report.write_html("zoya/fid=0.95", verbosity=2)

