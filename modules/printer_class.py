#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Filename     : printer_class.py
# Author       : James Dunne <james.dunne1@gmail.com>
# License      : GPL-3.0
# Comment      : This file is part of HPAPMT.
# ----------------------------------------------------------------------------
# Import modules
import subprocess
from datetime import datetime

class Printer():
    """
    A class to represent a printer definition
    """
    def __init__(self, new_printers):
        """
        Assign dictionary from csvimport list new_printers to variable
        called new_printers.
        """
        # printers csv file
        self.new_printers = new_printers

        # set log dir
        self.log_dir = 'logs'

        # log file date time format
        self.file_dt = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

        # log file format
        self.log_format = '.txt'

        # log entry time stamp
        self.timestamp = str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S-%p"))

    def add_printer(self):
        """
        Create the printer definition specified in the printers.csv file
        """
        # stdout log file name for mod function
        stdout_lfn = 'add_std_output'

        # stdout final log file
        stdout_lf = self.log_dir + '/' + stdout_lfn + \
            '_' + self.file_dt + self.log_format

        # Create an empty list for storing stdout log output
        log_output = []

        # Loop through the printers in dictionary.
        for printer in self.new_printers:
            # Define dictionary key,value for inf file as a single variable.
            # This is needed for prndrvr.vbs since it uses a different param
            # syntax compared to prnport.vbs.
            printer_name = printer['Printer']
            printer_commtype = printer['CommType']
            printer_tcphost = printer['TcpHost']
            printer_tcprport = printer['TCPRPort']
            printer_location = printer['Location']
            printer_model = printer['Model']

            add_prn_cmd = [r'C:/Program Files/LRS/VPSX EOM/bin/nvpscfg.exe', '-add',
                           '-printer=' + printer_name, '-commtype=' + printer_commtype,
                           '-tcphost=' + printer_tcphost, '-tcprport=' + printer_tcprport,
                           '-location=' + printer_location, '-model=' + printer_model]

            # Use a try statement to allow for execption checking.
            try:

                # run the subprocess call and specify stdout and stderr
                add_prn_cmd_sp = subprocess.run(
                    add_prn_cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL, text=True)

                # Assign stdout to a variable
                output = add_prn_cmd_sp.stdout

                # Append the variable to a list
                log_output.append(output)

                # write stdout list to file by interating on the list
                # write stdout list to log file
                with open(stdout_lf, 'w') as fout:
                    for item in log_output:
                        fout.write(
                            str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S-%p")))
                        fout.write("%s\n" % item)
                print(output)

            # exception when error occurs
            except Exception as e:

                # append stdout to log_output list
                log_output.append(e)

                # write stdout list to log file
                with open(stdout_lf, 'w') as fout:
                    for item in log_output:
                        fout.write(
                            str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S-%p")))
                        fout.write("%s\n" % e)

                # define exception error message
                error_msg = 'Error(s) Found'

                # print exception errr message
                print(f'{error_msg}:{e}')

    def del_printer(self):
        """
        Delete the printer definition specified in the printers.csv file
        """
        # stdout log file name for mod function
        stdout_lfn = 'del_std_output'

        # stdout final log file
        stdout_lf = self.log_dir + '/' + stdout_lfn + \
            '_' + self.file_dt + self.log_format

        # Create an empty list for storing stdout log output
        log_output = []

        # Loop through the printers in dictionary.
        for printer in self.new_printers:
            printer_name = printer['Printer']

            del_prn_cmd = [r'C:/Program Files/LRS/VPSX EOM/bin/nvpscfg.exe',
                           '-delete', '-printer=' + printer_name]

            # Use a try statement to allow for execption checking.
            try:
                # run the subprocess call and specify stdout and stderr
                del_prn_cmd_sp = subprocess.run(
                    del_prn_cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL, text=True)

                # Assign stdout to a variable
                output = del_prn_cmd_sp.stdout

                # Append the variable to a list
                log_output.append(output)

                # write stdout list to file by interating on the list
                # write stdout list to log file
                with open(stdout_lf, 'w') as fout:
                    for item in log_output:
                        fout.write(
                            str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S-%p")))
                        fout.write("%s\n" % item)
                print(output)

            # exception when error occurs
            except Exception as e:

                # append stdout to log_output list
                log_output.append(e)

                # write stdout list to log file
                with open(stdout_lf, 'w') as fout:
                    for item in log_output:
                        fout.write(
                            str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S-%p")))
                        fout.write("%s\n" % e)

                # define exception error message
                error_msg = 'Error(s) Found'

                # print exception errr message
                print(f'{error_msg}:{e}')

    def mod_printer(self):
        """
        Create the printer definition specified in the printers.csv file
        """
        # stdout log file name for mod function
        stdout_lfn = 'mod_std_output'

        # stdout final log file
        stdout_lf = self.log_dir + '/' + stdout_lfn + \
            '_' + self.file_dt + self.log_format

        # Create an empty list for storing stdout log output
        log_output = []

        # Loop through the printers in dictionary.
        for printer in self.new_printers:
            printer_name = printer['Printer']
            printer_commtype = printer['CommType']
            printer_tcphost = printer['TcpHost']
            printer_tcprport = printer['TCPRPort']
            printer_location = printer['Location']
            printer_model = printer['Model']
            # Windows Command to be run with relevant parameters
            mod_prn_cmd = [r'C:/Program Files/LRS/VPSX EOM/bin/nvpscfg.exe', '-modify',
                           '-printer=' + printer_name, '-commtype=' + printer_commtype,
                           '-tcphost=' + printer_tcphost, '-tcprport=' + printer_tcprport,
                           '-location=' + printer_location]

            # Use a try statement to allow for execption checking.
            try:
                # run the subprocess call and specify stdout and stderr
                mod_prn_cmd_sp = subprocess.run(
                    mod_prn_cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL, text=True)

                # Assign stdout to a variable
                output = mod_prn_cmd_sp.stdout

                # Append the variable to a list
                log_output.append(output)

                # write stdout list to file by interating on the list
                # write stdout list to log file
                with open(stdout_lf, 'w') as fout:
                    for item in log_output:
                        fout.write(
                            str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S-%p")))
                        fout.write("%s\n" % item)
                print(output)

            # exception when error occurs
            except Exception as e:

                # append stdout to log_output list
                log_output.append(e)

                # write stdout list to log file
                with open(stdout_lf, 'w') as fout:
                    for item in log_output:
                        fout.write(
                            str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S-%p")))
                        fout.write("%s\n" % e)

                # define exception error message
                error_msg = 'Error(s) Found'

                # print exception errr message
                print(f'{error_msg}:{e}')