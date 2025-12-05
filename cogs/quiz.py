import discord
from discord.ext import commands
from discord import app_commands

from utils.question_manager import QuestionManager
from utils.score_manager import ScoreManager

qm = QuestionManager()
sm = ScoreManager()

class Quiz(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(
        name="quiz",
        description="Pose une question de culture générale."
    )
    async def quiz(self, ctx: commands.Context):
        """Command usable as !quiz AND /quiz"""
        q = qm.get_random_question()

        embed = discord.Embed(
            title="🧠 Question de Culture Générale",
            description=q["question"],
            color=discord.Color.blurple()
        )

        choices = q.get("choices", [])
        rep_text = ""
        for i, c in enumerate(choices, start=1):
            rep_text += f"**{i}** — {c}\n"

        embed.add_field(name="Réponses possibles :", value=rep_text, inline=False)
        embed.set_footer(text="Réponds avec le numéro de ta réponse (15s).")

        await ctx.send(embed=embed)

        def check(m: discord.Message):
            return (
                m.author == ctx.author
                and m.channel == ctx.channel
            )

        try:
            reply: discord.Message = await self.bot.wait_for(
                "message",
                timeout=15.0,
                check=check
            )
        except Exception:
            return await ctx.send("⏳ Temps écoulé !")

        # Vérif réponse
        try:
            index = int(reply.content.strip()) - 1
        except ValueError:
            return await ctx.send("❌ Réponse invalide. Réponds avec un numéro.")

        if index < 0 or index >= len(choices):
            return await ctx.send("❌ Ce numéro ne correspond à aucune réponse.")

        if choices[index] == q["answer"]:
            sm.add_point(ctx.author.id)
            score = sm.get_score(ctx.author.id)
            await ctx.send(f"✅ Bonne réponse {ctx.author.mention} ! (Score: **{score}**) 🔥")
        else:
            await ctx.send(f"❌ Mauvaise réponse ! La bonne réponse était : **{q['answer']}**")

async def setup(bot: commands.Bot):
    await bot.add_cog(Quiz(bot))
