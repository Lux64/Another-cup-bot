import discord
from discord import client
client = discord.Client()

botenabled = False
phrase = 'cup'
prefix = 'cup '

def SetPrefix(x):
    global prefix
    prefix = x

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(ctx):
    global botenabled
    global phrase
    global prefix
    commandused = False
    if (ctx.author.name == 'Lux64'):
        if (ctx.author.discriminator == '4554'):
            if (ctx.content == f'{prefix}disable'):
                await ctx.channel.send('Bot disabled!')
                botenabled = False
                commandused = True
            if (botenabled == False):
                if (ctx.content == f'{prefix}enable'):
                    await ctx.channel.send('Bot enabled!')
                    botenabled = True
                    commandused = True
                if (ctx.content.startswith(f'{prefix}phrase ')):
                    if (len(ctx.content) < 8 + len(prefix)):
                        await ctx.channel.send('This phrase is invalid, please try another one.')
                        return
                    phrase = ctx.content[7 + len(prefix):len(ctx.content)]
                    await ctx.channel.send('Set phrase to ' + phrase)
                    commandused = True
                if (ctx.content.startswith(f'{prefix}prefix ')):
                    if (len(ctx.content) < 8 + len(prefix)):
                        await ctx.channel.send('This prefix is invalid, please try another one.')
                        return
                    if (ctx.content[len(ctx.content) - 3:len(ctx.content)] == 'Spc'):
                        prefix = ctx.content[7 + len(prefix):len(ctx.content) - 3]
                    else:
                        prefix = ctx.content[7 + len(prefix):len(ctx.content)]
                    await ctx.channel.send(f'Set prefix to `{prefix}`')
                    commandused = True
                if (ctx.content == f'{prefix}help'):
                    await ctx.channel.send(f'''List of commands

`{prefix}enable` - Enable the restriction
`{prefix}disable` - Disable the restriction
`{prefix}phrase <Your phrase here>` - Change the phrase to say (deafult = cup)
`{prefix}prefix <Your prefix here>` - Change the prefix of the bot (deafult = `cup `) (Due to discords limitations, to have a space at the end, type like this: `...your prefix Spc`)''')
                commandused = True

    if (commandused == False):
        if (botenabled == True):
            if (ctx.content != phrase):
                await ctx.delete()
            
client.run('token')