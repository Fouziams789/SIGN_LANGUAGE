import PySimpleGUI as sg
def learsignlayout():
    p1_layout = [[sg.Image('imgs/welcome.png', size=(300, 300))]]
    p2_layout = [[sg.Image('imgs/please.png', size=(300, 300))]]
    p3_layout = [[sg.Image('imgs/sorry.png', size=(300, 300))]]
    p4_layout = [[sg.Image('imgs/yes.png', size=(300, 300))]]
    p5_layout = [[sg.Image('imgs/help.png', size=(300, 300))]]
    p6_layout = [[sg.Image('imgs/no.png', size=(300, 300))]]

    my_layout = [[sg.Column(p1_layout), sg.Column(p2_layout), sg.Column(p3_layout)],
                 [sg.Column(p4_layout), sg.Column(p5_layout), sg.Column(p6_layout)]
                 ]
    window = sg.Window("Learn Sign Language Gestures", my_layout, finalize=True, resizable=True,
                       background_color='white', element_justification='c')
    # window.maximize()
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event == sg.WIN_CLOSED:
            break
    window.close()