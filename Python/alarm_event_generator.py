#!C:\Users\e1055168\Anaconda3\python.exe

import sys, os
#import inspect #https://www.tutorialspoint.com/How-to-retrieve-source-code-from-Python-objects#:~:text=We%20use%20the%20getsource(),source%20code%20of%20the%20function.&text=Returns%20the%20text%20of%20the,%2C%20frame%2C%20or%20code%20object.
from dumper import dump

#This sets the paths of the homebrewed libraries
#When using it in vscode, you also have to update the path by shift+ctrl+p and search for Preference: Open Workspace Settings 
# sets the python to use and the custom library location
"""	
    "settings": {
		"python.condaPath": "C:\\Users\\USER\\Anaconda3\\python.exe",
		"python.analysis.extraPaths": [
			"C:\\Users\\USER\\OneDrive - COMPANY\\Desktop\\FIS\\tools\\github\\Python-Practice\\Python-Practice\\Mel\\MyScripts\\Python\\learning"
		]
"""  
#sys.path.append("/app/lab/lib/")
sys.path.append("C:\\Users\\USER\\OneDrive - COMPANY\\Desktop\\FIS\\tools\\github\\Python-Practice\\Python-Practice\\Mel\\MyScripts\\Python\\learning")

# homebrew libraries and function import
from ToolSet import HomeTools
import Tools_Alarm_Event_Composer as TAEC

# global variable
HT      = HomeTools()
debug   = 0

def getOpt():
    # This part of the code controls the flag attributes you can provide to run
    #   the code.
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-d", "--debug", type=int,
                        help="Controls how verbose the print out.", required=True)
    #parser.add_argument("-i", "--input_file", type=str,
    #                    help="This is the file to do the accounting to.")
    #parser.add_argument("-o", "--output_file", type=str,
    #                    help="This is the file that will be create w sum")
    args = parser.parse_args()

    #if args.debug is None:
    #    usage()
    #    HT.DEBUG_PRINT(debug, 0, "requires blah blah blah")
    #    exit()

    return args

def usage():

    title   = os.path.basename(__file__)
    version = HT.get_version_w_date(version="1.0.0")
    author  = "Melware"
    desc    = "This script will simulate data coming from our tools\n" + \
              "\t\t\tSpectrum\n" + \
              "\t\t\tNetcool (coming soon)\n" + \
              "\t\t\tFor help with arguments just provide --help as a single argument."

    HT.HowToUse(desc, title, author, version)
   
def main(args):
    HT.clear()
    HT.DEBUG_PRINT(debug, 0, "Starting Process")
    #dump(args)
    spectrum = TAEC.Spectrum()
    spectrum.set_alarm_key()
    spectrum.set_created_date()
    spectrum.set_alarm_details()
    spectrum.set_contact_person()
    spectrum.set_device_model_handle()
    spectrum.set_topology_model_name_string()
    spectrum.set_landscape_model_handle()
    spectrum.set_last_occurance_date()
    spectrum.set_model_types()
    spectrum.set_generic()
    print (vars(spectrum))

args = getOpt()
main(args)
