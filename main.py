import discord
from discord.ext import commands
from get_weather import get_weather
import datetime
#import logging
import requests
from get_wiki   import get_wiki

# INITIALIZATION
TOKEN = ''
bot = commands.Bot(command_prefix='!', description="A True Gentleman Unmatched")
time = datetime.datetime.now()
hour = time.hour

# REMOVE DEFAULT HELP TEXT
bot.remove_command('help')


#####################################################
# LOGGING
#####################################################
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger('discord')
#logger.setLevel(logging.DEBUG)
#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)


@bot.event
async def on_ready():
    print('Successfully Logged in')
    print(bot.user.name)
    print(bot.user.id)
    print('----------------------')


@bot.command()
async def champ(*, champion: str):
    champion_lower = champion.lower()
    url = 'https://u.gg/lol/champions/'+champion_lower+'/build'
    r = requests.get(url)
    if r.status_code == 200:
        msg = 'Here you go, m\'lady'+'\n\n'+r.url
    else:
        msg = 'Please give a champion when you call this command.(e.g. !op.gg aatrox)'
    await bot.say(msg)


@bot.command(pass_context=True)
async def hello(ctx):
    if hour <= 12:
        msg = 'Good Morning, m\'lady. You, {0.author.mention} are incredibly beautiful.'.format(ctx.message)
    elif 18 > hour > 12:
        msg = 'Good Afternoon, m\'lady. You, {0.author.mention}  light up my life like no one else.'.format(ctx.message)
    else:
        msg = 'Good Evening, m\'lady. You, {0.author.mention} are a beautiful human.'.format(ctx.message)
    await bot.say(msg)


@bot.command(pass_context=True)
async def help(ctx):
    msg = 'Hello there m\'lady. Your smile is radiant today! Here is a list of current available commands: \n\n' \
          '```css\n' \
          '!champ [champion] : Receive some assistance with your runes and builds for a league champion\n\n' \
          '!hello : Say hello to Zachary\n\n' \
          '!help  : Receive this instructional text box\n\n'  \
          '!weather [city] : Be awed by some wonderful weather knowledge from the infamous weather man himself\n\n' \
          '!smartyzach : Become enlightened by Zach\'s true and endless intelligence\n\n```'
    await bot.say(msg)


@bot.command()
async def weather(*, city: str):
    report = get_weather(city)
    temp = report[1]
    humidity = report[2]

    await bot.say('Well so uhhh... if you lookie here..')


#@bot.command()
#async def smartyzach():

#@bot.command_not_found()
#async def !():
##    msg = 'Sorry, that command does not exist. Maddame, try using the !help command.'
#   await bot.say(msg)


bot.run(TOKEN)

