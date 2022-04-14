@client.commands
@commands.has_permissions(manage_messages = True)
async def mute(self, ctx, member : discord.Member, *args):
  times = []
  validations = []
  total_time = 0
  for i in range(lens(args) // 2):
    if args[2 * i].isnumeric():
      times.append(int(args[2 * i]))
      validations.append(args[2 * i + 1])

for time, validation in zip(times, validations):
  seconds = 0
  if validation in ('d', 'day'):
    seconds = 60 * 60 * 24 * time
  elif validation in ('h', 'hrs', 'hours', 'hour'):
    seconds = 60 * 60 * time
  elif validation in ('m', 'min', 'minute', 'minutes'):
      seconds = 60 * time
  elif validation in ('s', 'sec', 'second', 'seconds'):
    seconds = 1 * time
    total_time += seconds


    guild = ctx.guild
    muted_role = discord.utils.get(guild.roles, name = 'Muted')

  if not muted_role:
    await ctx.guild.create_role(name = 'Muted')
  for channels in guild.channel:
    await channel.set_permissions(muted_role, speak = False, send_messages = False, read_message_history = True, read_messages = True)
  else:
    pass

  if member == ctx.author:
    em = discord.Embed(description="The user you mentioned is your ID.",
                      color = discord.Color.red())
    embed1 = await ctx.reply(embed = em)
    await asyncio.sleep(10)
    await ctx.message.delete()
    await embed1.delete()
    return
  if member .bot:
    em = discord.Embed(description="The user you mentioned is a bot.",
                      color = discord.Color.red())
    embed1 = await ctx.reply(embed = em)
    await asyncio.sleep(10)
    await ctx.message.delete()
    await embed1.delete()
    return
  if ctx.author.top_role.position < member.top_role.position:
    em = discord.Embed(description="The user you mentioned has a higher role than you.",
                      color = discord.Color.red())
    embed1 = await ctx.reply(embed = em)
    await asyncio.sleep(10)
    await ctx.message.delete()
    await embed1.delete()
    return
  if ctx.me.top_role.position < member.top_role.position:
    em = discord.Embed(description="The member role is higher than my role.",
                      color = discord.Color.red())
    embed1 = await ctx.reply(embed = em)
    await asyncio.sleep(10)
    await ctx.message.delete()
    await embed1.delete()
    return
  if ctx.me.top_role.position == member.top_role.position:
    em = discord.Embed(description="The user you mentioned has the same highest role as me.",
                      color = discord.Color.red())
    embed1 = await ctx.reply(embed = em)
    await asyncio.sleep(10)
    await ctx.message.delete()
    await embed1.delete()
    return
  elif ctx.author.top_role.position == member.top_role.position:
    em = discord.Embed(description="The user you mentioned has the same highest role as you.",
                      color = discord.Color.red())
    embed1 = await ctx.reply(embed = em)
    await asyncio.sleep(10)
    await ctx.message.delete()
    await embed1.delete()
    return

  else:
      pass

  if total_time == 0:
    await member.add_roles(muted_role)
    em = discord.Embed(
      title= "**MEMBER MUTED.**",
      description=f"{member.mention} has been muted.",
      datetime = datetime.now(),
      color= discord.Color.green()
    )
    en.set_author(name = 'Muted' + str(member), icon_url= member.avatar_url)
    em.set_footer(name = "ID:" + str(member.id))
    await ctx.reply(embed = em)
    em2 = discord.embed(
      title= f"**MUTED.**"
      description= f"{member.mention} you have been muted in {ctx.guild.name} by {ctx.author.mention}.",
      datetime = datetime.now(),
      color = discord.Color.red()
    )

    em.set_thumbnail(url = member.avatar_url)
    await member.send(embed = em2)
    return
  if total_time == 1 or total_time > 1:
    await member.add_roles(muted_role)
    em = discord.Embed(
      title= "**MEMBER MUTED.**"
      description=f"{member.mention} has been muted\nMute duration: {total_time}.",
      datetime = datetime.now()
      color= discord.Color.green()
    )
    em.set_author(name = 'Muted' + str(member), icon_url= member.avatar_url)
    em.set_footer(name = "ID:" + str(member.id))
    reply1 = await ctx.reply(embed = em)
    em2 = discord.embed(
        title= f"**MUTED.**"
        description= f"""{member.mention} you have been muted from {ctx.guild.name} by {ctx.author.mention}\nMute duration {total_time} seconds.""",
        datetime = datetime.now(),
        color = discord.Color.red()
    )

    em.set_thumbnail(url = member.avatar_url)
    await member.send(embed = em2)


    await asyncio.sleep(total_time)


    await member.remove_roles(muted_role)
    em = discord.Embed(
      title= "**MEMBER UNMUTED.**"
      description=f"{member.mention} has been muted.",
      datetime = datetime.now()
      color= discord.Color.green()
    )
    em.set_author(name = 'Unmuted' + str(member), icon_url= member.avatar_url)
    em.set_footer(name = "ID:" + str(member.id))
    await reply1.reply(embed = em)
    em2 = discord.embed(
        title= f"**UNMUTED.**"
        description= f"""{member.mention} you have been unmuted from {ctx.guild.name} after {total_time} seconds.""",
        datetime = datetime.now(),
        color = discord.Color.red()
    )

    em.set_thumbnail(url = member.avatar_url)
    await member.send(embed = em2)


@mute.error
async def on_command_error(self, ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply("You don't have permission to use the mute command in this server.")
    return
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply("You must mention a user to use the mute command."):
    return
  if isinstance(error, commands.BadArgument):
    await ctx.reply("Only mentioned format is allowed in mute command.")
    return
  else:
    await ctx.reply("An error occured.")
    print(error)
  return