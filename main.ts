let info = ""
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 4; index++) {
        info = control.deviceName()
        basic.showString(info)
    }
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
})
