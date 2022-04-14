import os
import discord
import random
from discord_slash import SlashCommand
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix="s!")
slash = SlashCommand(client, sync_commands=True)
@client.event
async def on_connect():
    await client.change_presence(activity=discord.Game(name='s!help'))
    print("Scythe Bot is online.")
  # Connect
client.remove_command("help")
  # Removing the default 'help' command, so that we can make our own
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")
    # s!ping command
@client.command()
async def invite(ctx):
    await ctx.send(
        "**Here's the invite:** *https://discord.com/api/oauth2/authorize?client_id=961289249993424996&permissions=8&scope=bot*. Enjoy!"
    )


    # s!invite command
@client.command()
async def say(ctx, *, text):
    await ctx.channel.purge(limit=1)
    await ctx.send(text)


    # s!say command
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Scythe Bot Commands",
                          description=("""**s!ping** | Pings the bot.
                    **s!help** | Shows all the Scythe Bot commands.
                    **s!members** | Shows member count.
                    **s!say** | Makes the bot say what you said, use it in the format: `s!say {query}`.
                    **s!ban** | Bans member, use it in the format: `s!ban {member}` - Requires Admin or higher.
                    **s!warn** | Warns member, use it in the format: `s!warn {member}` - Requires Trainee or higher.
                    **s!mute** | Mutes member, use it in the format: `s!mute {member} {amount}` - Requires Helper or higher.
                    **Please invite me! I need to get to 100 servers to be verified :pleading_face:**
                    My invite link: *https://discord.com/api/oauth2/authorize?client_id=961289249993424996&permissions=8&scope=bot*"""
                                       ),
                          color=0x2f19bb)
    await ctx.send(embed=embed)


# s!help command
@client.command()
async def warn(ctx, member: discord.Member, reason=None):
    await member.send(f'You have been warned for {reason}')
    await ctx.send("Member Has Been Warned")


    # s!warn command
@client.command()
async def purge(ctx, *, amount):
    amount = int(amount)
    await ctx.channel.purge(limit=amount)
    await ctx.channel.purge(limit=1)


    # s!purge command
@client.command()
async def members(ctx):
    count = ctx.guild.member_count
    await ctx.send(f'There are {count} members in Arc of The Scythe')


# s!members command
@slash.slash(name="Ping", description="Ping command")
async def test(ctx):
    await ctx.send('Insert Command')


    # s!test command
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        reason = " No reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason}')


# s!kick command
@client.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        reason = " No reason provided"
    await ctx.guild.ban(member)
    await ctx.send(f'User {member.mention} has been banned for {reason}.')


# s!ban command
TOKEN = os.environ['TOKEN']
client.run(TOKEN)