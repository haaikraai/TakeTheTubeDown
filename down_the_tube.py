import PySimpleGUI as sg
import pytube, yt_dlp, youtube_dl
from bs4 import BeautifulSoup as bs
import requests
from time import sleep

import os

sg.theme('Dark Blue 3')

class YTAccessor():
    yt_page = ''
    downloader = 'pytube' | 'yt-dlp' | 'youtube-dl'
    def __init__(self, yturl):
        self.yt_page = yturl
    
    def scrape_page(self):
        resp = requests.get(self.yt_page)
    
    def download_url(self, url):
        if self.downloader == self.downloader




layout = [[sg.Text('Enter URLs on a new line each:', justification='l', auto_size_text=True,)],
        [sg.Multiline(key='-USER-URLS-', size=(200, 22), expand_x=True, auto_refresh=True)],
        # [sg.Multiline(key='-URLS-', size=(900, 20), expand_x=True,)],
        [sg.Button('Download')],
        [sg.Multiline(key='-SAVED-URLS-', size=(200, 22), expand_x=True, disabled=True)],
        [sg.InputText(key='-BROWSE-', size=(200, 1), readonly=True, expand_x=True), sg.FolderBrowse('Browse', key='-BROWSE-')],
        [sg.FolderBrowse(), sg.Button('Ok', focus=True), sg.Button('Exit')],
        [sg.StatusBar(f'Downloading'.format(url))]]

window = sg.Window('URL List', layout, resizable=True, finalize=True, return_keyboard_events=True, margins=(20, 20), element_padding=(10,10), auto_size_text=True, auto_size_buttons=True)
# window.maximize()

while True:
    
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Escape:9':
        break
    elif event == 'Ok':
        urls = values['-USER-URLS-']
        values['-SAVED-URLS-'] = urls
        values['-USER-URLS-'] = ''
        values['-BROWSE-'] = 'entarad'
        window.write_event_value('-UPDATE-', values)
        window.refresh()
        print(urls)
        urls = urls.split('\n')
        print(urls)
        
        continue

    if event == 'Download':
        for url in urls:
            downloadUrls = YTAccessor(url)
        

window.close()