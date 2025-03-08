# Importando a API e bibliotecas
import discord
from discord.ext import commands
from youtubesearchpython import VideosSearch

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Configuração do bot
intents = discord.Intents.all()
bot = commands.Bot('.', intents=intents)

# Configuração do Spotify API
SPOTIPY_CLIENT_ID = "" #pegar no spotify for developers
SPOTIPY_CLIENT_SECRET = "" #pegar no spotify for developers

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

# Eventos
@bot.event
async def on_ready():
    sincs = await bot.tree.sync()
    print(f'{len(sincs)} comandos sincronizados!')
    print('Bot inicializado com sucesso')

@bot.event
async def on_member_join(member: discord.Member):
    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
    mencionando_usuario = member.mention
    canal_id = 1332667490429304892
    canal = bot.get_channel(canal_id)
    
    if canal:
        await canal.send(mencionando_usuario)
    
    my_embed = discord.Embed(
        title='**Grata**',
        description=f'**{mencionando_usuario}:**\n**Timor est quod patimur, finiendus est.** 🐀'
    )
    imagem = discord.File('Midia/gif/gif_olho.gif', "olho.gif")
    my_embed.set_image(url='attachment://olho.gif')
    my_embed.set_thumbnail(url=avatar_url)
    my_embed.set_footer(text=f'ID do usuário: {member.id}')
    my_embed.set_author(name=member.name, icon_url=avatar_url, url='https://github.com/Gaento')
    
    await canal.send(file=imagem, embed=my_embed)

# Apagar todas as mensagens do chat
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, quantidade: int = 10):
    await ctx.channel.purge(limit=quantidade + 1)
    await ctx.send(f'🧹 {quantidade} mensagens apagadas!', delete_after=3)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"🚫 {ctx.author.mention}, você **não tem permissão** para usar este comando!")

# Lista de comandos
@bot.command(name="ajuda")
async def ajuda(ctx: commands.Context):
    embed = discord.Embed(title="📜 Lista de Comandos", color=discord.Color.dark_gray())
    embed.add_field(name=".clear", value="Apaga mensagens do chat 🧹 (somente para quem tem permissão)", inline=False)
    embed.add_field(name=".Vasco", value="É o Vasco né? Não precisa de explicações 🤓☝", inline=False)
    embed.add_field(name=".youtube <música>", value="Busca um vídeo da música no YouTube 🎵", inline=False)
    embed.add_field(name=".spotify <música>", value="Busca um link da música no Spotify 🎧", inline=False)
    await ctx.send(embed=embed)

# Comando para buscar música no YouTube
@bot.command()
async def youtube(ctx, *, song_name):
    search = VideosSearch(song_name, limit=1)
    results = search.result()
    if results["result"]:
        video_url = results["result"][0]["link"]
        await ctx.send(f"Aqui está o link da música no YouTube: {video_url}")
    else:
        await ctx.send("Não encontrei essa música no YouTube.")


# Comando para buscar música no Spotify
@bot.command()
async def spotify(ctx, *, song_name):
    results = sp.search(q=song_name, limit=1, type='track')
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_url = track['external_urls']['spotify']
        await ctx.send(f"Aqui está a música no Spotify: {track_url}")
    else:
        await ctx.send("Não encontrei essa música no Spotify.")

# Rodar o bot
bot.run('') #pegar no discord for developers
