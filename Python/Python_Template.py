#!C:\Users\e1055168\Anaconda3\python.exe
import faker
import sys, os
import inspect
from dumper import dump

#This sets the paths of the homebrewed libraries
#When using it in vscode, you also have to update the path by shift+ctrl+p and search for Preference: Open Workspace Settings 
# sets the python to use and the custom library location
"""	
    "settings": {
		"python.condaPath": "C:\\Users\\e1055168\\Anaconda3\\python.exe",
		"python.analysis.extraPaths": [
			"C:\\Users\\e1055168\\OneDrive - FIS\\Desktop\\FIS\\tools\\github\\Python-Practice\\Python-Practice\\Mel\\MyScripts\\Python\\learning"
		]
"""  
#sys.path.append("/app/lab/lib/")
sys.path.append("C:\\Users\\e1055168\\OneDrive - FIS\\Desktop\\FIS\\tools\\github\\Python-Practice\\Python-Practice\\Mel\\MyScripts\\Python\\learning")

# homebrew libraries and function import
from ToolSet import HomeTools

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
    dump(args)

args = getOpt()
main(args)
fake = faker.Faker()
print(inspect.getsource(fake))