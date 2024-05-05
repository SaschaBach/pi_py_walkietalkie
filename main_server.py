import argparse  
import sys

from termcolor import colored
from myLogger import MyLogger
  
print("*****************************************************")       
print("               _ _    _      _        _ _    _       ")       
print("              | | |  (_)    | |      | | |  (_)      ")      
print("__      ____ _| | | ___  ___| |_ __ _| | | ___  ___  ")  
print("\ \ /\ / / _` | | |/ / |/ _ \ __/ _` | | |/ / |/ _ \ ")
print(" \ V  V / (_| | |   <| |  __/ || (_| | |   <| |  __/ ")
print("  \_/\_/ \__,_|_|_|\_\_|\___|\__\__,_|_|_|\_\_|\___| ")
print("*****************************************************")
print("                                                     ")
print("                                   |                 ")
print("      |                            |                 ")
print("      |                      .=====|                 ")
print("      |=====.                |.---.|                 ")
print("      |.---.|                ||=o=||                 ")
print("      ||=o=||                ||   ||                 ")
print("      ||   ||                ||   ||                 ")
print("      ||   ||                ||___||                 ")
print("      ||___||                |[:::]|                 ")
print("      |[:::]|                '-----'                 ")
print("      '-----'                                        ")
print("*****************************************************")                                        
print("       ####  ###### #####  #    # ###### #####       ")
print("      #      #      #    # #    # #      #    #      ")
print("       ####  #####  #    # #    # #####  #    #      ")
print("           # #      #####  #    # #      #####       ")
print("      #    # #      #   #   #  #  #      #   #       ")
print("       ####  ###### #    #   ##   ###### #    #      ")
print("*****************************************************")
print(colored("Press Ctrl-C to skip","red"))
print("*****************************************************")

# process cmd line args
parser = argparse.ArgumentParser(description='Start script for the walkie talkie server.')
parser.add_argument("--logLevel", type=str, default='INFO')
parser.add_argument("--dryMode", type=bool, default=False)
args = parser.parse_args()
logLevel = args.logLevel
dryMode = args.dryMode
print('Arg[logLevel]=%s' % logLevel )
print('Arg[dryMode]=%s' % dryMode )
print("************************************")

# init and create the first logger
MyLogger.level = logLevel
myLogger = MyLogger('main')

try:
 #   stop_event.wait()  # wait forever but without blocking KeyboardInterrupt exceptions
 print("************************************")

except KeyboardInterrupt:   
    myLogger.info("Ctrl+C pressed...")
#    stop_event.set()  # inform the child thread that it should exit
    sys.exit(1)