# this is a simple Gpio import and export script for a project of mine feel free to use it and customize it
# main use cases:
# Export a pin
# Set Pin to High or Low
# unexport a pin 

import os
import time



#configure this to anything you like GPIO has already been set change the names if you want, you can add sunxi names compatiblity or keep default physical pins

#make sure to keep unsable pins as " ", it need to be a string with space in the middle, DONT SKIP THESE PINS. Pin numbers are determined by order of the GPIO in the table


OPiZero2WLayout = [
    " ",     # 1 - 3.3V
    " ",     # 2 - 5V
    264,     # 3 - SDA.1
    " ",     # 4 - 5V
    263,     # 5 - SCL.1
    " ",     # 6 - GND
    269,     # 7 - PWM3
    224,     # 8 - TXD.0
    " ",     # 9 - GND
    225,     # 10 - RXD.0
    226,     # 11 - TXD.5
    257,     # 12 - PI01
    227,     # 13 - RXD.5
    " ",     # 14 - GND
    261,     # 15 - TXD.2
    270,     # 16 - PWM4
    " ",     # 17 - 3.3V
    228,     # 18 - PH04
    231,     # 19 - MOSI.1
    " ",     # 20 - GND
    232,     # 21 - MISO.1
    262,     # 22 - RXD.2
    230,     # 23 - SCLK.1
    229,     # 24 - CE.0
    " ",     # 25 - GND
    233,     # 26 - CE.1
    266,     # 27 - SDA.2
    265,     # 28 - SCL.2
    256,     # 29 - PI00
    " ",     # 30 - GND
    271,     # 31 - PI15
    267,     # 32 - PWM1
    258,     # 33 - PI02
    " ",     # 34 - GND
    272,     # 35 - PI16
    260,     # 36 - PI04
    " ",     # 37 - 5V
    259      # 38 - PI03
]

# [!!! IMPORTANT !!!]
# custom is by defualt the same as OPiZero2W you WILL need to change the GPIO. As mentions above pin numbers are determined by order of these GPIO in the table
#YOU WILL need to change the order of the GPIO if your using another board. sunxi-names supports isnt implemented right now but I think it will be very easy for you to do




CustomLayout = [
    " ",     # 1 - 3.3V
    " ",     # 2 - 5V
    264,     # 3 - SDA.1
    " ",     # 4 - 5V
    263,     # 5 - SCL.1
    " ",     # 6 - GND
    269,     # 7 - PWM3
    224,     # 8 - TXD.0
    " ",     # 9 - GND
    225,     # 10 - RXD.0
    226,     # 11 - TXD.5
    257,     # 12 - PI01
    227,     # 13 - RXD.5
    " ",     # 14 - GND
    261,     # 15 - TXD.2
    270,     # 16 - PWM4
    " ",     # 17 - 3.3V
    228,     # 18 - PH04
    231,     # 19 - MOSI.1
    " ",     # 20 - GND
    232,     # 21 - MISO.1
    262,     # 22 - RXD.2
    230,     # 23 - SCLK.1
    229,     # 24 - CE.0
    " ",     # 25 - GND
    233,     # 26 - CE.1
    266,     # 27 - SDA.2
    265,     # 28 - SCL.2
    256,     # 29 - PI00
    " ",     # 30 - GND
    271,     # 31 - PI15
    267,     # 32 - PWM1
    258,     # 33 - PI02
    " ",     # 34 - GND
    272,     # 35 - PI16
    260,     # 36 - PI04
    " ",     # 37 - 5V
    259      # 38 - PI03
]

UsingPins = "OPiZero2W"





def pinmode(PinNum, State):
    assert State in ["in", "out"], "State must be 'in' or 'out'"

    layout = None
    index = PinNum - 1
    GPIOnum = PinNum

    if UsingPins == "OPiZero2W":
        layout = OPiZero2WLayout
    elif UsingPins == "Custom":
        layout = CustomLayout
    elif UsingPins == "GPIO":
        print("Found GPIO Layout")
    else:
        raise ValueError(f"Unsupported layout type: {UsingPins}")
        return

    if layout:
        if layout[index] != " ":
            PinNum = layout[index]  # Translate pin number to GPIO number
        else:
            print(f"Pin {PinNum} is not usable (e.g., GND or VCC)")
            return
    else:
        print("Using GPIO Layout")
        PinNum = GPIOnum

    os.system(f"echo {PinNum} > /sys/class/gpio/export")
    os.system(f"echo {State} > /sys/class/gpio/gpio{PinNum}/direction")


def write(PinNum, State):
    layout = None
    index = PinNum - 1
    GPIOnum = PinNum

    if UsingPins == "OPiZero2W":
        layout = OPiZero2WLayout
    elif UsingPins == "Custom":
        layout = CustomLayout
    elif UsingPins == "GPIO":
        print("Found GPIO Layout")
    else:
        raise ValueError(f"Unsupported layout type: {UsingPins}")
        return

    if layout:
        if layout[index] != " ":
            PinNum = layout[index]  # Translate pin number to GPIO number
        else:
            print(f"Pin {PinNum} is not usable (e.g., GND or VCC)")
            return
    else:
        print("Using GPIO Layout")
        PinNum = GPIOnum

    assert State in [0, 1], "State must be 0 (Low) or 1 (High)"
    os.system(f"echo {State} > /sys/class/gpio/gpio{PinNum}/value")








def unexport(PinNum):
    layout = None
    index = PinNum - 1
    GPIOnum = PinNum

    if UsingPins == "OPiZero2W":
        layout = OPiZero2WLayout
    elif UsingPins == "Custom":
        layout = CustomLayout
    elif UsingPins == "GPIO":
        print("Found GPIO Layout")
    else:
        raise ValueError(f"Unsupported layout type: {UsingPins}")
        return

    if layout:
        if layout[index] != " ":
            PinNum = layout[index]  # Translate pin number to GPIO number
        else:
            print(f"Pin {PinNum} is not usable (e.g., GND or VCC)")
            return
    else:
        print("Using GPIO Layout")
        PinNum = GPIOnum



    os.system(f"echo {PinNum} > /sys/class/gpio/unexport")




def readpin(PinNum):
    layout = None
    index = PinNum - 1
    GPIOnum = PinNum

    if UsingPins == "OPiZero2W":
        layout = OPiZero2WLayout
    elif UsingPins == "Custom":
        layout = CustomLayout
    elif UsingPins == "GPIO":
        print("Found GPIO Layout")
    else:
        raise ValueError(f"Unsupported layout type: {UsingPins}")
        return

    if layout:
        if layout[index] != " ":
            PinNum = layout[index]  # Translate pin number to GPIO number
        else:
            print(f"Pin {PinNum} is not usable (e.g., GND or VCC)")
            return
    else:
        print("Using GPIO Layout")
        PinNum = GPIOnum



    try:
        with open(f"/sys/class/gpio/gpio{PinNum}/value", "r") as f:
            return int(f.read().strip())
    except FileNotFoundError:
        print(f"GPIO {PinNum} not exported!")
        return None
    except Exception as e:
        print(f"Error reading GPIO {PinNum}: {e}")
        return None






# BOARDMODE this is allow using custom pin names/numbers for spesific GPIO, this allows for compaitbility across all orange pi boards that use linux



def boardmode(BOARDMODE):
	assert BOARDMODE in ["OPiZero2W", "Custom", "GPIO"], "BOARDMODE can be set premade(OPiZero2W), Custom(needs to be configured in ORPi-wiring.py) or GPIO(Uses GPIO numbers)"
	UsingPins = BOARDMODE
	



