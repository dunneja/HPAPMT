#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Filename     : main.py
# Author       : James Dunne <james.dunne1@gmail.com>
# License      : GPL-3.0
# Comment      : This file is part of HPAPMT.
# ----------------------------------------------------------------------------

# Import python core modules
import PySimpleGUI as sg
import clipboard

# Import selfcoded modules containing project functions.
from modules.gui_modules import addprn_function as addprn
from modules.gui_modules import delprn_function as delprn
from modules.gui_modules import modprn_function as modprn
from modules.gui_modules import create_csv as cc

# HP Advance Printer Management Tool GUI
# Define the theme to be used
sg.theme('Reddit')

# Define the window top menus
menu_def = [['File', ['Generate CSV', 'Quit']],
            ['Edit', ['Paste']],
            ['Help', ['Notice', 'Usage', 'About', 'Github']], ]

# Define the window layout
layout = [[sg.Menu(menu_def, tearoff=False)],
          [sg.Text('Select a CSV file containing printer information.')],
          [sg.Text('CSV Filename:', size=(11, 1)), sg.Input(size=(
              49, 1), default_text='printers.csv', key='_Input_'), sg.FileBrowse(file_types=(("CSV Files", "*.csv"),),)],
          [sg.Radio('Add Printers', 'Radio1', default='True', key='_add_'), sg.Radio(
              'Delete Printers', 'Radio1', key='_del_'), sg.Radio('Modify Printers', 'Radio1', key='_mod_')],
          [sg.Output(size=(70, 10), key='_output_')],
          [sg.Submit(button_text='Execute'), sg.Button(button_text='Clear'), sg.Cancel(button_text='Quit'),
          sg.ProgressBar(2000, orientation='h', size=(32, 20), key='progbar')],
          ]

# Define the main window
window = sg.Window('HP Advance Printer Management Tool',
                   layout, icon=r'icons/hp.ico', keep_on_top='True')

# Window Event Loopls
while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break

    if event == 'Execute' and values['_add_'] == True:
        window['_output_']('')
        addprn(values['_Input_'])
        prtqty = len(values['_Input_'])
        for i in range(prtqty):
            window['progbar'].update_bar(i + 50000)

    if event == 'Execute' and values['_del_'] == True:
        window['_output_']('')
        delprn(values['_Input_'])
        prtqty = len(values['_Input_'])
        for i in range(prtqty):
            window['progbar'].update_bar(i + 50000)

    if event == 'Execute' and values['_mod_'] == True:
        window['_output_']('')
        modprn(values['_Input_'])
        prtqty = len(values['_Input_'])
        for i in range(prtqty):
            window['progbar'].update_bar(i + 50000)

    if event == 'Clear':
        window['_output_']('')
        window['progbar'].update_bar(0)

    if event == "Paste":
        text = clipboard.paste()  # Text to paste
        window['_Input_'].Widget.insert("insert", text)

    if event == 'About':

        popup = sg.popup_no_buttons('HP Advance Print Management Tool',
                                    'Version: 1.0',
                                    'Build Date: 01/02/2021',
                                    'Included Components:',
                                    '  * Python: 3.8',
                                    '  * PySimpleGUI: 4.34.0',
                                    '  * PyInstaller: 4.2',
                                    'Dependencies:',
                                    '  * Nvpscfg.exe',
                                    'Supported OS:',
                                    '  * Microsoft Windows Server 2019',
                                    title='About', keep_on_top='True', icon=r'icons/info.ico')

    if event == 'Usage':

        popup = sg.popup_no_buttons('DISCLAIMER',
                                    'THE SOFTWARE TOOL IS PROVIDED "AS IS", WITHOUT WARRANTY',
                                    'OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT',
                                    'LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS',
                                    'FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO',
                                    'EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES',
                                    'OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT',
                                    'TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION',
                                    'WITH THE SOFTWARE TOOL OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.',
                                    title='Usage Policy Notification', keep_on_top='True', icon=r'icons/info.ico')

    if event == 'Notice':

        popup = sg.popup_no_buttons('This Software Tool was created as a python related educational project.',
                                    'The tool is not endorsed or supported by HP Inc and was created solely '
                                    'for use in presales demo or pre production testing environments.',
                                    title='Software Notice', keep_on_top='True', icon=r'icons/info.ico')

    if event == 'Github':

        popup = sg.popup_no_buttons('Github:',
                                    ' * Code: https://github.com/dunneja/HPAPMT',
                                    ' * Issues: https://github.com/dunneja/HPAPMT/Issues',
                                    'Author: James Dunne - <james.dunne1@gmail.com',
                                    title='Github Information', keep_on_top='True', icon=r'icons/github.ico')

    if event == 'Generate CSV':

        if cc(values['_Input_']) == 1:
            window['_Input_']('Printers.csv')
            popup = sg.PopupOK('Printers CSV File Already Exists!',
                               title='Warning!', keep_on_top='True', icon=r'icons/warning.ico')

        else:
            window['_Input_']('Printers.csv')
            window['_output_']('')
            popup = sg.PopupOK('CSV File Generated!',
                               'Check README for CSV Config options.',
                               title='CSV Template', keep_on_top='True', icon=r'icons/info.ico')
window.close()
