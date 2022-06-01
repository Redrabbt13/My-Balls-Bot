from typing import Any, Callable, List

import discord
import os
import re

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

balls_list = ["balls", "Balls", "BALL", "BALLS", "ball", "Ball"]
# refactor_punctuation_list: refactors string by removing punctuation and
# splits sentence into list by space
refactor_punctuation_list: Callable[[Any], List[str]] = lambda x: list(
	re.sub(r'[^\w\s]', '', x).split())
# refactored_message: determines whether each word in new refactored message
# list contains words in balls_list. Returns a boolean list
refactored_message: Callable[[Any], List[bool]] = lambda rpl: list(
	map(lambda x: any(b in x for b in balls_list), rpl))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	rpl = refactor_punctuation_list(message.content)
	rm = refactored_message(rpl)
	out_message = 'in my jaaaws!'
	if any(rm):
		ball_in_question = rpl[rm.index(True)]
		if ball_in_question.isupper():
			out_message = out_message.upper()
		
		await message.channel.send(out_message)

client.run('OTgxMjk4NDA5Njc3OTE0MTEy.G_fXrh.dJzHmXygD8YvxCOdK4Jj8gBBTmOhI'
           '-FcJFjxsY')
