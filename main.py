import discord
import asyncio
from discord.ext import commands
import logging
from properties import *
from Tag_Listener import *
from Tag_Handler import *
from Swear_Filter import *
logging.basicConfig(level=logging.INFO)
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    print('Guilds Connected:')
    for guild in client.guilds:
        print("guild name: \"" + guild.name + "\", id: \""+ str(guild.id) +"\"\n")

    # adding tag event listener
    listener = Tag_Listener(client)
    client.add_cog(listener)
    client.add_cog(Swear_Filter(client))

    # LEAGUE OF LEGENDS TAG
    league_Handler = Tag_Handler(Add_Role(),'♌', TEXT, "+[League Of Legends]", "Member")
    listener.add_event(league_Handler, "onTag")
    league_Handler = Tag_Handler(Remove_Role(),'♌', TEXT, "+[League Of Legends]", "Member")
    listener.add_event(league_Handler, "offTag")
     #Usings tags for the message to obtain roles
  #  mess = await client.get_channel(TEXT_CHANNEL).fetch_message(TEXT)
  #  await mess.add_reaction('🔄');
    

@client.event
async def on_message(message):
    if message.author.bot == False:
        print('Message from {0.author}: {0.content}'.format(message))
        print('author avatar hash: {}'.format(message.author.avatar_url))
        print(str(message.channel.id))
        if message.channel.id == 599494119584301056 and message.content == "-password please!":
            await message.delete()
            await message.author.send("For the last time, stop begging me everyday, please stop saying 'please'!")
            async with message.author.dm_channel.typing():
                await asyncio.sleep(3)
                await message.author.send("How about this, I'll give you one chance, here's an ID card which will let you in my garden, here you can gather ingredients.")
            async with message.author.dm_channel.typing():
                await asyncio.sleep(2)
                await message.author.send("Make me something delicious and I'll consider making you my apprentice chef! Hmmpf.")
            role = discord.utils.get(message.guild.roles, name="Member")
            await message.author.add_roles(role)
            role = discord.utils.get(message.guild.roles, name="Guest")
            await message.author.remove_roles(role)
            embed=discord.Embed(title="Description", description="This card identifies that this particular person has started their career as a chef and has been acknowledged by chef Hunzer as a disciple.")
            embed.set_author(name="[common] Membership Card", icon_url="http://getdrawings.com/vectors/zen-circle-vector-7.jpg")
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.add_field(name="Name", value=message.author.name, inline=True)
            embed.add_field(name="Assigned By", value="Chef Hunzer", inline=True)
            embed.set_footer(text="Remark: Can only be obtained through Chef Hunzer's recognition of a potential chef!")
            await message.author.send(embed=embed)
'''
    if payload.message_id == TEXT and payload.emoji.name == '🔄':
        member = client.get_guild(GUILD).get_member(payload.user_id)
        isMember = False;
        try:
            for role in member.roles:
                if role.name == 'Member':
                    isMember = True
                    break;
            if isMember == False:
                role = discord.utils.get(client.get_guild(GUILD).roles, name="Guest")
                await member.add_roles(role)
        except:
            print("Member rank too high!")
'''

#client = discord.ext.commands.Bot("!", None, "A master chef!", options={"activity": discord.Game("Cooking Food")})
client.run('NTk5MzA4NTg1OTYwMzQxNTA2.XSjVtg.8sIeUAadBSNK6RAgz5vRzhGMyHU')
