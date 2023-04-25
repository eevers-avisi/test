import touch
import display
import led
import bluetooth

led.off(led.RED)
display.brightness(2)
text = display.Text('Hello world', 320, 200, display.GREEN, justify=display.MIDDLE_CENTER)
line = display.Line(50, 230, 590, 230, display.GREEN)
display.show(text, line)


def fn(bytes):
    txt = bytes.decode()
    text = display.Text(txt, 320, 200, display.GREEN, justify=display.MIDDLE_CENTER)
    display.show(text)

bluetooth.receive_callback(fn)



# Define the touch callback function which is triggered upon a touch event
def fn(arg):
    global text
    global line
    if arg == touch.A:
        print('A')
        display.show()
        display.show(display.Text("", 0, 0, 0))
    if arg == touch.B:
       display.show(display.Text("ping", 320, 200, display.GREEN, justify=display.MIDDLE_CENTER))
       print('B')


touch.callback(touch.BOTH, fn) # Attaches the callback to the both buttons
