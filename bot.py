import discord
import time
import dbutil

client = discord.Client()

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='with MY BIG duck'))
	for x in range(10000000):
		nice = input("msg: ")
		if nice.startswith("/type"):
			async with ru.typing():
				time.sleep(5)
		if nice.startswith("/spam"):
			for x in range(5):
				ru = client.get_channel(749996213666971700)
				await ru.send("My mind is like my web browser. 19 tabs are open, 3 are frozen and I have no idea where the music is coming from.")
		else:
			ru = client.get_channel(749996213666971700)
			await ru.send(nice)
	
	
client.run(dbutil.get_token())
