"""Explain your code (Main.py) — Pygame Zero boat display (OOP)

This program is a simple Pygame Zero game that:

- loads your boat image from `images/boat.png`
- draws the boat in the middle of the screen
- lets you scale the boat up/down while the game is running


============================
1) Setup
============================
- `WIDTH`, `HEIGHT`, and `TITLE` configure the game window.


- The boat sprite is loaded using Pygame Zero's `Actor` system.
  - In this version, that is inside a class (see below).
  - Pygame Zero automatically looks for images inside the `images/` folder.


============================
2) OOP part: the `Boat` class
============================
The `Boat` class handles everything about the boat:

--------------------------------
- `__init__(...)`
--------------------------------
- Creates the sprite:
    `self.actor = Actor("boat")`

- Sets its starting position:
    `self.actor.pos = (x, y)`

- Sets up scaling values:
  - `self.scale` starts at `1.0`
  - `self.base_size` stores the original width/height
  - `self.scaled_surf_base` stores the original Surface
    (so scaling is always based on the original image)


--------------------------------
- `rescale()`
--------------------------------
- Builds a new resized Surface using:
    `pygame.transform.smoothscale(...)`

  What it does:
  - `pygame.transform` contains image-scaling functions.
  - `smoothscale` resizes the image using a higher-quality (smoother) scaling algorithm.
  - It creates a *new* surface at the requested size.

- Stores the result in:
    `self.scaled_surf`



--------------------------------
- `update()`
--------------------------------
- Runs every frame.
- Reads keyboard input:
  - hold **W**  -> scale increases (boat gets bigger)
  - hold **S**  -> scale decreases (boat gets smaller, with a minimum)
- Calls `rescale()` whenever the scale changes.


--------------------------------
- `draw()`
--------------------------------
- Runs every frame.
- Draws the resized boat using:
    `screen.blit(self.scaled_surf, rect)`

- The `rect` is centred on the boat position (`self.actor.pos`).


============================
3) Pygame Zero hook functions (what args they accept)
============================

Pygame Zero calls these automatically:

- `update()`
  - **Accepts:** no arguments
  - **Does:** called ~60 times per second. In this program it calls `player.update()` to handle scaling input.

- `draw()`
  - **Accepts:** no arguments
  - **Does:** called after `update()` to render the frame. In this program it clears the screen, draws the scaled boat, and draws the scale text.

- `on_mouse_down(pos)`
  - **Accepts:** `pos` (a tuple `(x, y)`)
  - **Does:** runs once when the mouse button is pressed. (Currently `pass`, so it does nothing.)

- `on_key_down(key)`
  - **Accepts:** `key` (a key name, e.g. `'w'`, `'space'`, `'left'`)
  - **Does:** runs once when a key is pressed down. (Currently `pass`, so it does nothing.)



Run it with:
    python -m pgzero Main.py
"""



