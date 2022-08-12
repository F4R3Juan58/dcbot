import discord
from discord.ext import commands

servers = "D1 - 304 - 357 - 284 - 683 - 956 - 1264"

island = "steam://connect/85.190.148.207:27015"
gentwo = "steam://connect/37.10.126.191:27021"
genone = "steam://connect/85.190.155.154:27017"
thecenter = "steam://connect/85.190.152.139:27017"
abbone = "steam://connect/37.10.124.122:27017"
abbtwo = "steam://connect/37.10.124.117:27017"
fjordur = "steam://connect/31.214.205.38:27025"

servergrief = "d16"
#### BOT COMMANDS ####

bot = commands.Bot(command_prefix='+')

#### Bot Events ####
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Game(name="+help"))
   print('Logged in as')
   print('------')

@bot.command()
async def ourservers(ctx):
    await ctx.send(servers)

@bot.command()
async def serverlink(ctx):
    await ctx.send("D1 " + island)
    await ctx.send("956 " + gentwo)
    await ctx.send("683 " + genone)
    await ctx.send("357 " + thecenter)
    await ctx.send("304 " + abbone)
    await ctx.send("284 " + abbtwo)
    await ctx.send("1264 " + fjordur)

@bot.command()
async def dng(ctx):
    await ctx.send("""BLDX: 𝙧95 / 237 / 362 / 412 / 673 (temp) / 899 
Angry Girls: 249 / 298 / 359 / 666 / 668 
Chemb B: 179 305 380 793 908 
TPG: D2-57-88-292-566-950
Wizard Team : 677
B&G : 58, 93, 233, 290, 361, 417, 947,402
Updated 24-07-2022 """)

@bot.command()
async def joinsim(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/931687158534778910/1004559220340965436/TurtleSim_2.exe")

@bot.command()
async def grief(ctx):
    await ctx.send(servergrief)

@bot.command()
async def breed(ctx):
    await ctx.send("https://discord.gg/uQa8wyjbNv")

@bot.command()
async def ally(ctx):
    await ctx.send("https://discord.gg/Htvn8bb7nq")

@bot.command()
async def eos(ctx):
    await ctx.send("https://discord.gg/QXGPaYuYmW")

bot.run("MTAwNzQ4Njc0NjU0MTQzMjg3Mg.GGfmzM.O6sAi_qHSKs8WeqP9OV_Dd4i9TsTDZI4kbWXhc")