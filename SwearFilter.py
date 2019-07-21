from profanity_check import predict, predict_prob
from discord.ext import commands
import discord
class SwearFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        print("Hello")
        predict_percent = predict([message.content])[0]
        channel = message.channel
        if predict_percent == 1:
            await channel.send("The message has been deemed inappropriate. You have been silence for 5 minutes.")
            await message.delete()
        elif predict([message.content]) > 0.7:
            await channel.send("The message has been flagged for scanning. You have been silence for 3 minutes.")
            await message.delete()