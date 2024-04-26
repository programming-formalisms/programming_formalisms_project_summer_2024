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
        # Should pass without error
        create_experiment()
    def test_run(self):
        experiment = create_experiment()
        # Should pass without error
        run(experiment)
    def test_run_creates_a_result(self):
        experiment = create_experiment()
        # Should pass without error
        results = run(experiment)
    def test_save(self):
        experiment = create_experiment()
        results = run(experiment)
        # Should pass without error
        save(results, "my_results.csv")
    def test_create_an_experiment_with_parameters(self):
        parameters = create_parameters()
        experiment = create_experiment(parameters)
    def test_read_parameters_from_file(self):
        # Should pass without errors
        read_parameters_from_file("parameters.txt")
