count = 0

def on_button_pressed_a():
    global count
    count += 1
    if count > 9:
        count = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global count
    count += -1
    if count < 0:
        count = 9
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    basic.clear_screen()
    basic.show_leds("""
        # . . . #
                # . . . #
                # # # # #
                # . . . #
                # . . . #
    """)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_forever():
    basic.show_number(count)
basic.forever(on_forever)
