# Dream code for Model class

parameters = read_parameters(filename)
model = Model(parameters)
results = run(model)
save(results, output_file)
plot(results)