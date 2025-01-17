import discord
from redbot.core import commands
from redbot.core import Config
from redbot.core import checks
import asyncio
from .game import BattleshipGame


class Battleship(commands.Cog):
	"""Play battleship with one other person."""
	def __init__(self, bot):
		self.bot = bot
		self.games = []
		self.bs = BattleshipGame
		self.config = Config.get_conf(self, identifier=7345167901)
		self.config.register_guild(
			extraHit = True,
			doMention = False
		)
	
	@commands.guild_only()
	@commands.command()
	async def battleship(self, ctx):
		"""Start a game of battleship."""
		if [game for game in self.games if game.ctx.channel == ctx.channel]:
			return await ctx.send('A game is already running in this channel.')
		dm = await self.config.guild(ctx.guild).doMention()
		eh = await self.config.guild(ctx.guild).extraHit()
		check = lambda m: (
			m.author != ctx.message.author 
			and not m.author.bot 
			and m.channel == ctx.message.channel 
			and m.content.lower() == 'i'
		)
		await ctx.send('Second player, say I.')
		try:
			r = await self.bot.wait_for('message', timeout=60, check=check)
		except asyncio.TimeoutError:
			return await ctx.send('Nobody else wants to play, shutting down.')
		if [game for game in self.games if game.ctx.channel == ctx.channel]:
			return await ctx.send('Another game started in this channel while setting up.')
		await ctx.send(
			'A game of battleship will be played between '
			f'{ctx.author.display_name} and {r.author.display_name}.'
		)
		game = BattleshipGame(ctx, self.bot, dm, eh, ctx.author, r.author, self)
		self.games.append(game)
	
	@commands.guild_only()
	@checks.guildowner()
	@commands.command()
	async def battleshipstop(self, ctx):
		"""Stop the game of battleship in this channel."""
		wasGame = False
		for x in [game for game in self.games if game.ctx.channel == ctx.channel]:
			x.stop()
			wasGame = True
		if wasGame: #prevent multiple messages if more than one game exists for some reason
			await ctx.send('The game was stopped successfully.')
		else:
			await ctx.send('There is no ongoing game in this channel.')
	
	@commands.guild_only()
	@checks.guildowner()
	@commands.group()
	async def battleshipset(self, ctx):
		"""Config options for battleship."""
		if ctx.invoked_subcommand is None:
			extraHit = await self.config.guild(ctx.guild).extraHit()
			doMention = await self.config.guild(ctx.guild).doMention()
			msg = (
				f'Extra shot on hit: {extraHit}\n'
				f'Mention on turn: {doMention}'
			)
			await ctx.send(f'```py\n{msg}```')
	
	@battleshipset.command()
	async def extra(self, ctx, value: bool=None):
		"""
		Set if an extra shot should be given after a hit.
		
		Defaults to True.
		This value is server specific.
		"""
		if value is None:
			v = await self.config.guild(ctx.guild).extraHit()
			if v:
				await ctx.send('You are currently able to shoot again after a hit.')
			else:
				await ctx.send('You are currently not able to shoot again after a hit.')
		else:
			await self.config.guild(ctx.guild).extraHit.set(value)
			if value:
				await ctx.send('You will now be able to shoot again after a hit.')
			else:
				await ctx.send('You will no longer be able to shoot again after a hit.')
	
	@battleshipset.command()
	async def mention(self, ctx, value: bool=None):
		"""
		Set if players should be mentioned when their turn begins.
		
		Defaults to False.
		This value is server specific.
		"""
		if value is None:
			v = await self.config.guild(ctx.guild).doMention()
			if v:
				await ctx.send('Players are being mentioned when their turn begins.')
			else:
				await ctx.send('Players are not being mentioned when their turn begins.')
		else:
			await self.config.guild(ctx.guild).doMention.set(value)
			if value:
				await ctx.send('Players will be mentioned when their turn begins.')
			else:
				await ctx.send('Players will not be mentioned when their turn begins.')
	
	def cog_unload(self):
		return [game.stop() for game in self.games]
