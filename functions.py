from variables import *
from subprocess import Popen,PIPE
from libqtile.lazy import lazy
from time import strftime 
from libqtile import qtile

###### Modes ===========================================================================


@lazy.function
def takeScreenshot(event,select=False):
    scrDir=config["screenshot"]["screenshot_directory"]
    filename=strftime(config["screenshot"]["screenshot_format"])
    filepath=path.join(scrDir,filename)
    scr_cmd=config["screenshot"]["screenshot_command"].replace(":f:",filepath)
    scr_cp_cmd=config["screenshot"]["screenshot_copy_command"].replace(":f:",filepath)
    scr_cp_cmdSelect=config["screenshot"]["screenshot_copy_command_select"].replace(":f:",filepath)
    scr_cmdSelect=config["screenshot"]["screenshot_command_select"].replace(":f:",filepath)
    
    if select:
        run(scr_cmdSelect,shell=True,capture_output=False)
        run(scr_cp_cmdSelect,shell=True,capture_output=False)
    else:
        run(scr_cmd,shell=True,capture_output=False)
        run(scr_cp_cmd,shell=True,capture_output=False)

    if config["screenshot"]["screenshot_notification"]:
        heading=config["screenshot"]["screenshot_title"].replace(":f:",filepath)
        message=config["screenshot"]["screenshot_message"].replace(":f:",filepath)
        run(f"notify-send '{heading}' '{message}'",shell=True,capture_output=False)
    
def search():
    qtile.cmd_spawn("rofi -show drun")


def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/powermenu.sh")

def toggle_mute():
    run(["amixer", "-D", "pulse", "sset", "Master", "toggle"])

def update_memory():
    try:
        # Run the 'free -m' command to get memory usage in megabytes
        process = Popen(["free", "-m"], stdout=PIPE)
        output, _ = process.communicate()
        output_lines = output.decode().splitlines()
        used = output_lines[1].split()[2]
        return f"{used}"
    except Exception as e:
        return f"Error: {str(e)}"
