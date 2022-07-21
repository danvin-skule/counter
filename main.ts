let count = 0
input.onButtonPressed(Button.A, function () {
    count += 1
    if (count > 9) {
        count = 0
    }
})
input.onButtonPressed(Button.B, function () {
    count += -1
    if (count < 0) {
        count = 9
    }
})
basic.forever(function () {
    basic.showNumber(count)
})
