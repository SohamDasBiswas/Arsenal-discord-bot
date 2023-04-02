import discord,requests, sys, webbrowser, bs4
from discord import colour
from discord.flags import Intents
from discord import channel
import pyjokes
import youtube_dl
import os
from dotenv import load_dotenv
import random
import ffmpeg
import urllib.request
import re
import lxml
from lxml import etree
from discord.ext import *
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from time import strftime
import datetime
players = {}
player = []
search_list=[]
client= commands.Bot(command_prefix="||")
intents = discord.Intents.default()
intents.members =True
# clients = discord.Client(intents=intents)
roast_texts=["Where’s your off button?",
"You’re so real. A real ass.",
"I’m not shy. I just don’t like you.",
"My poop is far better than your face",
"My hair straightener is hotter than you.",
"I have heels higher than your standards.",
"You have more faces than Mount Rushmore.",
"I’m jealous of people who don’t know you.",
"You’re entitled to your incorrect opinion.",
"I’m visualizing duck tape over your mouth.",
"You’re the reason I prefer animals to people.",
"If I had a face like yours, I’d sue my parents.",
"I’d smack you, but that would be animal abuse.",
"You sound reasonable… Time to up my medication.",
"Hey, I found your nose, it’s in my business again!",
"I might be crazy, but crazy is better than stupid.",
"My middle finger gets a boner every time I see you.",
"Is there an app I can download to make you disappear?",
"90% of your ‘beauty’ could be removed with a Kleenex.",
"The people who know me the least have the most to say.",
"I am allergic to stupidity, so I break out in sarcasm.",
"I didn’t change. I grew up. You should try it sometime.",
"My phone battery lasts longer than your relationships.",
"I’m sorry that my brutal honesty inconvenienced your ego.",
"Some people should use a glue stick instead of chapstick.",
"It’s scary to think people like you are allowed to vote.",
"I bet you're a magician that only knows one trick: Turning beer into domestic violence",
"Keep rolling your eyes. Maybe you’ll find your brain back there.",
"I suggest you do a little soul searching. You might just find one.",
"Oh you’re talking to me, I thought you only talked behind my back.",
"Maybe you should eat make-up so you’ll be pretty on the inside too.",
"Your face is fine but you have to put a bag over that personality.",
"I keep thinking you can’t get any dumber and you keep proving me wrong.",
"It’s so cute when you try to talk about things you don’t understand.",
"I’d explain it to you but I left my English-to-Dumbass Dictionary at home.",
"Why is it acceptable for you to be an idiot but not for me to point it out?",
"If you’re offended by my opinion, you should hear the ones I keep to myself.",
"Everyone brings happiness to a room. I do when I enter, you do when you leave.",
"I thought I had the flu, but then I realized your face makes me sick to my stomach.",
"When karma comes back to punch you in the face, I want to be there in case it needs help.",
"I’m not an astronomer but I am pretty sure the earth revolves around the sun and not you.",
"If you’re going to be a smart ass, first you have to be smart, otherwise you’re just an ass.",
"I am not ignoring you. I am simply giving you time to reflect on what an idiot you are being.",
"No, no. I am listening. It just takes me a moment to process so much stupid information all at once."]


@client.command()                                       #=============================================Hello
async def hello(ctx):
    await ctx.send(f"Hello @{ctx.author}")


@client.command()                                       #==========================================ArsenalJokes
async def arsenaljokes(ctx):
    joke= pyjokes.get_joke()
    await ctx.send(joke)


@client.event
async def on_ready():
    print('Bot online')
    print(client.user.name)
    print(client.user.id)
    print("---------------")

@client.event
async def on_member_join(member,ctx):
    embed= discord.Embed(title="Welcome",color=0x9208ea,description=f"{member.mention}, Joined \nWelcome to the server :partying_face")
    embed.set_footer(text="Devoloped by SDBDARKNINJA#7631")
    msg = await ctx.send(discord.object(id="769225766982123533"),embed=embed)


@client.command(pass_context=True)                      #===========================================Join
async def join(ctx):
    channel = ctx.author.voice.channel
    await ctx.send("***Joining   ***"+":mailbox_with_mail:")
    await channel.connect()


@client.command(pass_context=True)                      #===========================================Leave
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await ctx.send(":mailbox_with_no_mail:"+"***   Successfully disconnected***")
        await ctx.voice_client.disconnect()
    else:
        await ctx.send(":x:"+"***   The bot is not connected to Arsenal Voice Channel***")


@client.command()  #=========================================Play
async def play(ctx, search_keyword: str):
    queue_list=[]
    count=0
    def play_song():
      queue_list.append(search_keyword)
      voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
      voice.play(discord.FFmpegPCMAudio("song.mp3"))
    for count in range(len(queue_list)):
        search_song_url = urllib.request.urlopen(
            "https://www.youtube.com/results?search_query=" + str(queue_list[count]))
        video_ids = re.findall(r"watch\?v=(\S{11})",
                            search_song_url.read().decode())
        url = "https://www.youtube.com/watch?v=" + video_ids[0]
        str(url)
        youtube = etree.HTML(urllib.request.urlopen(url).read())
        video_title = youtube.xpath("/html/head/title")
        print(video_title[0].text)
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
                player.clear()
                queue_list.pop[0]

        except PermissionError:
            await ctx.send(
                "Wait for the current playing music end or use the 'stop' command..."
            )
            
        await ctx.send(
            "Getting everything ready, playing audio soon, depends on your internet speed..."
        )
        print("Someone wants to play music let me get that ready for them...")
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        await ctx.send("***Now Playing   ***" + ":notes:" + "   " +
                    video_title[0].text)
        await ctx.send(url)
        ydl_opts = {
            'format':
            'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, 'song.mp3')
        play_song()
        # voice.play(discord.FFmpegPCMAudio("song.mp3"))

        voice.volume = 90
        if len(queue_list)==0:
            break
        else:
            count += 1
            play()
        
    




@client.command()
async def tell_me_about_yourself(ctx):
    text = "***My name is Arsenal!\n I was built by SDB DarkNinja. At present I have limited features(find out more by typing ||help)\n :)***"
    await ctx.send(text)


@client.command()                                   #=================================================Pause
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send("***Paused   ***"+":pause_button:")
    else:
        await ctx.send(":x:"+"***   Currently no audio is playing***")


@client.command()                                   #===============================================Resume
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        await ctx.send("***Resuming   ***"+":play_pause:")
    else:
        await ctx.send(":x:"+"***   The audio is not Paused***")


@client.command()                                    #===============================================Stop
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("***Stopped   ***"+":stop_button:")


@client.command()                                    #===============================================Introduce
async def introduce(ctx):
    await ctx.send(f"***Hello sir, @{ctx.author}, I am a robot assistant of your's, you can tell me anything so I can execute that for you, sir***")


@client.command()                                    #===============================================SourceCode
async def sourcecode(ctx):
    await ctx.send("https://github.com/SohamDasBiswas/Arsenal-discord-bot")


# @client.command()
# async def reminder(ctx, time1:str, text):
#     await ctx.send("Reminder set successfully!!")
     
#     if time1 == strftime('%I:%M%p'):
#         await ctx.send(strftime('%I:%M%p') + text)


@client.command()                                    #=======================================Roast
async def roast(ctx):
    random_roast= random.choice(roast_texts)
    await ctx.send(random_roast)


@client.command(help = "Prints details of Server")   #========================================Helpme
async def helpme(ctx):
    owner=str(ctx.guild.owner)
    region = str(ctx.guild.region)
    guild_id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    desc=ctx.guild.description
    
    embed = discord.Embed(
        title=ctx.guild.name + " Server Information",
        description=desc,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed= discord.Embed(title="Commands",discription="Some useful commands")
    embed.add_field(name="||hello", value="Bot Send's you Hello",inline=True)
    embed.add_field(name="||helpme", value="Bot Send's you Commands list and its uses",inline=True)
    embed.add_field(name="||sourcecode", value="Bot will send source code",inline=True)
    embed.add_field(name="||introduce", value="Bot Will introduce itself",inline=True)
    embed.add_field(name="||arsenaljokes", value="Bot Send's you a Funny Joke",inline=True)
    embed.add_field(name="||roast @", value="Bot will roast",inline=True)
    embed.add_field(name="||join", value="Bot will join the arsenal voice channel",inline=True)
    embed.add_field(name="||leave", value="Bot will disconnect the arsenal voice channel",inline=True)
    embed.add_field(name="||play [song name]", value="Bot will play that song on the arsenal voice channel",inline=True)
    embed.add_field(name="||pause", value="Bot will pause that song on the arsenal voice channel",inline=True)
    embed.add_field(name="||resume", value="Bot will resume that song on the arsenal voice channel",inline=True)
    await ctx.send(content=None, embed= embed)
    members=[]
    async for member in ctx.guild.fetch_members(limit=150) :
        await ctx.send('Name : {}\t Status : {}\n Joined at {}'.format(member.display_name,str(member.status),str(member.joined_at)))


load_dotenv()

client.run(os.getenv("TOKEN"))