info = ""

def on_button_pressed_ab():
    global info
    for index in range(4):
        info = control.device_name()
        basic.show_string(info)
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
