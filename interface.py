import PySimpleGUI as sg
import  detect as dt
# learn_layout = [
#     [sg.Button('back to home')]
# # ]
# def title_bar(title, text_color, background_color):
#
#     bc = background_color
#     tc = text_color
#     font = 'Helvetica 12'
#
#     return [sg.Col([[sg.T(title, text_color=tc, background_color=bc, font=font, grab=True)]], pad=(0, 0),
#                    background_color=bc),
#             sg.Col([[sg.T('_', text_color=tc, background_color=bc, enable_events=True, font=font, key='-MINIMIZE-'),
#                      sg.Text('❎', text_color=tc, background_color=bc, font=font, enable_events=True, key='Exit')]],
#                    element_justification='r', key='-C-', grab=True,
#                    pad=(0, 0), background_color=bc)]
#
# background_layout = [title_bar('Sign Language Detector', sg.theme_text_color('black'), sg.theme_background_color()), [sg.Image(r'bg_qb.png')]]
# window_background = sg.Window('Background', background_layout, no_titlebar=True, finalize=True, margins=(0, 0), element_padding=(0, 0), right_click_menu=[[''], ['Exit', ]])
#
# window_background['-C-'].expand(True, False, False)
head_layout = [
    [sg.Image('bg_pic.png')]
]
home_layout = [
    [sg.Button('Learn Sign Language')],
    [sg.Button('       Detect Signs     ')],
    [sg.Button('          About Us       ')]
]
layout = [
    [[sg.Column(head_layout, key='Home')], [sg.Column(home_layout, key='Learn')]]
]
window = sg.Window('Sign Language Detector Interface',layout,element_justification='c')

while True:
    event, values = window.read()
    if event in (None,'Exit'):
        break
    elif event == 'Learn Sign Language':
        window[f'Home'].update(visible=False)
        window[f'Learn'].update(visible=True)
    elif event == '       Detect Signs     ':
        dt.main(0, 'multi_best.pt')
        # dt.main(0, "best.pt")
        # dt.main(0,'plain_datasetbest.pt')
    elif event == 'back to home':
        window[f'Learn'].update(visible=False)
        window[f'Home'].update(visible=True)
    if event == sg.WIN_CLOSED:
        break
window.close()