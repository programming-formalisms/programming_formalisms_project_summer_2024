```mermaid

classDiagram
Visualisation <-- Bacteria : put on
 Visualisation <--> Simulation : run
 Visualisation <-- Nutrients : put on
 Bacteria --> Direction : has a
 Bacteria --> Position : has a
 Nutrients --> Position : has a
 Nutrients --> Concentration : has a

class Visualisation{
    Bacteria
    Nutrients
    init()
}
class Bacteria{
    - Position
    - Direction
    - init()
    - get_run()
    - get_tumble()
}
class Nutrients{
    - Position
    - Concentration
    - init()
}
class Position{
    - int x
    - int y
    - init()
}
class Direction{
    - Position pos1
    - Position pos2
    - str pos
    - init()
}
class Concentration{
    - int x
    - init ()
}
class Simulation{
    - Bacteria
    - Nutrients
    - tumble_init()
    - run()
    - stop()
}

```
