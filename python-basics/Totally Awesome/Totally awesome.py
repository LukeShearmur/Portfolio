import PySimpleGUI as sg

im = ()

layout = [[sg.Text("Press the button for an Awesome surprise"), [sg.Button('Woop')]]]

window = sg.Window("Totally Awesome", layout, margins=(500, 300)) 

while True:
    event, values = window.read()

    if event in 'Woop':

        layout = [[sg.Image(r'C:\Users\Luke\Downloads\test.png')]]
        window = sg.Window("Totally Awesome", layout, margins=(500, 300))
    
    if event == sg.WIN_CLOSED:
        break

window.close()

