import FreeSimpleGUI as sg

# 1. El layout (estructura de la ventana)
layout = [
    [sg.Text("Hello David! This is your first GUI")],
    [sg.Button("Greet"), sg.Button("Exit")]
]

# 2. Crear la ventana
window = sg.Window("My First Window", layout)

# 3. El event loop (escuchar eventos)
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Greet":
        sg.popup("Welcome to your Finance Manager!")

window.close()