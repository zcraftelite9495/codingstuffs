# Notes on 'pygame'

## How 'pygame' renders its display

### Display Surface
* Its like a blank canvas
* 1 per game instance
* Called when we call the `screen = pygame.display.set_mode((#, #))` function
* Object used when we call the `pygame.display.update()` function

### Surface
* Another type of blank canvas
* We can have as many surfaces as the client can handle

### Rect
* Rectanges that we use for positioning, collision detection and for drawing objects

## Disply of block entities

### Representing blocks
To represent the different rotation states of objects, we can imagine them in a grid big enough to fit it in all rotation states. The box is divided into a grid and we label the top left cell as the origin (0, 0). For each of the rotation states, we store the cells that occupy the grid (not all the cells in the grid).