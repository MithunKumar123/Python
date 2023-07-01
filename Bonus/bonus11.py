import PySimpleGUI as psg
from zip_creator import extract_archive

label_1 = psg.Text("Select archived file to extract")
input_1 = psg.Input()
choose_button_1 = psg.FileBrowse("Choose", key='file')

label_2 = psg.Text("Select destination folder")
input_2 = psg.Input()
choose_button_2 = psg.FolderBrowse("Choose",key='folder')

compress_button = psg.Button("Extract")
output_label = psg.Text(key="output", text_color="green")
window = psg.Window("File Extractor", layout=[
                                    [label_1, input_1, choose_button_1],
                                    [label_2, input_2, choose_button_2],
                                    [compress_button, output_label]
                                ])

while True:
    event, values = window.read()
    archive_path = values['file']
    folder = values["folder"]
    extract_archive(archive_path, folder)
    window['output'].update(value="Extraction Completed!!!")

window.close()