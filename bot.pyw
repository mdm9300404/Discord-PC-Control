from nextcord import Interaction
import nextcord
from nextcord.ext import commands
import os
import psutil

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

guildid = 99999999999999999 # Replace this with the server ID you put the bot in

@bot.event
async def on_ready():
    print("Bot is ready!")


# shutdown command
@bot.slash_command(name = "shutdown", description = "Shutdown your PC", guild_ids=[guildid])
async def shutdown(interaction: Interaction):
    await interaction.response.send_message("Shutting down PC... Goodbye!")
    os.system('shutdown -s -t 2') # Wait 2 seconds and shutdown
    await interaction.send("PC Shutdown successfully!")

# restart command
@bot.slash_command(name = "restart", description = "Restart your PC", guild_ids=[guildid])
async def restart(interaction: Interaction):
    await interaction.response.send_message("Restarting PC... Goodbye!")
    os.system('shutdown -r -t 2') # Restart the PC
    await interaction.send("PC Restarted successfully!")


# lock command
@bot.slash_command(name="lock", description="Lock your PC", guild_ids=[guildid])
async def lock(interaction: Interaction):
    await interaction.response.send_message("Locking PC...")
    os.system('rundll32.exe user32.dll,LockWorkStation') # Lock the PC
    await interaction.send("PC Locked Successfully!")


# Signout command
@bot.slash_command(name="signout", description="Sign out of your PC", guild_ids=[guildid])
async def signout(interaction: Interaction):
    await interaction.response.send_message("Signing out of PC...")
    os.system('shutdown -l') # Sign out of the PC
    await interaction.send("PC Signed Out Successfully!")


# Sleep command
@bot.slash_command(name="sleep", description="Put your PC to sleep", guild_ids=[guildid])
async def sleep(interaction: Interaction):
    await interaction.response.send_message("Putting PC to sleep...")
    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0') # Put the PC to sleep
    await interaction.send("PC put to sleep successfully!")


# Usage Command
@bot.slash_command(name="usage", description="Show usage of your PC", guild_ids=[guildid])
async def usage(interaction: Interaction):
    cpuusage = psutil.cpu_percent() # CPU Usage
    ramusagepercent = psutil.virtual_memory().percent # RAM %
    ramusageamount = psutil.virtual_memory().used # RAM usage
    ramusageamount = round(ramusageamount / 1000000000, 2) # Convert RAM usage from bytes to GB
    embed1 = nextcord.Embed(title="Usage", color=0x00ff00)
    embed1.add_field(name="CPU Usage", value=f"{cpuusage}%")
    embed1.add_field(name="RAM Usage", value=f"{ramusagepercent}%")
    embed1.add_field(name="RAM Used", value=str(ramusageamount) + " GB")
    await interaction.response.send_message(embed=embed1)
    

@bot.slash_command(name="status", description="Get the status of your PC", guild_ids=[guildid])
async def status(interaction: Interaction):
    await interaction.response.send_message("I'm online and signed in!")
    
bot.run("Put in your bot token here") # Replace this with your bot token. You can get one here: https://discord.com/developers/applications/
