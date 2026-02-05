input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("Hallo verden")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
radio.setGroup(42)
