from machine import Pin
pins = {"LED": Pin("LED", Pin.OUT)}
def pin_onoff(task):
    pin = task["pin"]
    val = task["val"]
    if pin in pins:
        pins[pin].value(val)
        return "Changed pin " + str(pin) + " to the value " + str(val)
    else:
        return "Unknown or unconfigured pin " + str(pin)

funcs = {"pin_onoff": pin_onoff}
