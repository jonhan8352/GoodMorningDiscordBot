# GoodMorningDiscordBot

We are going to create a Discord bot which it will send message to the channel in Discord Server during specific time. First we need to install Discord, Schedule and Time library into our Python script.

```
import discord
from discord.ext import commands
import schedule
import time
```

Let's say we also need to verify whether the Discord bot successfully executed we need we can add following line in the code.

```
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
```

Let's say we want the Discord bot to send "Good Morning!☀️" message everyday on 08:00 (8:00pm) at specific channel only in our Discord server.

```
def send_good_morning():
    channel = bot.get_channel(channel_id) #Replace channel_id with the id of the channel you want to send the message to
    await channel.send("Good morning!☀️")

@bot.command(name='schedule_good_morning')
async def schedule_good_morning(ctx):
    schedule.every().day.at("8:00").do(send_good_morning)
    await ctx.send("Scheduled Good morning message to be sent at 8:00 am every day.")
```

And finally at the end of the Python script, please add the Discord bot token in order for the Python script to verify the Discord bot's token.

```
bot.run('YOUR_BOT_TOKEN')
```
