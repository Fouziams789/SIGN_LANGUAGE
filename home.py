import detect as dt
import PySimpleGUI as Sg
from datetime import datetime
# using now() to get current time
# background_layout = [title_bar('This is the titlebar', sg.theme_text_color(), sg.theme_background_color()),
#                      [sg.Image(r'bg_qb.png')]]
# window_background = sg.Window('Background', background_layout, no_titlebar=True, finalize=True,
#                      margins=(0, 0), element_padding=(0, 0), right_click_menu=[[''], ['Exit', ]])
layout = [

            [Sg.Text("                                      Sign Language Detector")],
            [Sg.Text("---------------------------------------------------------------------------------------------------------------------------         ")],
            [Sg.Button("Click here to detect signs")]
         ]
layout2 = [
            [Sg.Text("                                      ")],

            [Sg.Text("---------------------------------------------------------------------------------------------------------------------------         ")],
            [Sg.Text("                                            Send Your Feedback")],
            [Sg.Text("---------------------------------------------------------------------------------------------------------------------------         ")],
            [Sg.Text("                                                                                                                                                                        ")],
            [Sg.Multiline(size=(30, 5), key='textbox')],
            [Sg.Text("                                                                                                                                                                        ")],
            [Sg.Button("Send Feedback")]
          ]
# Create the window
window = Sg.Window("Sign Language Detector", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Click here to detect signs":
        now = datetime.now()
        session_start_time = now.strftime('Date: %d/%Y/%m Time: %I:%M:%S')
        dt.main(0,"best.pt")
        window.close()
        window = Sg.Window("FeedBack", layout2)#show closing window
    elif event == Sg.WIN_CLOSED:
        break
window.close()