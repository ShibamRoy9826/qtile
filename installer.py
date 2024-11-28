from subprocess import run
from os import getlogin, makedirs,  removedirs

username=getlogin()

print("""Welcome to Qt_Tile installer!
-------------------------------

Installation is is pretty simple, just answer a few questions in yes or no, and that's it! 
There's almost no bloat in the installer, you can deny to include anything that you don't want!
Incase you feel something is still bloat, raise an issue on the github repo.

When a question is asked, if you type 'exit' it aborts the installation.
You can also just press enter to keep the default
""")


def installPackage(pkgName,pkgUrl):
    run(["git","clone",pkgUrl],check=True)
    run(["cd",pkgName])
    run(["makepkg -si --noconfirm"])

def takeBackup(p):
    run(["mv",p,"~/.config/backup"])
def ask(msg):
    a=input(msg+ " (y/n): ")
    if a.lower()=="y" or a.lower()=="":
        print(f"Selected Yes.")
        return True
    elif a.lower()=="exit":
        print(f"Alright, aborting installation!")
        exit()
    elif a.lower()=="n":
        print(f"Selected No.")
        return False

    else:
        return ask("Please enter a valid input")
def askFloat(msg,default=None):
    a=input(msg+":")
    if a=="":
        return default
    try:
        res=float(a)
    except:
        return askFloat("Please enter a valid input (in decimals):")

    return res
def preInstall():
    global username
    
    makedirs("temp")
    makedirs(f"/home/{username}/.config/backup")

def postInstall():
    removedirs("temp")

def runInstall():
    pass

dependencies=["Iosevka Nerd Fonts","Papirus Icon Theme"]
toBeInstalled=[]

script_list = """
- A water reminder notification script
- Automatic nightlight script 
- A script to fetch music mp3's from youtube (requires youtube-dl) to be played using mpd
- A script to show notification on plugging charger
- A script to show nontification when any device is connected/disconnected
- Battery percentage alert scripts
"""

term=ask("Do you want to install and configure suckless terminal automatically?")
shell=ask("Do you want to install zsh, and zinit?")
easyfeh=ask("Do you want to install EasyFeh for color palette generation and wallpaper management?")
launcher=ask("Do you want to setup an app launcher(rofi)?")
powermenu=ask("Do you want to setup a powermenu(rofi)?")
extra_scripts=ask("Do you want to add extra scripts too? this list includes: \n"+script_list)
dunst=ask("Do you want to setup a notification daemon? (dunst)")
mpd=ask("Do you want to setup Music Player Daemon(MPD)?")
p10k=ask("Do you want to setup powerlevel 10k as your zsh theme?")
dropdown=ask("Do you want to setup scratchpads?")
recorder=ask("Do you want to install a screen recorder? (simplescreenrecorder)")
scrot=ask("Do you want to install scrot for taking screenshots?")
picom=ask("Do you want to install picom? it includes all the animations, blur, rounded corners and fancy stuff.. (pijulius fork)")
gestures=ask("Do you want to auto-setup touchpad gestures? (uses libinput-gestures)")
browser=ask("Do you want to install a browser?(zen-browser)")
flManager=ask("Do you want to install a file-manager?(thunar)")
gtkTheme=ask("Do you want to install a GTK theme? (colloid-catppuccin-gtk-theme-git)")


###### Extra questions

##$$$$$ MPD
if mpd:
    ncmpcpp=ask("Do you want to setup ncmpcpp for mpd?")
else:
    ncmpcpp=False

##$$$$$$ Terminal
if term==False:
    termname=input("Alright! What do you want to use as your terminal emulator then? (Type exact name please, I will look into the AUR): ")
else:
    termname="st"

##$$$$$$ Picom
if picom:
    print("Okay, you need to answer some additional questions then...")
    active_opacity=askFloat("What do you want to use as the ")

##$$$$$$ Browser
if browser:
    browsername="zen-browser"
else:
    browsername=input("Okay.. So is there any other browser that you would like to install? (Type exact name please, I will look into the AUR):")

##$$$$$$ File manager
if flManager:
    filemanager="thunar"
else:
    filemanager=input("Okay.. So is there any other file manager that you would like to install? (Type exact name please, I will look into the AUR):")

#### Calculating all packages

#### End of printing  questions
print("Cool, all's well, but there are a few things that are going to be installed as dependencies, not installing any of them can cause problems with other functions/features... Here's a list of them:")
for package in dependencies:
    print("  - ",package)

print("\nBesides, there's also a confirmation required, so these are the things which are going to be installed except for the ones mentioned above:")
for package in toBeInstalled:
    print("  - ",package)

confirm=ask("So... Are you alright with installation of all these packages?")

############### Starting/Aborting installation
if confirm:
    print("OkAy! StArTiNG tHe InStALlAtiOn rIgHt nOw!")
    preInstall()
    runInstall()
else:
    print(f"Alright, aborting installation!")
    exit()
