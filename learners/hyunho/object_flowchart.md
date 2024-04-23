'''mermaid
    graph TD
        A[Simulation] --> B[Simulation parameters]
        A[Simulation\n-simulation step] --> C[Coordinate system object\n -position]
        F[Movement type\n-run\n-tumble] --> D
        D[Bacteria\n -movement\n -longevity] --> C  
        E[Nutrient] --> C  
        A --> G[Visualization]
'''
