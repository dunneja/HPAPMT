#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Filename     : conf_files.py
# Author       : James Dunne <james.dunne1@gmail.com>
# License      : GPL-3.0
# Comment      : This file is part of HPAPMT.
# ----------------------------------------------------------------------------
import os.path
import configparser
from configparser import ConfigParser

class configfile():

    """
    A Class to represent a config file
    """

    def __init__(self, config_file):
        """
        Initialisation
        Define a config file variable.
        """

        self.config_file = config_file

    def check_conf(self):
        """
        Create a conf / ini file if one does not exist
        """
        # Check if the config_file exists.
        if (os.path.isfile(self.config_file)):
            print(f'\nFile {self.config_file} exists!\n')

        # If the config_file does not exist then create a template.
        elif (os.path.isfile(self.config_file)) == False:
            print(f'\nFile {self.config_file} does not exist!\n')
            # Create a config layout.
            config = ConfigParser()
            config.read(self.config_file)
            config.add_section('main')
            config.set('main', 'cfgusers', 'root')
            config.set('main', 'vpsx_api_port', '5501')
            config.set('main', 'nvpscfg_dir',
                       'C:/Program Files/LRS/VPSX EOM/bin/nvpscfg.exe')
            config.set('main', 'log_dir', './logs')

            # Write the config layout to an ini file.
            with open('config.ini', 'w') as f:
                config.write(f)
                print(f'Creating file {self.config_file} ...\n')

    def read_conf(self):
        """
        Read the conf / ini file
        """
        # Read the settings in the config file and assign to variables.
        # Check if the config_file exists.
        if (os.path.isfile(config_file)):
            # Read the config_file contents.
            config = configparser.ConfigParser()
            config.read(config_file)
            cfgusers = (config.get('main', 'cfgusers'))
            vpsx_api_port = (config.get('main', 'vpsx_api_port'))
            nvpscfg_location = (config.get('main', 'nvpscfg_dir'))

        # If the config_file does not exist then print a message.
        elif (os.path.isfile(config_file)) == False:
            print(
                f'\nFile {config_file} does not exist! Unable to read {config_file} ...\n')

    def check_csv(self):
        """
        Read the Printers.csv configuration file
        """
        # Read the settings in the config file and assign to variables.
        # Check if the config_file exists.
        if (os.path.isfile(self.config_file)):
            print(F'File {self.config_file} exists!')
            return(0)

        # If the config_file does not exist then print a message.
        elif (os.path.isfile(self.config_file)) == False:
            print(
                f'\nFile {self.config_file} does not exist! Unable to read file {self.config_file} ...\n')
            return(1)

    def check_log_dir():
        """
        check if the log dir exists
        """
        if (os.path.isdir('logs')):
            print(f'Log directory exists!')
        else:
            try:
                print("Log directory doesn't exist!\n")
                os.mkdir('logs')
                print('Sucessfully created the log directory.')
            except OSError:
                print('Creation of the directory failed.')