from profanity_check import predict, predict_prob
from discord.ext import commands
import asyncio
import discord
from Tag_Handler import Add_Role, Payload, Remove_Role
class Swear_Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role = Add_Role()
        self.remove = Remove_Role()
    @commands.Cog.listener()
    async def on_message(self, message):
        predict_percent = predict([message.content])[0]
        channel = message.channel
        if predict_percent == 1:
            await channel.send("The message has been deemed inappropriate. You have been silence for 5 minutes.")
            await message.delete()
            await self.role.prep(self.bot, Payload(user_id=message.author.id), None,None, "+『si̸̲̬l̢͓̲en̺̹͞c͖͈͘ȩ』")
            await asyncio.sleep(60*3)
            await self.remove.prep(self.bot, Payload(user_id=message.author.id), None,None, "+『si̸̲̬l̢͓̲en̺̹͞c͖͈͘ȩ』")

        elif predict([message.content]) > 0.7:
            await channel.send("The message has been flagged for scanning. You have been silence for 3 minutes.")
            await message.delete()
            await self.role.prep(self.bot, Payload(user_id=message.author.id), None,None, "+『si̸̲̬l̢͓̲en̺̹͞c͖͈͘ȩ』")
            await asyncio.sleep(60*1)
            await self.remove.prep(self.bot, Payload(user_id=message.author.id), None,None, "+『si̸̲̬l̢͓̲en̺̹͞c͖͈͘ȩ』")