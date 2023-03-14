import PySimpleGUI as sg
import azure_translate_api as az

# Very basic window where user can enter text to translate
layout = [[sg.Text("Enter text to translate")],
          [sg.Multiline("", key="-INPUT-", size=(50, 5))],
          [sg.Text("Click \"OK\" to translate")],
          [sg.Button("OK")],
          [sg.Text("Translation:")],
        [sg.Multiline("", key="-OUTPUT-", size=(50, 5))]
          ]

window = sg.Window("Translator", layout, size=(500, 300))

# Event loop
def open_program():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "OK" or event == "<Return>":
            text = values["-INPUT-"]
            translation = az.azure_translate(text)
            window["-OUTPUT-"].update(translation)
        #user closes window
        if event == sg.WIN_CLOSED:
            break
    window.close()
    #stop main
    exit()