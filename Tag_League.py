from Tag_Handler import *
from properties import *
import discord
class Tag_League(Tag_Handler):
    async def run(client, payload):
        if payload.message_id == TEXT and payload.emoji.name == '♌':
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