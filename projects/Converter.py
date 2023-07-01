import PySimpleGUI as psg

from Bonus import converters
from Bonus.converters import convert

label_1 = psg.Text("Enter feet")
input_1 = psg.Input(key="feet")

label_2 = psg.Text("Enter Inches")
input_2 = psg.Input(key="inches")

result_text = psg.Text(key="output", text_color="green")

convert_button = psg.Button("Convert")
exit_button = psg.Button('Exit')
window = psg.Window("Converter", layout=[
                                    [label_1, input_1],
                                    [label_2, input_2],
                                    [convert_button, exit_button, result_text]
                                ])
while True:
    event, values = window.read()
    match event:
        case psg.WIN_CLOSED:
            break
        case 'Exit':
            break
    feet = float(values['feet'])
    inches = float(values['inches'])
    meters = convert(feet, inches)
    window['output'].update(value= f"The meter value is {meters}")

window.close()