# Python Photo Collage

A simple python implementation for creating a photo collage (grid).

## Workflow

**V.1**: The current implementation is creating images from `NxM` sized arrays that are initialized with a random pixel color (that will serve as background).

* The matrices are created with random sizes (e.g., `N` and `M` are randomly chosen at *creation time*).
* Based on a *sort-by-size* procedure, decision for truncating each matrix is done, such that an optimal joining procedure for any two matrices is done properly. 
* Finally, a grid arrangement of all the obtained objects is done, with an export as a single unified matrix.
