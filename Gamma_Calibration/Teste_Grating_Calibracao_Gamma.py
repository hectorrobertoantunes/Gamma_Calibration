from psychopy import visual, event, monitors



monitor = monitors.Monitor(name ='O_Nome_Do_Seu_Monitor')
win = visual.Window(monitor = monitor)
patch = visual.GratingStim(
    win,
    size=(1, 1),
    colorSpace='rgb255',
    units='norm',
    sf=0)
text = visual.TextStim(win, pos=(0, -0.6))

for intensity in range(0, 255, 10):
    patch.color = (intensity, intensity, intensity)
    text.text = f'x={intensity}'
    patch.draw()
    text.draw()
    win.flip()
    event.waitKeys()