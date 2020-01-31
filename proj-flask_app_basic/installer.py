
import subprocess
from pathlib import Path
from basicapp.controllers.file_manager import FileManager

########################################
### Check if prompt toolkit is installed
########################################
prompt = None
WordCompleter = None
try:
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter
except:
    ans = input(">>>> Prompt toolkit is not installed should we pip install it? ([y]/n): ")

    if ans == 'n':
        exit("---- Goodbye! ----")
    else:
        subprocess.run(["pip", "install", "prompt_toolkit"])  # doesn't capture output

########################################
### Setup some variables
########################################
yes_no_completer = WordCompleter(['y', 'n'])

########################################
### Choose Action path
########################################
setup_opt_completer = WordCompleter(['install', 'uninstall'])
text = prompt('>>>> How can we help you? (tab): ', completer=setup_opt_completer)


########################################
### PATH: Install
########################################
if text == "install":

    ### install the basic app package ###
    file_manager = FileManager()
    text = prompt(f'>>>> basicapp local files location ok? @{str(file_manager.storage_path)}\n>>>> (y/[n]): ', completer=yes_no_completer)
    if text == "n":
        exit("---------- goodbye ----------")
    
    
    subprocess.run(["pip", "install", "-e", "."])

    ### setup system files ###
    file_manager.install()

    print("---------- basicapp successfully installed ----------")
            

########################################
### PATH: uninstall
########################################
if text == "uninstall": 
    try:
        file_manager = FileManager()
        text = prompt(f'>>>> uninstall basicapp? files at ({file_manager.storage_path}) will be deleted (y/[n]): ', completer=yes_no_completer)

        if text == 'y':
            file_manager.uninstall()

        subprocess.run(["pip", "uninstall", "BasicApp"])
        
        print("---------- basicapp successfully uninstalled ----------")

    except Exception as error:
        print("---------- error uninstalling basicapp ----------")
        print(f">>> ERROR: {error}")
    