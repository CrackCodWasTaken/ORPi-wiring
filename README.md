# ORPi-wiring
this is a very basic library that can make GPIO easier for you.  this library has been tested on orange pi zero 2w.
I made it becuase I couldnt find a good solution for GPIO since every library i found was either not supported by orange pi zero 2w
or not working properly, you can modify the library and its extermely simple with only one script and a few lines of code. of course it
does work with raspberry pi librarys for tools requiring such a wiring library since this ones VERY basic and only designed to export, change state, unexport a pin, read a pin

i dont know if analoge functionality is there but ill try to make a function for analogWrite and ill try adding a export all feature to export all pins used


how to use:

simply download the file and include it in your project.

commands are simple

YOU MUST USE GPIO!! NOT PHYSICAL PIN NUMBERS OR SUNXI NAMES OF PINS!!



pinmode(GPIO, State) -- used to set a GPIO as input or output and export, to do this you must either put "in"(Input) or "out"(output) IN STRING!

write(GPIO, State) -- used to set a GPIO either HIGH or LOW, to do this either put state as 1(HIGH) or 0(LOW)

unexport(GPIO) -- used to unexport a GPIO when you done using it

readpin(GPIO) -- used to read value of a GPIO, this return the value of the GPIO as a int
