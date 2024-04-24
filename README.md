# programming_formalisms_project_summer_2024

![](programming_formalisms_student_team_summer_2024_logo_50.png)

The Programming Formalisms project of summer 2024.

## Goal

To simulate bacterial movement in 2D space.

One way to model bacterial movement is 
the run and tumble model,
where 'run' is going straight in a direction,
and 'tumble' is picking a random direction.
The 'run' lasts longer when a bacterium
finds more and more nutrients (e.g. dissolved
sugars), and lasts shorter
when finding less and less nutrients.

![](run_and_tumble.jpg)

> Image from [coursehero](https://www.coursehero.com/study-guides/microbiology/unique-characteristics-of-prokaryotic-cells/)

## Internal links

 * [design](design/README.md): design documents
 * [learners](learners/README.md): place to keep notes and do exercises on an individual basis

## Files used for continuous integration scripts

Filename                           |Descriptions
-----------------------------------|------------------------------------------------------------------------------------------------------
[mlc_config.json](mlc_config.json) |Configuration of the link checker
[.spellcheck.yml](.spellcheck.yml) |Configuration of the spell checker, use `pyspelling -c .spellcheck.yml` to do spellcheck locally
[.wordlist.txt](.wordlist.txt)     |Whitelisted words for the spell checker, use `pyspelling -c .spellcheck.yml` to do spellcheck locally
[.pylintrc](.pylintrc)             |Configuration file for pylint
[pyproject.toml](pyproject.toml)   |Configuration file of this package

## External links

 * [Programming Formalisms GitHub repository](https://github.com/UPPMAX/programming_formalisms)

## References

 * [Wang et al., 2011] Wang, Charles CN, et al. "Simulation of bacterial chemotaxis by the random run and tumble model." 2011 IEEE 11th International Conference on Bioinformatics and Bioengineering. IEEE, 2011.

Richel is on main!

