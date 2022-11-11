#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Filename     : csv_import.py
# Author       : James Dunne <james.dunne1@gmail.com>
# License      : GPL-3.0
# Comment      : This file is part of HPAPMT.
# ----------------------------------------------------------------------------
# Import modules
import csv

# Define csv import function.
def dictreaderimport(csv_input):
    """
    builds a dictionary from the csv specified
    and stores this in a list
    """
    csv_filename = csv_input

    try:

        with open(csv_filename, 'r') as csv_file:

            csv_dict = csv.DictReader(csv_file)

            csv_import = list(csv_dict)

        return csv_import

    except FileNotFoundError:

        msg = f'Error: Filename {csv_filename} does not exist.'

        print(msg)