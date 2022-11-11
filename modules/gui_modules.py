#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Filename     : gui_modules.py
# Author       : James Dunne <james.dunne1@gmail.com>
# License      : GPL-3.0
# Comment      : This file is part of HPAPMT.
# ----------------------------------------------------------------------------
# Import core modules
import os.path
import PySimpleGUI as sg

# Import project specific custom modules
from modules.csv_import import dictreaderimport as csv_import
from modules.conf_files import configfile as cf
from modules.printer_class import Printer as prn

# Pass config_file variable to the configfile class in conf_file.py
# This will check if the file exists, create it if not and read the
# config values.
config_file_class = cf('config.ini')

def addprn_function(input_value):
    """
    Function to add printers
    """
    # Check log dir exists, if not create it!
    cf.check_log_dir()

    # Define CSV Filename from sg.input
    csv_filename = input_value

    # Check if the config_file exists, if not it creates a default.
    # Uses the check_conf method in the configfile class.
    cf.check_conf(config_file_class)

    printer_file_class = cf(csv_filename)

    if cf.check_csv(printer_file_class) == 0:

        # Popup to warn user prior to execution. Quit possible.
        popup = sg.PopupYesNo('Are you sure you want to execute?',
                              'This will update HPAdvance Directly!', title='Warning!',
                              keep_on_top='True', icon=r'icons/warning.ico', location=(900, 450))

        if popup == 'Yes':

            print(f'\nUsing CSV Filename: {csv_filename} \n')

            # Pass CSV file to csv_import function
            new_printers = csv_import(csv_filename)

            # Assign the Class Printer with the csv file parsed to a variable.
            printer_install = prn(new_printers)

            # Execute Class Printer(). This will import the csv file and assign
            # the list containing the printer dictionary to a variable.
            printer_install

            # Execute each method of the Printer Class.
            printer_install.add_printer()

            # Print Message confirming end of operation.
            print(f'\nPrinter Add Operation Completed!\n')

        else:

            print(f'\nPrinter Add Operation Aborted!\n')

        return

    else:

        return

def delprn_function(input_value):
    """
    Function to del printers
    """
    # Check log dir exists, if not create it!
    cf.check_log_dir()

    # Define CSV Filename
    csv_filename = input_value

    # Check if the config_file exists, if not it creates a default.
    # Uses the check_conf method in the configfile class.
    cf.check_conf(config_file_class)

    printer_file_class = cf(csv_filename)

    if cf.check_csv(printer_file_class) == 0:

        # Popup to warn user prior to execution. Quit possible.
        popup = sg.PopupYesNo('Are you sure you want to execute?',
                              'This will update HPAdvance Directly!', title='Warning!',
                              keep_on_top='True', icon=r'icons/warning.ico')

        if popup == 'Yes':

            print(f'\nUsing CSV Filename: {csv_filename} \n')

            # Pass CSV file to csv_import function
            new_printers = csv_import(csv_filename)

            # Assign the Class Printer with the csv file parsed to a variable.
            printer_install = prn(new_printers)

            # Execute Class Printer(). This will import the csv file and assign the list
            # containing the printer dictionary to a variable.
            printer_install

            # Execute each method of the Printer Class.
            printer_install.del_printer()

            # Print Message confirming end of operation.
            print(f'\nPrinter Delete Operation Completed!\n')

        else:

            print(f'\nPrinter Delete Operation Aborted!\n')

            return
    else:

        return


def modprn_function(input_value):
    """
    Function to mod printers
    """
    # Check log dir exists, if not create it!
    cf.check_log_dir()

    # Define CSV Filename
    csv_filename = input_value

    # Check if the config_file exists, if not it creates a default.
    # Uses the check_conf method in the configfile class.
    cf.check_conf(config_file_class)

    printer_file_class = cf(csv_filename)

    if cf.check_csv(printer_file_class) == 0:

        # Popup to warn user prior to execution. Quit possible.
        popup = sg.PopupYesNo('Are you sure you want to execute?',
                              'This will update HPAdvance Directly!', title='Warning!',
                              keep_on_top='True', icon=r'icons/warning.ico')

        if popup == 'Yes':

            print(f'\nUsing CSV Filename: {csv_filename} \n')

            # Pass CSV file to csv_import function
            new_printers = csv_import(csv_filename)

            # Assign the Class Printer with the csv file parsed to a variable.
            printer_install = prn(new_printers)

            # Execute Class Printer(). This will import the csv file and assign the list
            # containing the printer dictionary to a variable.
            printer_install

            # Execute each method of the Printer Class.
            printer_install.mod_printer()

            # Print Message confirming end of operation.
            print(f'\nPrinter Modification Operation Completed!\n')

        else:

            print(f'\nPrinter Modification Operation Aborted!\n')

            return

    else:

        return


def create_csv(input_value):
    """
    Create the Printers.csv configuration file
    """
    csv_filename = input_value

    if (os.path.isfile(csv_filename)):
        return(1)
    elif (os.path.isfile('printers.csv')):
        return(1)

    else:

        with open('printers.csv', 'w') as csv:
            csv.write('Printer,CommType,TcpHost,TCPRPort,Location,Model')
            csv.write(
                '\nHPLAB-PRN-01,tcpip/sock,192.168.2.254,9100,HPLAB,NPIC5155D')
            csv.write(
                '\nHPLAB-PRN-02,tcpip/sock,192.168.2.255,9100,HPLAB,NPIC5155D')
            csv.write(
                '\nHPLAB-PRN-03,tcpip/sock,192.168.2.256,9100,HPLAB,NPIC5155D')
            csv.write(
                '\nHPLAB-PRN-04,tcpip/sock,192.168.2.257,9100,HPLAB,NPIC5155D')
            csv.write(
                '\nHPLAB-PRN-05,tcpip/sock,192.168.2.258,9100,HPLAB,NPIC5155D')
            csv.write(
                '\nHPLAB-PRN-06,tcpip/sock,192.168.2.259,9100,HPLAB,NPIC5155D')
            csv.write(
                '\nHPLAB-PRN-07,tcpip/sock,192.168.2.260,9100,HPLAB,NPIC5155D')
            csv.write(
                '\nHPLAB-PRN-08,tcpip/sock,192.168.2.261,9100,HPLAB,NPIC5155D')
            csv.close()