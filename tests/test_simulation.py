"""Tests all function in src.bacsim.richel_utils."""

import unittest

from src.bacsim.simulation import (
    create_experiment,
    create_parameters,
    read_parameters_from_file,
    run,
    save,
)


class TestExperiment(unittest.TestCase):

    """Class to test the code in src.bacsim.particle."""

    def test_create_experiment(self):
        """"Create a default experiment."""
        create_experiment()
    def test_run(self):
        """"Run a default experiment."""
        experiment = create_experiment()
        # Should pass without error
        run(experiment)
    def test_run_creates_a_result(self):
        """"Get results from a run."""
        experiment = create_experiment()
        # Should pass without error
        results = run(experiment) # noqa: F841
    def test_save(self):
        """"Save results from a run."""
        experiment = create_experiment()
        results = run(experiment)
        # Should pass without error
        save(results, "my_results.csv")
    def test_create_an_experiment_with_parameters(self):
        """"An experiment has parameters."""
        parameters = create_parameters()
        experiment = create_experiment(parameters) # noqa: F841
    def test_read_parameters_from_file(self):
        """"Parameters can be read from file."""
        # Should pass without errors
        read_parameters_from_file("parameters.txt")
