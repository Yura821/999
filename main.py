def on_button_pressed_a():
    basic.show_number(5)
    basic.show_number(4)
    basic.show_number(3)
    basic.show_number(2)
    basic.show_number(1)
    for index in range(1):
        basic.show_icon(IconNames.HEART)
        basic.show_string("TQM")
input.on_button_pressed(Button.A, on_button_pressed_a)
