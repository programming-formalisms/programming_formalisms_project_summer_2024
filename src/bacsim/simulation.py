"""Simulation class and associated functions."""

def create_parameters():
    """"Create a default/testing parameter set."""
    return []

def read_parameters_from_file(filename):
    """"Create a parameter set from file."""
    return filename

def create_experiment(parameters = []):
    """"Create an experiment class with its parameters."""
    return parameters

def run(experiment):
    """"Run an experiment and get the results."""
    return experiment

def run_experiment(parameters_filename, results_filename):
    """"Run an experiment for a parameters file and save the results to file."""
    # Untested, to show that Codecov works fine :-)
    print("Reading file: ", parameters_filename) # noqa: T201
    print("Running simulation...") # noqa: T201
    print("Saving results to: ", results_filename) # noqa: T201

def save(results, filename):
    """"Save the experimental results to file."""
    return (results, filename)
