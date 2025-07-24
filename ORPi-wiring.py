# this is a simple Gpio import and export script for a project of mine feel free to use it and customize it
# main use cases:
# Export a pin
# Set Pin to High or Low
# unexport a pin 

import os
import time


def pinmode(PinNum, State):
    assert State in ["in", "out"], "State must be 'in' or 'out'"
    os.system(f"echo {PinNum} > /sys/class/gpio/export")
    os.system(f"echo {State} > /sys/class/gpio/gpio{PinNum}/direction") 

def write(PinNum, State):
    assert State in [0, 1], "State must be 0 (Low) or 1 (High)"
    os.system(f"echo {State} > /sys/class/gpio/gpio{PinNum}/value")

def unexport(PinNum):
        os.system(f"echo {PinNum} > /sys/class/gpio/unexport")

def readpin(PinNum):
    try:
        with open(f"/sys/class/gpio/gpio{PinNum}/value", "r") as f:
            return int(f.read().strip())
    except FileNotFoundError:
        print(f"GPIO {PinNum} not exported!")
        return None
    except Exception as e:
        print(f"Error reading GPIO {PinNum}: {e}")
        return None
