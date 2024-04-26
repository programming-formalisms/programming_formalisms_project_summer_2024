"""The Programming Formalisms Summer 2024 Project.

Project used in the UPPMAX Programming Formalisms Summer 2024 course.
"""

import cProfile
import sys

from bacsim.simulation import (
  run_experiment,
)

def run_here():
    run_experiment("parameter_filename.txt", "results_filename.csv")

def do_benchmark():
    """Benchmark this project."""
    cProfile.run("run_here()")

if __name__ == "__main__":

    if "--benchmark" in sys.argv:
        print("Benchmarking application") # noqa: T201 print is used as a stub
        if __debug__:
            e = RuntimeError("Do not benchmark in debug mode")
            raise e
        do_benchmark()
    else:
        print("Running workflow") # noqa: T201 print is used as a stub
        run_here()
