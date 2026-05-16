# Tea-n-Thieves (Pygame Zero)

## Run
```bash
python -m pgzero Main.py
```

## What you should see
- A boat image (`images/boat.png`) drawn in the middle of the screen.

## Controls
- **W**: scale the boat up
- **S**: scale the boat down

## Where the important code is
### `Main.py`
- `player = Actor("boat")`: loads the boat asset
- `update()`:
  - checks keyboard input (W/S)
  - updates `scale`
- `draw()`:
  - clears the screen
  - draws a resized surface of the boat using `screen.blit(...)`
  - draws the title text in the top-left

## Assets
- `images/boat.png` (must exist)

