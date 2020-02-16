import base64
import discord, logging, os
import subprocess
import inspect

from discord.ext import commands

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

token = os.getenv("DISCORD_BOT_TOKEN")

client = discord.Client()
bot = commands.Bot(command_prefix="!")
bot.remove_command('help')

help_text = """
    ```
Jaskier:
==============================
!frappe
Return a frappe for you

!ls
Returns the contents of the home directory

!pwd
Returns the current directory

!viewcode <function>
Returns the code of the given function. Be careful with that one!
Available functions: decrypt, hmask, h_rotl, blockify, cnt, revenc, pwd, ls, frappe

!revenc <string>
Reverses an encrypted string
Example of reversing 'Hello World': !revenc SJVsbG9Ap2+yzGEA
```
"""
# ======= CRYPTO =======

BLOCK_SIZE = 2
TABLE_DIM = 4

def hmask(size, idx):
    return 2**size-1 << idx*size

def blockify(inpt, size, pad):
    return [inpt[i:i+size].ljust(size, pad) for i in range(0, len(inpt), size)]

def cnt(pt, size, idx):
    """
    Counts 0s,1s in a square table of bits
    """
    a,b = 0,0
    pt = pt >> idx * size
    for _ in range(size):
        if pt % 2 == 0: a+=1 
        else: b += 1
        pt = pt >> 1
    return a,b

def h_rotr(pt, rot, size, idx):
    """
    Horizontal right rotation used for encryption. Almost identical with left rotation
    but it won't be given to the participants so they have to figure it out.
    """
    m = hmask(size, idx)
    blk = pt & m
    rot = rot % size
    r = ((blk >> rot) | (blk << (size - rot)))  & m
    return pt ^ blk | r

def h_rotl(pt, rot, size, idx):
    """
    Horizontal left rotation.
    """
    m = hmask(size, idx)
    blk = pt & m
    rot = rot % size
    r = ((blk << rot) | (blk >> (size - rot)))  & m
    return pt ^ blk | r

def encrypt(pt):
    """
    Encrypt function. This won't be provided to the participants
    """
    enc = []
    blocks = blockify(pt, BLOCK_SIZE, b'\x00')
    for blk in blocks:
        blk_int = int.from_bytes(blk, byteorder='big')
        for n in range(TABLE_DIM):
            a,b = cnt(blk_int, TABLE_DIM, n)
            blk_int = h_rotr(blk_int, a, TABLE_DIM, b)
        enc.append(blk_int.to_bytes(BLOCK_SIZE, byteorder='big'))
    return b''.join(enc)

def decrypt(ct):
    """
    Decrypt function
    Global Vars:
    ------------
    BLOCK_SIZE = 2
    TABLE_DIM = 4
    """
    dec = []
    blocks = blockify(ct, BLOCK_SIZE, b'\x00')
    for blk in blocks:
        blk_int = int.from_bytes(blk, byteorder='big')
        for n in range(TABLE_DIM, -1, -1):
            a,b = cnt(blk_int, TABLE_DIM, n)
            blk_int = h_rotl(blk_int, a, TABLE_DIM, b)
        dec.append(blk_int.to_bytes(BLOCK_SIZE, byteorder='big'))
    return b''.join(dec).strip(b'\x00')

# ======================

@bot.event
async def on_ready():
    logger.info(('<' + bot.user.name) + ' Online>')
    logger.info(discord.__version__)

@bot.command()
async def help(ctx):
    await ctx.channel.send(help_text)

@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        await message.channel.send('Stop playing around.... Focus!')
        return
    if bot.user != message.author:
        if isinstance(message.channel, discord.DMChannel):
            await bot.process_commands(message)
        else:
            if message.content.startswith("!"):
                await message.channel.send('Shhhhh! This is a public channel! Try again in DM')

@bot.command()
async def frappe(ctx):
    await ctx.channel.send("On its way!")

@bot.command()
async def ls(ctx):
    files = ''
    for r,d,f in os.walk("/home/jaskier"):
        for file in f:
            files = files+'\n'+file
    await ctx.channel.send(f'`{files}`')

@bot.command()
async def pwd(ctx):
    await ctx.channel.send(f'`{os.getcwd()}`')

@bot.command()
async def revenc(ctx, params):
    try:
        dec_in = decrypt(base64.b64decode(params)).decode('utf-8')
        getResult =  subprocess.Popen(f'echo {dec_in} | rev', shell=True, stdout=subprocess.PIPE).stdout
        result =  getResult.read()
        await ctx.channel.send(result.decode())
    except Exception as e:
        print(e)
        await ctx.channel.send("Ops, something went wrong..")


@bot.command()
async def viewcode(ctx, param):
    if param in ["decrypt", "hmask", "h_rotl", "blockify", "cnt", "revenc", "pwd", "ls", "frappe"]:
        func = eval(param)
        if type(func) == commands.core.Command:
            await ctx.channel.send(f"```python\n{inspect.getsource(func._callback)}```")
        else:
            await ctx.channel.send(f"```python\n{inspect.getsource(func)}```")
    elif param == "encrypt":
        await ctx.channel.send("This is TOP secret! You ain't getting that....")

if __name__ == '__main__':
    bot.run(token)
