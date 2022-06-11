The installation instructions look like a lot to read/do, but that's because I explain things in extreme detail. In reality, most people won't need this amount of detail and ***you'll be able to get your bot up-and-runnning in just 5 minutes or less!***

# Manual Installation Instructions:

* 1: Download and install Python 3.10.5 from here: https://www.python.org/downloads/release/python-3105/ (Download the "Windows installer (64-bit)")

* 2: Run the installer. ***Make sure the checkbox "Add Python 3.10.5 to PATH" is checked and that you install pip***

* 3: Open Command Prompt or Powershell, and type "pip". If it works, type "pip install nextcord==2.0.0a10" and wait until it completes. Next, type "pip install psutil==5.9.0" and wait until it completes.

* 4: Press the green "Code" button at the top of this page and press "Download ZIP". Extract the .ZIP file.

* 5: Create a new Discord server, with you being the only member. If you let other members in this server, they will be able to control your PC too!

* 6: Go to https://discord.com/developers/applications/ | Sign in (if required), and press "New Application" at the top. Give it any name you'd like.

* 7: On the left panel, click "Bot". Then, press "Add Bot", and then press "Yes, do it!". Give the bot any name you'd like

* 8: On the bot page, make sure all three Privileged Gateway Intents are enabled ("Presence Intent", "Server Members Intent", and "Message Content Intent") Next, disable the option "Public Bot"

* 9: On the left panel, click "OAuth2", then, click "URL Generator". Select the options "Bot" and "applications.commands". Scroll down and find "Bot Permissions". Select the option "Administrator". Then, copy the generated URL and visit that website you just copied. Once you're at the website, sign-in with Discord (if needed) and add the bot to the server you just created.

* 10: Open Discord. At the bottom, next to the mute and deafen icons, click the settings icon. Click "Advanced", which is under "App Settings". Enable Developer Mode if it isn't already.

* 11: Go back to the bot page, where you enabled all the Privileged Gateway Intents. Press "Reset Token", then press "Yes, do it!. If 2FA is enabled, put in your 2FA code. Press the "Copy" button or select everything and copy it to your clipboard.

* 12: Open the folder you extracted earlier. Right-click the .pyw file, and click "Edit with IDLE". If you do ***not*** see that option, move on to step #14. If you ***do*** see that option, move on to step #13

* 13: If you opened the file with IDLE, find the very last line of code where it says "bot.run()" and paste the bot token in those quotes, replacing the old text. Then, open Discord. Right-Click the server you just created, and press "Copy ID" at the bottom. Open the IDLE again. Replace that number where it says "guildid = " with the ID you just copied. Do not confuse this with "guild_ids=[]" Do not add quotation marks. At the top of the IDLE, press "File", then press "save". Move on to step #15

* 14: On Windows 10, at the top of file explorer, click "View". Then, check the box that says "File name extensions" on the right. Right-click the .pyw file, and rename the end from ".pyw" to ".txt". Open the .txt file in notepad. Find the very last line of code where it says "bot.run()" and paste the bot token in those quotes, replacing the old text. Then, open Discord. Right-Click the server you just created, and press "Copy ID" at the bottom. Open the TXT file again. Replace that number where it says "guildid = " with the ID you just copied. Do not confuse this with "guild_ids=[]" Do not add quotation marks. At the top of notepad, press "File", then press "Save". Close notepad, and rename the end of the file once more, replacing ".txt" with ".pyw". Move on to step #15

* 15: Press the Windows Key and the letter "R" at the same time. When the run dialog appears, type "shell:startup" and press "OK". Copy the .pyw file into the folder that appears.

* 16: Restart your PC and your bot should be online! You can now begin using slash commands to control your PC.
