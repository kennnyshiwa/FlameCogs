# FlameCogs

[![Discord server](https://discordapp.com/api/guilds/535921134152187919/embed.png)](https://discord.gg/bYqCjvu)
[![Red cogs](https://img.shields.io/badge/Red--DiscordBot-cogs-red.svg)](https://github.com/Cog-Creators/Red-DiscordBot/tree/V3/develop)
[![discord.py](https://img.shields.io/badge/discord-py-blue.svg)](https://github.com/Rapptz/discord.py)

Cogs for a [Red Discord Bot](https://github.com/Cog-Creators/Red-DiscordBot)  

# Installation

>These are cogs for the [Red-DiscordBot V3](https://github.com/Cog-Creators/Red-DiscordBot/tree/V3/develop). You need to have a working V3 Redbot in order to install these cogs.

*[p] is your prefix.*

Make sure downloader is loaded:  
`[p]load downloader`

Add the repo to your bot:  
`[p]repo add flamecogs https://github.com/Flame442/FlameCogs`

Install the cogs you want:  
`[p]cog install flamecogs <cog name>`

Load installed cogs:  
`[p]load <cog name>`

# Cogs

Name | Description
--- | ---
[Battleship](../master/README.md#battleship) | Play battleship against another member of your server.
[Deepfry](../master/README.md#deepfry) | Deepfry and nuke images.
[Face](../master/README.md#face) | Find and describe the faces in an image.
[Gameroles](../master/README.md#gameroles) | Grant roles when a user is playing a specific game.
[Hangman](../master/README.md#hangman) | Play hangman with the bot.
[Monopoly](../master/README.md#monopoly) | Play monopoly with up to 7 other people in your server.
[Onlinestats](../master/README.md#onlinestats) | Information about what devices people are using to run discord.
[Partygames](../master/README.md#partygames) | Chat games focused on coming up with words from 3 letters.
[SimpleEmbed](../master/README.md#simpleembed) | Simply create embeds.
[Wordstats](../master/README.md#wordstats) | Track commonly used words by server and member.

## Battleship

This cog will let you play battleship against another member of your server.

### Usage

**`[p]battleship`**  
Begin a game of battleship.

**`[p]battleshipset <argument>`**  
Config options for battleship.  
This command is only usable by the server owner and bot owner.

**`[p]battleshipset extra [value]`**  
Set if an extra shot should be given after a hit.  
Defaults to `True`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]battleshipset mention [value]`**  
Set if players should be mentioned when their turn begins.  
Defaults to `True`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

## Deepfry

This cog lets you deepfry and nuke images. It has a configurable chance to deepfry any image posted automatically and users can choose to deepfry or nuke images.  

### Usage

**`[p]deepfry [link]`**  
Deepfries the attached image.  
Use the optional parameter `link` to use a **direct link** as the target.  
Alias: `[p]df`

**`[p]nuke [link]`**  
Nukes the attached image.  
Use the optional parameter `link` to use a **direct link** as the target.

**`[p]deepfryset <argument>`**  
Config options for deepfry.  
This command is only usable by the server owner and bot owner.

**`[p]deepfryset frychance [value]`**  
Change the rate images are automatically deepfried.  
Images will have a 1/`[value]` chance to be deepfried.  
Higher values cause less often fries.  
Set to `0` to disable.  
Defaults to `0` (off)  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]deepfryset nukechance [value]`**  
Change the rate images are automatically nuked.  
Images will have a 1/`[value]` chance to be nuked.  
Higher values cause less often nukes.  
Set to `0` to disable.  
Defaults to `0` (off)  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]deepfryset allowalltypes [value]`**  
Allow filetypes that have not been verified to be valid.  
Can cause errors if enabled, **use at your own risk**.  
Defaults to `False`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

## Face

This cog will find faces in images and give information about them such as predicted age, hair color, and emotions.  
This cog requires an API key from Microsoft Azure Face API. Setup instructions can be found [here!](../master/face/setup.md)

### Usage

**`[p]face [link]`**  
Finds and describes faces in the attached image.  
Use the optional parameter `link` to use a **direct link** as the target.

**`[p]faceset <argument>`**  
Config options for face.  
This command is only usable by the server owner and bot owner.

**`[p]faceset menu [value]`**  
Set if results should be made into a menu.  
If in a menu, one large image with faces marked will be sent instead of cropped images of each face.  
Defaults to `True`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

## Gameroles

This cog will grant roles when a user is playing a specific game.

### Usage

**`[p]gameroles <argument>`**  
Alias `[p]gr <argument>`

**`[p]gameroles addrole <role>`**  
Sets a role to be managed by gameroles.  
Roles with with multiple word names need to be surrounded in quotes.
The bot's highest role needs to be above the role that you are adding and the bot needs permission to manage roles.  
This command is only usable by the server owner and bot owner.

**`[p]gameroles delrole <role>`**  
Stop a role from being managed by gameroles.  
Roles with with multiple word names need to be surrounded in quotes.  
This command is only usable by the server owner and bot owner.

**`[p]gameroles addactivity <role> <activity>`**  
Add an activity to trigger a role.  
Roles and activities with with multiple word names need to be surrounded in quotes.  
You can get the name of your current activity with `[p]gameroles currentactivity`.  
This command is only usable by the server owner and bot owner.

**`[p]gameroles delactivity <role> <activity>`**  
Remove an activity from triggering a role.  
Roles and activities with with multiple word names need to be surrounded in quotes.  
You can get the name of your current activity with `[p]gameroles currentactivity`.   
This command is only usable by the server owner and bot owner.

**`[p]gameroles listroles`**  
List the roles currently managed by gameroles.  
This command is only usable by the server owner and bot owner.

**`[p]gameroles listactivities <role>`**  
List the activities that trigger a role.  
Roles with with multiple word names need to be surrounded in quotes.  
This command is only usable by the server owner and bot owner.

**`[p]gameroles currentactivity`**  
Get your current activity.  
This command is only usable by the server owner and bot owner.

**`[p]gameroles recheck`**  
Force a recheck of your current activities.  

**`[p]gameroleset <argument>`**  
Config options for gameroles.  
This command is only usable by the server owner and bot owner.  
Alias: `[p]grset`

**`[p]gameroleset add [value]`**  
Set if roles should be added when someone starts playing a game.  
Defaults to `True`.  
This value is server specific.

**`[p]gameroleset remove [value]`**  
Set if roles should be removed when someone stops playing a game.  
Defaults to `True`.  
This value is server specific.

## Hangman

This cog will play hangman with you.

### Usage

**`[p]hangman`**  
Begin a game of hangman.

**`[p]hangmanset <argument>`**  
Config options for hangman.  
This command is only usable by the server owner and bot owner.

**`[p]hangmanset wordlist [value]`**  
Change the wordlist used.  
Extra wordlists can be put in the data folder of this cog.  
Wordlists are a text file with every new line being a new word.  
Use `default` to restore the default wordlist.  
Use `list` to list available wordlists.  
This value is server specific.

**`[p]hangmanset edit [value]`**  
Set if hangman messages should be one edited message or many individual messages.  
Defaults to `True`.  
This value is server specific.

## Monopoly

This cog will let you play monopoly with up to 7 other people in your server.

### Usage

**`[p]monopoly [savename]`**  
Begin a game of monopoly.   
Use the optional parameter `savename` to load a saved game.

**`[p]monopoly delete <savefile>`**  
Delete a save file.  
This cannot be undone.  
This command is only usable by the server owner and bot owner.

**`[p]monopoly list`**  
List available save files.   

**`[p]monopolyconvert <savefile>`**  
Convert a savefile to work with the latest version of this cog.

**`[p]monopolyconvert list`**  
List save files that can be converted.

**`[p]monopolystop`**  
Stop the game of monopoly in the current channel.  
This command is only usable by the server owner and bot owner.

**`[p]monopolyset <argument>`**  
Config options for monopoly.  
This command is only usable by the server owner and bot owner.

**`[p]monopolyset auction [value]`**  
Set if properties should be auctioned when passed on.  
Defaults to `False`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset bail [value]`**  
Set how much bail should cost.  
Defaults to `50`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset doublego [value]`**  
Set if landing on go should double the amount of money given.  
Defaults to `False`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset freeparking [value]`**  
Set the reward for landing on free parking.  
Use an integer to set a static reward.  
Use "none" for no reward.  
Use "tax" to use the sum of taxes and fees as the reward.  
Defaults to `None`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset go [value]`**  
Set the base value of passing go.  
Defaults to `200`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset hotellimit [value]`**  
Set a limit on the number of hotels that can be bought.  
Use -1 to disable the limit.  
Defaults to `12`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset houselimit [value]`**  
Set a limit on the number of houses that can be bought.  
Use -1 to disable the limit.  
Defaults to `32`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset income [value]`**  
Set how much Income Tax should cost.  
Defaults to `200`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset luxury [value]`**  
Set how much Luxury Tax should cost.  
Defaults to `100`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset maxjailrolls [value]`**  
Set the maximum number of rolls in jail before bail has to be paid.  
Defaults to `3`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset mention [value]`**  
Set if players should be mentioned when their turn begins.  
Defaults to `False`.  
This command is only usable by the server owner and bot owner.
This value is server specific.  

**`[p]monopolyset minraise [value]`**  
Set the minimum raise in auctions.  
Defaults to `1`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset startingcash [value]`**  
Set how much money players should start the game with.  
Defaults to `1500`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]monopolyset timeout [value]`**  
Set the amount of time before the game times out.  
Value is in seconds.  
Use -1 to disable the timeout.  
Defaults to `60`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

## Onlinestats

This cog gives information about what devices people are using to run discord.

### Usage

**`[p]onlinestatus`**  
Prints how many people are using each type of device.  
Alias: `[p]onlinestats`

**`[p]onlineinfo [member]`**  
Shows what devices a member is using.  
Defaults to the author.

## Partygames

This cog has chat games focused on coming up with words from 3 letters.

### Usage

**`[p]partygames <argument>`**  
Alias `[p]pg <argument>`

**`[p]partygames bombparty [hp]`**  
Start a game of bombparty.  
Each player will be asked to come up with a word that contains the given characters.  
If they are unable to do so, they will lose a life.  
Words cannot be reused.  
The last person to have lives left wins.  
Use the optional parameter `hp` to set the number of lives each person starts with.

**`[p]partygames fast [maxpoints]`**  
Race to type a word the fastest.  
The first person to type a word that contains the given characters gets a point.  
Words cannot be reused.  
The first person to get `maxpoints` points wins.  
Use the optional parameter `maxpoints` to set the number of points required to win.

**`[p]partygames long [maxpoints]`**  
Type the longest word.  
The person to type the longest word that contains the given characters gets a point.  
Words cannot be reused.  
The first person to get `maxpoints` points wins.  
Use the optional parameter `maxpoints` to set the number of points required to win.

**`[p]partygames most [maxpoints]`**  
Type the most words.  
The person to type the most words that contain the given characters gets a point.  
Words cannot be reused.  
The first person to get `maxpoints` points wins.  
Use the optional parameter `maxpoints` to set the number of points required to win.

**`[p]partygames mix [maxpoints]`**  
Play a mixture of all 4 games.  
Words cannot be reused.  
The first person to get `maxpoints` points wins.  
Use the optional parameter `maxpoints` to set the number of points required to win.

**`[p]partygames locale <locale>`**  
Override the bot's locale for partygames.  
Use `reset` to remove the override.  
This command is only usable by the bot owner.  
This value is global.

## SimpleEmbed

This cog will let you send embedded messages quickly and easily.

### Usage

**`[p]sendembed [color] <text>`**  
Send an embed.  
Use the optional parameter `color` to change the color of the embed.  
The embed will contain the text `text`.  
All normal discord formatting will work inside the embed.

## Wordstats

This cog will track commonly used words by server and member.

### Usage

**`[p]wordstats [member_or_guild] [amount_or_word]`**  
Prints the most commonly used words.  
Use the optional parameter `member_or_guild` to see the stats of a member or guild.  
Use the optional parameter `amount_or_word` to change the number of words that are displayed, or to check the stats of a specific word (default `30`).

**`[p]wordstats global [amount_or_word]`**  
Prints the most commonly used words across all guilds.  
Use the optional parameter `amount_or_word` to change the number of words that are displayed, or to check the stats of a specific word (default `30`).

**`[p]topchatters [guild] [word] [amount]`**  
Prints the members who have said the most words.  
Use the optional parameter `guild` to see the topchatters in a specific guild.
Use the optional parameter `word` to see the topchatters of a specific word.  
Use the optional parameter `amount` to change the number of members that are displayed (default `10`).

**`[p]topchatters global [word] [amount]`**  
Prints the members who have said the most words across all guilds.  
Use the optional parameter `word` to see the topchatters of a specific word.  
Use the optional parameter `amount` to change the number of members that are displayed (default `10`).

**`[p]topratio <word> [guild] [amount]`**  
Prints the members with the highest "word to all words" ratio.  
Use the parameter `word` to set the word to compare.  
Use the optional parameter `guild` to see the ratio in a specific guild.  
Use the optional parameter `amount` to change the number of members that are displayed (default `10`).

**`[p]topratio global <word> [amount]`**  
Prints the members with the highest "word to all words" ratio in all guilds.  
Use the parameter `word` to set the word to compare.  
Use the optional parameter `amount` to change the number of members that are displayed (default `10`).

**`[p]wordstatsset <argument>`**  
Config options for wordstats.  
This command is only usable by the server owner and bot owner.  

**`[p]wordstatsset server [value]`**  
Set if wordstats should record stats for the channel the command is used in.  
Defaults to `True`.  
This command is only usable by the server owner and bot owner.  
This value is server specific.

**`[p]wordstatsset channel [value]`**  
Set if wordstats should record stats for the server the command is used in.  
Defaults to `True`.  
This command is only usable by the server owner and bot owner.  
This value is channel specific.

# Contact

Feel free to create an issue on this repository or join [my discord](https://discord.gg/bYqCjvu) if you have any issues.

# Credit

Thanks to:  
The [creators of Redbot](https://github.com/Cog-Creators/Red-DiscordBot/graphs/contributors) for creating the base these cogs run on,  
The helpful support staff at the [Redbot discord](https://discord.gg/red),  
[Aikaterna](https://github.com/aikaterna) for taking the time to QA this repo,  
[Hasbro](hasbro.com) for creating the games that Battleship and Monopoly are based off of,  
[TrustyJAID](https://github.com/TrustyJAID) for helping with Deepfry,  
[Desi Quintans](http://www.desiquintans.com/nounlist) for the wordlist used by Hangman,  
[iComputer7#0007](https://github.com/iComputer7) for the inspiration for Face,  
[Microsoft Azure](https://azure.microsoft.com/en-us/) for the API that Face uses,  
[Sparklin Labs](http://bombparty.sparklinlabs.com/) for creating the game that Partygames is based off of,  
[/u/YoungsterGlenn](https://www.reddit.com/r/BombParty/comments/3lehxq/a_nearly_exhaustive_subset_of_the_bombparty/) for the wordlist used by Partygames,  
[Sinbad](https://github.com/mikeshardmind) for helping with Wordstats,  
And [Preda](https://github.com/PredaaA) for translating Partygames.
