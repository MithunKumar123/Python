import PySimpleGUI as psg
from zip_creator import make_archive

label_1 = psg.Text("Select files to compress")
input_1 = psg.Input()
choose_button_1 = psg.FilesBrowse("Choose", key='ChooseFiles')

label_2 = psg.Text("Select destination folder")
input_2 = psg.Input()
choose_button_2 = psg.FolderBrowse("Choose",key='ChooseFolder')

compress_button = psg.Button("Compress")
output_label = psg.Text(key="output", text_color="green")
window = psg.Window("File Zipper", layout=[
                                    [label_1, input_1, choose_button_1],
                                    [label_2, input_2, choose_button_2],
                                    [compress_button, output_label]
                                ])

while True:
    event, values = window.read()
    print(event)
    print(values)
    filePaths = values['ChooseFiles'].split(";")
    folder = values["ChooseFolder"]
    make_archive(filePaths, folder)
    window['output'].update(values="Compression Completed!!!")

window.close()