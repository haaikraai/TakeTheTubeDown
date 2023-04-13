import PySimpleGUI as sg
from time import sleep
import os

sg.theme('Dark Blue 3')

layout = [[sg.Text('Enter URLs on a new line each:')],
        [sg.Multiline(key='-URLS-', size=(900, 30), expand_x=True)],
        # [sg.Multiline(key='-URLS-', size=(900, 20), expand_x=True,)],
        [sg.Multiline(key='-URLS-', size=(900, 30), expand_x=True, disabled=True)],
        [sg.InputText(key='-BROWSE-', size=(200, 1), readonly=True, expand_x=True), sg.FolderBrowse('Browse', key='-BROWSE-')],
        [sg.FolderBrowse(), sg.Button('Download', focus=True), sg.Button('Cancel')]]

window = sg.Window('URL List', layout, resizable=True, finalize=True, return_keyboard_events=True)
# window.maximize()

while True:
    sleep(1)
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Escape:9':
        break
    elif event == 'Submit':
        urls = values['-URLS-'].split(',')
        print(urls)

window.close()