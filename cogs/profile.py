import discord
from discord.ext import commands

from utils.score_manager import ScoreManager

sm = ScoreManager()

class Profile(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(
        name="profil",
        description="Affiche ton profil CultureG."
    )
    async def profil(self, ctx: commands.Context, member: discord.Member | None = None):
        user = member or ctx.author
        score = sm.get_score(user.id)

        embed = discord.Embed(
            title=f"📊 Profil CultureG de {user.display_name}",
            color=discord.Color.gold()
        )
        embed.add_field(name="Score total", value=str(score), inline=False)
        embed.set_thumbnail(url=user.display_avatar.url)

        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Profile(bot))
