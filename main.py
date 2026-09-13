import discord
from discord.ext import commands 

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents) 

@bot.event
async def on_ready():
print(f'Logged in as {bot.user.name}') 

@bot.command()
async def ticket(ctx):
await ctx.send("Ticket system is active! Click below to create a ticket.") 


bot.run("MTU0NTYyODI5NDcyMzAxODgzMg.GicVJ1.S1KwqJJEfGjOz5OHu8Tt69-0JATtE2PzHSabzA")
