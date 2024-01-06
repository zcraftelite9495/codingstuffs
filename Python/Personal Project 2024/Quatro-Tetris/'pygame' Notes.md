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