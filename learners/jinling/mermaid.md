classDiagram
    VisualObj <|-- Bacterial
    VisualObj <|-- Nutrient
    VisualObj : +int x-coord
    VisualObj : +int y-coord
    Bacterial : +int run_magnitude
    Bacterial : run(x-coord,y-coord)
    Bacterial : +int direction
    Bacterial : +int tumble
    Bacterial : canMove()
    Nutrient  : +int concentration
    Nutrient  : conGradient(concentration,x-coord,y-coord)
    