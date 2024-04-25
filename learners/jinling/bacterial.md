parameters = read_parameters_from_file("parameters.txt")
experiment = create_experiment(parameters)
results = run(experiment)
save(results, "my_results.csv")
