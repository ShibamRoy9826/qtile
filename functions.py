from variables import *
from subprocess import Popen,PIPE
from libqtile.lazy import lazy
from time import strftime ,sleep
from libqtile import qtile
# from libqtile.log_utils import logger

###### Modes ===========================================================================

@lazy.function
def shiftBar(event):
    with open(config_file, "r") as fl:
        config = load(fl)
    bar_pos = config["bar"]["bar_position"]
    if bar_pos == "top":
        config["bar"]["bar_position"] = "bottom"
    else:
        config["bar"]["bar_position"] = "top"
    with open(config_file,"w") as fl:
        dump(config,fl)
    qtile.restart()

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
    
def toggle_mute():
    run("pactl set-sink-mute @DEFAULT_SINK@ toggle",capture_output=False,shell=True)

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

@lazy.function
def randomWall(event):
    run("easyfeh -r && xdotool key ctrl+super+r",check=True,shell=True)

@lazy.function
def nextWall(event):
    run("easyfeh -n && xdotool key ctrl+super+r",check=True,shell=True)

@lazy.function
def prevWall(event):
    run("easyfeh -p && xdotool key ctrl+super+r",check=True,shell=True)

