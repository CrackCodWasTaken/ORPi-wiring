# ORPi-wiring
this is library that can make GPIO easier for you.  this library has been tested on orange pi zero 2w, and will work with every other model if you use GPIO board mode.
I made it becuase I couldnt find a good solution for GPIO since every library i found was either not supported by orange pi zero 2w
or not working properly, you can modify the library and its extermely simple with only one script and a few lines of code. of course it
does work with raspberry pi librarys for tools requiring such a wiring library since this ones basic and only designed to export, change state, unexport a pin, read a pin


I dont know if analoge functionality is there but ill try to make a function for analogWrite and ill try adding a export all feature to export all pins used





UPDATE LOG! V2.0:

* Added Physical Pin support

* Added Custom Layout support






HOW TO USE!

1. Download the latest ORPi-wiring.py file
2. move the file in the same directory as your project
3. add "import ORPi-wiring as GPIO" at the top of your project
4. select boardmode using GPIO.boardmode() list of board modes are below Alternativly you can just use "GPIO" which allows you to pass GPIO number instead of physcial pin number to interact with a GPIO, check the orange pi wiki for your board and scrol down to wiringOP to find the GPIO for your board this can be used to configure a custom board, hence this library supports all orange pi models running linux

List of Default supported Boards:
* Orange pi zero 2w

NOTE!!
more board support coming soon however you can include your own board config by editing the ORPi-wiring.py file all instructions are in it as well






COMMANDS TO USE THE LIBRARY!


boardmode(BOARDMODE) -- used to set boardmode to use either physical pins

pinmode(PIN, State) -- used to set a GPIO/PIN as input or output and export, to do this you must either put "in"(Input) or "out"(output) IN STRING!

write(PIN, State) -- used to set a GPIO/PIN either HIGH or LOW, to do this either put state as 1(HIGH) or 0(LOW)

unexport(PIN) -- used to unexport a GPIO/PIN when you done using it

readpin(PIN) -- used to read value of a GPIO/PIN, this return the value of the GPIO as a int

NOTE!!
analoge MIGHT work, I havent tested analoge yet however the logic for readpin is simple, it returns the value of the pin in /sys/class/gpio/gpio(PIN)/value



