# this is a simple Gpio import and export script for a project of mine feel free to use it and customize it
# main use cases:
# Export a pin
# Set Pin to High or Low
# unexport a pin 

import os

OPiZero2WLayout = [
    " ", " ", 264, " ", 263, " ", 269, 224,
    " ", 225, 226, 257, 227, " ", 261, 270,
    " ", 228, 231, " ", 232, 262, 230, 229,
    " ", 233, 266, 265, 256, " ", 271, 267,
    258, " ", 272, 260, " ", 259
]

CustomLayout = OPiZero2WLayout[:]  # Same for now

UsingPins = "OPiZero2W"


def _resolve_pin(pin_num):
    """Convert board pin to GPIO number based on layout."""
    layouts = {
        "OPiZero2W": OPiZero2WLayout,
        "Custom": CustomLayout
    }
    layout = layouts.get(UsingPins)
    if UsingPins == "GPIO":
        return pin_num
    if not layout:
        raise ValueError(f"Unsupported layout: {UsingPins}")
    gpio = layout[pin_num - 1]
    if gpio == " ":
        raise ValueError(f"Pin {pin_num} is not usable (GND/VCC)")
    return gpio


def pinmode(pin_num, mode):
    assert mode in ["in", "out"], "Mode must be 'in' or 'out'"
    gpio = _resolve_pin(pin_num)
    try:
        with open("/sys/class/gpio/export", "w") as f:
            f.write(str(gpio))
    except FileExistsError:
        pass
    with open(f"/sys/class/gpio/gpio{gpio}/direction", "w") as f:
        f.write(mode)


def write(pin_num, value):
    assert value in [0, 1], "Value must be 0 or 1"
    gpio = _resolve_pin(pin_num)
    with open(f"/sys/class/gpio/gpio{gpio}/value", "w") as f:
        f.write(str(value))


def readpin(pin_num):
    gpio = _resolve_pin(pin_num)
    try:
        with open(f"/sys/class/gpio/gpio{gpio}/value", "r") as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return None


def unexport(pin_num):
    gpio = _resolve_pin(pin_num)
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(gpio))


def boardmode(mode):
    global UsingPins
    assert mode in ["OPiZero2W", "Custom", "GPIO"]
    UsingPins = mode
