parameters = read_parameters_from_file("parameters_protein.txt")
protein = create_protein(parameters)
results = run(protein)
save(results, "protein.csv")