import discord
from discord import app_commands

TOKEN = "MTQxNTQzNzgwOTg0MTQ3NTczNQ.G-Mag2.AEuuW7MyYPJdJDcflSYKpF7fscb5eVGXM3SgyE"
GUILD_ID = 1414090061372461128  # replace with your server ID

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        await self.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"✅ Logged in as {self.user}")

client = MyClient()

@client.tree.command(name="verify", description="Verify that you're not a bot", guild=discord.Object(id=GUILD_ID))
async def verify(interaction: discord.Interaction):
    warning = (
        "**⚠️ WARNING:** This link will display your public IP address.\n"
        "If you do not want your IP to be shown, **do not click.**\n\n"
        "👉 Verification link: http://yourwebsite.com/verify.html"
    )
    await interaction.response.send_message(warning)

client.run(TOKEN)
