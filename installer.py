# Please report any bugs for this installer to me

import time
import webbrowser
import os
import subprocess
import sys
import pickle
import shutil
import traceback as tb
os.system('cls')
os.system('title  PC Control Bot Installer')
try:
    print("Thanks for installing PC Control Bot! Let's get some things setup...")
    time.sleep(5)

    # Initialize the instructions as a list and a variable
    introtext = ["First, open Discord on your computer. Next to the mute and deafen icons, click the settings icon. Under \"APP SETTINGS\", click \"Advanced\". Then, turn on developer mode.", "Once developer mode is enabled, create a new Discord server. Do not let anyone else in this server, or they will be able to control your PC too!", "Once you've created the server, right-click the server icon on the left-hand panel and click \"Copy ID\""]

    createbottext = ["Now that you're at the developer portal, click \"New Application\" at the top and give it a name.", "On the left panel, click \"Bot\". Then, press \"Add Bot\". Lastly, press \"Yes, do it!\" and give your new Discord bot any name you'd like.", "Scroll down and find \"Public Bot\". Disable this option.", "On the left panel, click \"OAuth2\", then click \"URL Generator\"", "Select and enable the options \"Bot\" and \"applications.commands\"", "Scroll down and find \"Bot Permissions\". Select the option \"Administrator\"", "Copy the generated URL at the bottom, visit that url in a new tab, and add the bot to the server you just created", "Go back to the developer portal, and press \"Bot\" once again on the left-hand panel. Press \"Reset Token\", then press \"Yes, do it!\". Put in your 2FA code if required.", "Next to the token, press \"Copy\""]

    # Loop through introtext, and wait for the user to press ENTER before moving on to the next step
    for item in introtext:
        os.system('cls')
        print("Thanks for installing PC Control Bot! Let's get some things setup...")
        print("\n" + item + "\n")
        input("When done with this step, press ENTER to continue...")

    guildid = input("\nEnter the server ID you just copied here: ")

    # Check if the server ID is valid. If not, ask the user to try again and exit in 10 seconds.
    try:
        guildid = int(guildid)
    except:
        print("\n\nYour server ID contains some characters that aren't numbers, or the server ID is empty. Please try again.")
        time.sleep(10)
        exit()
    os.system('cls')
    print("Great! Now let's create a Discord bot and get its token. I will open Discord's Developer Portal in your default browser now...\nOnce the page loads, come back to this window.")
    time.sleep(5)
    webbrowser.open("https://discord.com/developers/applications", new=2)

    # Loop through createbottext, and wait for the user to press ENTER before moving on to the next step
    for item in createbottext:
        os.system('cls')
        print("Great! Now let's create a Discord bot and get its token. I will open Discord's Developer Portal in your default browser now...\nOnce the page loads, come back to this window.")
        print("\n" + item + "\n")
        input("When done with this step, press ENTER to continue...")

    bottoken = input("\nEnter the bot token you just copied here: ")

    # Remove any spaces from the bot token to prevent errors.
    bottoken = bottoken.replace(" ", "")


    print("\nI will now install a .pickle file (Needed for storing data such as your bot token) in " + str(os.path.expanduser(r"~\Documents")))
    answer1 = input("\nIs this okay?: ")
    answer1 = answer1.lower() # Make answer lowercase to prevent any unintended behavior
    # Yes to ok
    if answer1 == "y" or answer1 == "yes":
        print("\nInstalling pickle file...")
        dict1 = {'guildid': guildid, 'bottoken': bottoken} # Create a dictionary to store the data
        os.mkdir(os.path.expanduser(r"~\Documents\PC Control Bot")) # Create a folder called "PC Control Bot" in the user's Documents folder
        picklefile = open(os.path.expanduser(r"~\Documents\PC Control Bot\PC Control Bot.pickle"), "wb")
        pickle.dump(dict1, picklefile) # Write dictionary to newly created pickle file
        picklefile.close()
        print("\nPickle file installed!")
    # No to ok
    elif answer1 == "n" or answer1 == "no":
        print("\nCancelling installation...")
        time.sleep(5)
    # Not Recognized to ok
    else:
        print("\nAnswer not recognized as 'y', 'yes', 'n', or 'no'. Please try again.")
        time.sleep(10)
        exit()


    print("\nInstalling dependencies...\n")
    time.sleep(5)
    # Installs dependencies via pip (Does not create a virtual environment)
    subprocess.call([sys.executable, "-m", "pip", "install", "nextcord==2.0.0a10"])
    subprocess.call([sys.executable, "-m", "pip", "install", "psutil==5.9.0"])
    print("\nDependencies installed!")


    print("\nMoving PC Control Bot.py into the startup folder...")
    # Copy bot file to Windows startup folder
    startupfolder = os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup") # Save the startup folder path to a variable
    shutil.copy2("bot.pyw", str(startupfolder)) # Copy the bot file to the startup folder

    restartyesno = input("\nThe bot has been successfully installed! Do you want to restart your computer now? (y/n): ")
    restartyesno.lower() # Make answer lowercase to prevent any unintended behavior
    # Yes to restart
    if answer1 == "y" or answer1 == "yes":
        print("\nRestarting computer in 5 seconds...")
        time.sleep(5)
        os.system('shutdown -r -t 0') # Restart the PC instantly
    # No or unknown to restart
    else:
        print("\nOk, feel free to keep using your PC! This window will automatically close in 10 seconds...")
        time.sleep(10)
        exit() # Kill window
except Exception as e:
    tbreason = ''.join(tb.format_exception(None, e, e.__traceback__))
    print(tbreason)
    time.sleep(15)