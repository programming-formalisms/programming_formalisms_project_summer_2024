"""The Programming Formalisms Summer 2024 Project.

Project used in the UPPMAX Programming Formalisms Summer 2024 course.
"""

import cProfile
import sys

from bacsim.simulation import (
  create_experiment,
  create_parameters,
  read_parameters_from_file,
  run,
  save,
)

def do_workflow():
    parameters = read_parameters_from_file("parameters.txt")
    experiment = create_experiment(parameters)
    results = run(experiment)
    save(results, "results.csv")

def do_benchmark():
    """Benchmark this project."""
    cProfile.run("do_workflow()")

if __name__ == "__main__":

    if "--benchmark" in sys.argv:
        print("Benchmarking application") # noqa: T201 print is used as a stub
        if __debug__:
            e = RuntimeError("Do not benchmark in debug mode")
            raise e
        do_benchmark()
    else:
        print("Running workflow") # noqa: T201 print is used as a stub
        do_workflow()


