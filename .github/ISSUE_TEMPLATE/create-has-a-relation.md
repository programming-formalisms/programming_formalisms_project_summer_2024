---
name: Create a has-a relation
about: Need to create a has-a relation
title: 'A [name_of_class] has a [name_of_subclass]'
labels: ''
assignees: ''

---

In [the class design document](https://github.com/programming-formalisms/programming_formalisms_example_project/blob/main/design/class_diagram_richel.puml), 
the classes in the title
have a has-a relation. Create it!

# Procedure

 * [ ] Add the smaller class to the bigger class
   in the implementation, for example:

```python
# ...

from src.pf_example.speed import (
    Speed,
)

class Particle:
   # ...

   def __init__(self):
       self._speed = Speed()

   # ...
```

 * [ ] Create a minimal class test,
   for example:

```python
# ...

class TestParticle(unittest.TestCase):

    # ...

    def test_a_particle_has_a_speed(self):
        """#[number]: a Particle has a Speed."""
        p = Particle()
        p._speed # noqa: B018, SLF001
```

The test is that it works, not that it does anything useful.

The `# noqa: B018, SLF001` allows one to temporarily
do (1) create an unused variable, and (2) read a private member variable.
This test can be removed later, when other tests
supersede this one.

Use [the workflow that fits you best](https://github.com/programming-formalisms/programming_formalisms_example_project/tree/main/workflow#github-workflows), 
ideally use a topic branch for this issue 
and merge to develop using a PR with code review.
