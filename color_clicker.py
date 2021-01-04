from pynput.mouse import Listener, Button
from pyautogui import position, pixel
from clipboard import copy

print("right click: RGB, middle: #hex")


def on_click(x, y, button, pressed):
    if not pressed:
        return

    pos = position()
    r, g, b = pixel(pos[0], pos[1])
    if button == Button.right:
        copy(f"{r} {g} {b}")
        print(f"Copied RGB: {r} {g} {b}")

    elif button == Button.middle:
        copy("#%02x%02x%02x" % (r, g, b))
        print("Copied #hex: #%02x%02x%02x" % (r, g, b))


with Listener(on_click=on_click) as listener:
    listener.join()
