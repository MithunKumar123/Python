import PySimpleGUI as psg

label_1 = psg.Text("Enter feet")
input_1 = psg.Input()

label_2 = psg.Text("Enter Inches")
input_2 = psg.Input()

convert_button = psg.Button("Convert")
window = psg.Window("Converter", layout=[
                                    [label_1, input_1],
                                    [label_2, input_2],
                                    [convert_button]
                                ])

window.read()
window.close()