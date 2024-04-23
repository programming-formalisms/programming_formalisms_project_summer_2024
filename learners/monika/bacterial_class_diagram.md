```

classDiagram
class Surface{
    + tuple coor
}

class Bacteria{
    - tuple coor
    - int init_dir
    - string state
    + set_state()
    + get_state()
    + Nutrients.get_nutrients(x,y)
    + move(state = tumble/run)
    + eat(int how much)
}

class Nutrients{
    - tuple coor
    - tuple nutrients
    - get_nutrients()
    - set_nutrients(type,conc)
}


class Simulation{
    set_surface()
    set_init_state()
    run()
}

class Visualization{
    - null
}

Simulation --> Visualization
Simulation --> Surface
Surface --> Nutrients
Surface "1..n" *-- Bacteria

```
