import unittest
from main import *


class UnitTests(unittest.TestCase):

  def test_1(self):
      # Enter code here
    import os
    
    import discord
    
    from discord.ext import commands
    
    from keep_alive import keep_alive
    
    bot = commands.Bot(command_prefix="s!")
      # Prefix
    @bot.event
    async def on_connect():
      await bot.change_presence(activity=discord.Game(name='s!help'))
      print("Scythe Bot is online.")
    bot.remove_command("help")
    @bot.command()
    async def ping(ctx):
      await ctx.send("Pong!")
      # +ping command
    @bot.command()
    async def say(ctx, *, text):
      await ctx.channel.purge(limit=1)
      await ctx.send(text)
      # +say command
    @bot.command()
    async def warn(ctx, member: discord.Member, reason=None):
      await member.send(f'You have been warned for {reason}')  
      await ctx.send("Member Has Been Warned")
      # +warn command
    @bot.command()
    async def purge(ctx, *, ammount):
      ammount = int(ammount)
      await ctx.channel.purge(limit=ammount)
      # +purge command
    @bot.command()
    async def help(ctx):
      await ctx.channel.purge(limit=1)
      await ctx.send('''
                        **These are the commands so far for Scythe Bot!**
                     
                        s!ping | Pings the bot
                        s!help | Shows all the Scythe Bot commands
                        s!kick | Kicks member, use it in the format: s!kick {member} - Requires Admin or higher
                        s!ban | Bans member, use it in the format: s!ban {member} - Requires Admin or higher
                        s!warn | Warns member, use it in the format: s!warn {member} Requires Trainee or higher
                     
      *More coming soon...*''')
      # +commands command
    @bot.command()
    async def test(ctx):
      await ctx.send('Insert Command')
      # +test command
    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
        if reason==None:
          reason=" No reason provided"
        await ctx.guild.kick(member)
        await ctx.send(f'User {member.mention} has been kicked for {reason}')
      
    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def ban(ctx, member: discord.Member, *, reason=None):
        if reason==None:
          reason=" No reason provided"
        await ctx.guild.ban(member)
        await ctx.send(f'User {member.mention} has been banned for {reason}.')
    keep_alive()
    TOKEN = os.environ['TOKEN']
    bot.run(TOKEN)

