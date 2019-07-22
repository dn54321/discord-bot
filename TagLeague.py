from TagHandler import *
from properties import *
import discord
class TagLeague(Tag_Handler):
    async def run(client, payload):
        if payload.message_id == REACT_MSG and payload.emoji.name == '♌':
            member = client.get_guild(GUILD).get_member(payload.user_id)
            for role in member.roles:
                if role.name == 'Member':
                    role = discord.utils.get(client.get_guild(GUILD).roles, name="[League Of Legends]")
                    try:
                        await member.add_roles(role)
                    except:
                        print("Member rank too high!")
                    finally:
                        break