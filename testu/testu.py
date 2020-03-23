import discord
from discord.ext import commands

class testù(commands.Cog):
      def __init__(self, bot):
            self.bot = bot

    @tasks.loop(seconds=10)
    await ctx.send("testù")

def setup(bot):
      bot.add_cog(ServStatus(bot))
