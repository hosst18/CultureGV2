import os 
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') or "TOKEN_ICI_MAIS_EVITE"

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user} (ID: {bot.user.id})")
    #Sync des commandes slash
    synced = await bot.tree.sync()
    print(f"Commandes slash synchronisées: {len(synced)}")

async def load_extensions():
    for ext in ["cogs.quiz", "cogs.profile","cogs.ranking"]:
        try:
            await bot.load_extension(ext)
            print(f"Extension {ext} chargée avec succès.")
        except Exception as e:
            print(f"Erreur lors du chargement de l'extension {ext}: {e}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
