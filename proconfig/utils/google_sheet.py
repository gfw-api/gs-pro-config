import gspread
import os
import sys
import logging
import json
import base64
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheet(object):

    def open_spreadsheet(sheet_name, custom_key=False):
        """
        Open the spreadsheet for read/update
        :param sheet_name: name of the google sheet
        :return: a gspread wks object that can be used to edit/update a given sheet
        """

        if custom_key:
            spreadsheet_key = custom_key
        else:
            spreadsheet_key = r'1KnJ8zujY0AxpbMpMO5FPdret6U_2ZzR68nN2RyvFex8'

        # Updated for oauth2client
        # http://gspread.readthedocs.org/en/latest/oauth2.html
        credentials = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet.json',
                                                                       ['https://spreadsheets.google.com/feeds'])

        gc = gspread.authorize(credentials)
        wks = gc.open_by_key(spreadsheet_key).worksheet(sheet_name)

        return wks


    def sheet_to_dict(sheet_name, tech_title):
        """
        Convert the spreadsheet to a dict with {layername: {colName: colVal, colName2: colVal}
        :param sheet_name: name of the google sheet
        :param tech title: the unique ID for features in spreadsheet
        :return: a dictionary representing the sheet
        """

        sheet_as_dict = {}
        wks = GoogleSheet.open_spreadsheet(sheet_name)
        gdoc_as_lists = wks.get_all_values()

        # Pull the header row from the Google doc
        header_row = gdoc_as_lists[0]

        # Iterate over the remaining data rows
        for dataRow in gdoc_as_lists[1:]:

            # Build a dictionary for each row with the column title
            # as the key and the value of that row as the value
            row_as_dict = {k: v for (k, v) in zip(header_row, dataRow)}

            # Grab the technical title (what we know the layer as)
            layer_name = row_as_dict['Technical Title']

            # Add that as a key to the larger outDict dictionary
            sheet_as_dict[layer_name] = {}

            # For the values in each row, add them to the row-level dictionary
            for key, value in row_as_dict.items():
                sheet_as_dict[layer_name][key] = value

        return sheet_as_dict[tech_title]
