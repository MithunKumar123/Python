import PySimpleGUI as psg

label_1 = psg.Text("Select files to compress")
input_1 = psg.Input()
choose_button_1 = psg.FilesBrowse("Choose")

label_2 = psg.Text("Select destination folder")
input_2 = psg.Input()
choose_button_2 = psg.FolderBrowse("Choose")

compress_button = psg.Button("Compress")
window = psg.Window("File Zipper", layout=[
                                    [label_1, input_1, choose_button_1],
                                    [label_2, input_2, choose_button_2],
                                    [compress_button]
                                ])

window.read()
window.close()