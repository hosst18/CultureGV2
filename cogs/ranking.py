import discord
from discord.ext import commands

from utils.score_manager import ScoreManager

sm = ScoreManager()

class Ranking(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(
        name="top",
        description="Affiche le classement des meilleurs joueurs."
    )
    async def top(self, ctx: commands.Context):
        top = sm.top_scores(limit=10)

        if not top:
            return await ctx.send("Personne n'a encore de score. Joue avec /quiz ou !quiz !")

        embed = discord.Embed(
            title="🏆 Classement CultureG",
            color=discord.Color.purple()
        )

        lines = []
        medals = ["🥇", "🥈", "🥉"]
        for i, (user_id, score) in enumerate(top, start=1):
            user = ctx.guild.get_member(int(user_id))
            username = user.display_name if user else f"Utilisateur {user_id}"
            prefix = medals[i-1] if i <= 3 else f"#{i}"
            lines.append(f"{prefix} — **{username}** : {score} pts")

        embed.description = "\n".join(lines)
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Ranking(bot))
