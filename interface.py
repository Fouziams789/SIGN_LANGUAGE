import PySimpleGUI as sg
import detect as dt
import learnsigns as ls

head_layout = [
    [sg.Image('imgs/about.png')]
]
home_layout = [
    [sg.Button('Learn Sign Language')],
    [sg.Button('       Detect Signs     ')]
]
layout = [
    [[sg.Column(head_layout, key='Home')], [sg.Column(home_layout, key='Learn')]]
]
# noinspection PyTypeChecker
window = sg.Window('Sign Language Detector Interface', layout, element_justification='c')

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event == 'Learn Sign Language':
        ls.learsignlayout()
    elif event == '       Detect Signs     ':
        dt.main(0, 'multi_best.pt')
        # dt.main(0,'plain_datasetbest.pt')
    if event == sg.WIN_CLOSED:
        break
window.close()
