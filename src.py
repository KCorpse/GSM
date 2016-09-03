from takeinput import Input
from algo3 import Week
from buildoutput import Spreadsheet
from cleanlist import xlfriendly
import os


folder = '/home/kyle/Dropbox/lrn/flask/uploads'
startdate = '8/21/16'

def find_file(path):

    for file in os.listdir(path):
        if file.endswith('.xlsx'):
            return(file)


orig_xl = find_file(folder)


def create_schedule():

    database = Input(orig_xl)
    roughschedule = Week()
    tbwsched = xlfriendly(roughschedule.schedule2, orig_xl)
    Spreadsheet(orig_xl, startdate, roughschedule.schedule2)
