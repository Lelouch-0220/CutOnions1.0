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

#when bot is added onto a server
@client.command()
async def on_guild_join(guild: discord.Guild):
    for channels in guild.text_channels:
        if channels.permissions_for(guild.me).send_messages:
            await channels.send("To view my commands type ~h")

#roast    
@client.command()
async def roast(ctx):
    roasted = random.choice(L4)
    await ctx.send(roasted)


#when a person joins
@client.event
async def on_member_join(member):
    intro = random.choice(L3)
    await client.get_channel(848532288697794642).send(f"{member.mention} " + intro) 
    await client.get_channel(848532288697794642).send("To view my commands, type ~h")

@client.event
async def on_member_join(member):
    intro = random.choice(L3)
    await client.get_channel(826284371119046669).send(f"{member.mention} " + intro) 
    await client.get_channel(826284371119046669).send("To view my commands, type ~h")
    
#dice roll
@client.command()
async def roll(ctx, dice: str):
    """Rolls a dice in ndN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in ndN!' + '\nwhere n is number of rolls, and N is number of sides on the die')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

#8ball
@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    responses = [ "Certainly", "Probably yeah", "Yes, definitely....maybe","You may rely on it", "As I see it, yes", "Likely", "Eh",
    "Yes", "Signs point to yes", "Sure dude", "Lmao yeah","Lmao no", "Bruh yeah", "Bruh no","Sure dude", "Tf is that supposed to mean", "My sources say no", "mmmm no", "Very Doubtful"]
    ball = random.choice(responses)
    await ctx.send(ball)

@client.command(pass_context = True,aliases=['h'])
async def helpme(ctx):
    emb = discord.Embed(colour = discord.Colour.dark_orange())
    emb.set_author(name = "Help")
    emb.set_author(name = "~roast", value= "Roasts you")
    emb.add_field(name = "~greet", value = "Replies with a greeting response",inline = False)
    emb.add_field(name = "~helpme/~h", value = "Lists out the different commands for the bot",inline = False)
    emb.add_field(name = "~8ball *question*", value = "Input ~8ball followed by a question to call upon the questionable fortune telling skills of CutOnion",inline = False)
    emb.add_field(name = "~rps *your move*", value = "Input ~rps followed by either one of rock,paper or scissors to play Rock, Paper and Scissors",inline = False)
    emb.add_field(name = "~pickup", value = "Input ~pickup to have the Bot throw a cringey pickup line at you",inline = False)
    emb.add_field(name = "~nick @user nickname", value = "Input ~nick followed by the usertag followed by the nickname you want to change it to\n~nick @john dumbass changes @john's nickname to dumbass",inline = False)
    emb.add_field(name = "~clear *number*", value = "Clears prior number of message corresponding to the number entered after ~clear",inline = False)
    emb.add_field(name = "~roll *ndN*", value = "Input ~roll followed by ndN to roll a die where n is the number of rolls and N is the number of sides to the die\n 1d4 will roll a 4 sided die once",inline = False)
    await ctx.send(embed=emb)

#run
client.run("xxx")
