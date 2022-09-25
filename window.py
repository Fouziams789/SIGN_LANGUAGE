import PySimpleGUI as sg

sg.Window._move_all_windows = True

def title_bar(title, text_color, background_color):

    bc = background_color
    tc = text_color
    font = 'Helvetica 12'

    return [sg.Col([[sg.T(title, text_color=tc, background_color=bc, font=font, grab=True)]], pad=(0, 0),
                   background_color=bc),
            sg.Col([[sg.T('_', text_color=tc, background_color=bc, enable_events=True, font=font, key='-MINIMIZE-'),
                     sg.Text('❎', text_color=tc, background_color=bc, font=font, enable_events=True, key='Exit')]],
                   element_justification='r', key='-C-', grab=True,
                   pad=(0, 0), background_color=bc)]

def main():
    background_layout = [title_bar('Sign Language Detect', sg.theme_text_color('black'), sg.theme_background_color()), [sg.Image(r'bg_qb.png')]]
    window_background = sg.Window('Background', background_layout, no_titlebar=True, finalize=True, margins=(0, 0), element_padding=(0, 0), right_click_menu=[[''], ['Exit', ]])

    window_background['-C-'].expand(True, False, False)
    column1 = [[sg.Text('Column 1', justification='center', size=(10, 1))],
               [sg.Spin(values=('Spin Box 1', 'Spin Box 2', 'Spin Box 3'),
                        initial_value='Spin Box 1')],
               [sg.Spin(values=['Spin Box 1', '2', '3'],
                        initial_value='Spin Box 2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

    layout = [
        # [sg.Text('', size=(30, 2), justification='left', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.InputText('This is my text')],
        # to create a frame
        [sg.Frame(layout=[
            [sg.CBox('Checkbox', size=(10, 1)),
             sg.CBox('My second checkbox!', default=True)],
            [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10, 1)),
             sg.Radio('My second Radio!', "RADIO1")]], title='Options', relief=sg.RELIEF_SUNKEN,
            tooltip='Use these to set flags')],
        # to create a textbox
        [sg.MLine(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
         sg.MLine(default_text='A second multi-line', size=(35, 3))],
        # to create a combo box
        [sg.Combo(('Combobox 1', 'Combobox 2'), default_value='Combobox 1', size=(20, 1)),
        #  create horizontal slider
        sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
        #create menu with 3 options
        [sg.OptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
        # to create a list box
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
         # label group + column1
         sg.Frame('Labelled Group', [[
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, tick_interval=25),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
             sg.Col(column1)]])
         ],
        [sg.Text('_' * 80)],
        [sg.Text('Choose A Folder', size=(40, 1))],
        [sg.Text('Your Folder', size=(15, 1), justification='right'),
         sg.InputText('Default Folder'), sg.FolderBrowse()],
        [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()],
        # [sg.Text('', size=(30, 1), justification='center', font=("Helvetica", 25),
        #          relief=sg.RELIEF_SUNKEN)]
    ]

    top_window = sg.Window('Everything bagel', layout, finalize=True, keep_on_top=True, grab_anywhere=False,
                           transparent_color=sg.theme_background_color(), no_titlebar=True)

    while True:
        window, event, values = sg.read_all_windows()
        print(event, values)
        if event is None or event == 'Cancel' or event == 'Exit':
            print(f'closing window = {window.Title}')
            break

    top_window.close()
    window_background.close()

if __name__ == '__main__':
    main()