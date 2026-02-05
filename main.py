def on_button_pressed_a():
    radio.send_string("Hallo verden")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

radio.set_group(42)