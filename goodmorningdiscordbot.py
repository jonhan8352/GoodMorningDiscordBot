import discord
from discord.ext import commands
import schedule
import time

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

def send_good_morning():
    channel = bot.get_channel(channel_id) #Replace channel_id with the id of the channel you want to send the message to
    await channel.send("Good morning! ☀️")

@bot.command(name='schedule_good_morning')
async def schedule_good_morning(ctx):
    schedule.every().day.at("8:00").do(send_good_morning)
    await ctx.send("Scheduled Good morning message to be sent at 8:00 am every day.")

bot.run('YOUR_BOT_TOKEN')