import discord
from discord.ext import commands, tasks
import random
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='-', intents= intents)

L1 = ['rock','paper','scissors']
L2 = ['I think you’re my compiler. My life wouldn’t start without you.','Hey baby, wanna go do some PUSHing and POPing...',
'Give me your Twitter? My father said that I must follow my dream.','Do you believe in love at first sight, or should I walk past you again?',
'Do you like raisins? How do you feel about a date?','Hi, I’m writing a phonebook. Can I have your number?'
,'Hey, tie your shoes. I don’t want you falling for anyone else.','You make my floppy disk turn into a hard drive',
'Are you going to kiss me, or am I going to have to lie to my diary?',
'Ill show you my source code.','You are orienting my objects.','// TODO: You']
L3 = ['What’s kicking, little chicken?','I come in peace! Chow chow.','I am Batman. Who are you, gorgeous?','Hiiiii, baaaaaby!']
@client.event
async def on_ready():
    print("bot is ready")


@client.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def nick(ctx, member: discord.Member, name: str):
    perms = ctx.channel.permissions_for(ctx.author)
    if perms.manage_nicknames:
        await member.edit(nick=name)
    else: 
        await ctx.send("Don't have permissions")

@client.command()
async def rps(ctx, option):
    if option not in L1:
        await ctx.send("Invalid")
    else: 
        await ctx.send(f"You chose {option}")
        comp_choice = random.choice(L1)
        await ctx.send(f"Bot chose {comp_choice}")
        if comp_choice==option:
            await ctx.send("Tie")
        elif comp_choice=='paper' and option=='scissors':
            await ctx.send("You win")
        elif comp_choice=='paper' and option=='rock':
            await ctx.send("Bot wins")
        elif comp_choice=='scissors' and option=='rock':
            await ctx.send("You win")
        elif comp_choice=='scissors' and option=='paper':
            await ctx.send("Bot wins")
        elif comp_choice=='rock' and option=='paper':
            await ctx.send("You win")
        elif comp_choice=='rock' and option=='scissors':
            await ctx.send("Bot wins")
    
@client.command()
async def pickup(ctx):
    pickup = random.choice(L2)
    await ctx.send(pickup) 

@client.command()
async def greet(ctx):
    greet = random.choice(L3)
    await ctx.send(greet + f'{ctx.author.mention}')

@client.event
async def on_member_join(member):
    intro = random.choice(L3)
    await client.get_channel(848532288697794642).send(f"{member.mention} " + intro) 

@client.event
async def on_member_remove(member):
    await client.get_channel(848532288697794642).send("Nobody wanted you here anyways")



client.run("ODQ4NTIxMzg3MTIzMDE1NzQx.YLN1Hw.7lVMbkOCjHAblJb2KePDa_QMzG8")