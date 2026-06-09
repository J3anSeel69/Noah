import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

app = Flask('')


@app.route('/')
def home():
    return "Rose está viva 🌹"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


def keep_alive():
    t = Thread(target=run_web)
    t.start()

#permiçoes do bot
intents = discord.Intents.default()
intents.message_content = True

#Criando o Bot
bot = commands.Bot(
    command_prefix="#",
    intents=intents
)

#quando o Noah Ligar
@bot.event
async def on_ready():
    print(f'{bot.user} esta online! 🐬')

    #status do Noah
    await bot.change_presence(
        activity=discord.CustomActivity(
            name="Acho que mais um Café nao vai atrapalhar o Sono né? ☕"
        )
    )

@bot.event
async def on_disconnect():
    print("Bot desconectou 😭")

@bot.event
async def on_resumed():
    print("Bot reconectou 🌹")

#comando de teste
@bot.command()
async def setup(ctx):

    #procurar o canal
    canal = discord.utils.get(
        ctx.guild.text_channels,
        name="regras"
    )

    #caso nao encontre
    if canal is None:
        await ctx.send(
            "não achei o canal #regras"
        )

    #criando embed
    embed = discord.Embed(
        title="⛔ Oque posso ou não fazer? ✅",
        description=(
            "Ola meu Nome é Noah, e é um Prazer ter você aqui, espero que se sinta em"
            "casa, mais mesmo assim por favor respeite algumas regras que temos aqui no"
            "nosso pequeno cantinho:\n\n"

            "1 - Seja Respeitoso: se você tratar os outros com respeito tambem ira ser"
            "tratado de forma Respeitosa, todos ficam Felizes.\n"

            "2 - Sem Caos Desnecessario: Evite spam, flood, discussões exageradas ou"
            "tranformar o servidor em um clima pesado, a ideia desse local que temos é"
            "o conforto e não estresse.\n"

            "3 - Tudo ao seu Tempo: Nem todo mundo consegue responde rápido ou se enturma na hora. "
            "Sem pressão. Às vezes amizade começa devagar mesmo.\n"

            "4 - Ambiente Seguro e Tranquilo: Conteudos pesados como NSFW, Gore e Politica são"
            "Proibidas aqui, isso acaba com a vibe do servidor e das pessoas.\n\n"

            "E a regra mais importante de todas, Seja simpatico e converçe bastante"
            "aproveite bem da companhia das pessoas daqui. Ate logo 😁"
        ),
        color=0xd88cff
    )

    #imagem na mensagem
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1513743197812293692/1514014724298244217/LoverRock_banner.jpg?ex=6a29d397&is=6a288217&hm=7b65f1a84ffe55589b166e0325ab8fb24f2e80ce9956ce98e595f7f2d8ba2c44&"
    )

    #Rodape
    embed.set_footer(
        text="Noah 🐬 • Entre o Restante perdido e procurador de Rosas."
    )

    #enviar mensagem
    mensagem = await canal.send(
        embed=embed
    )

    #fixar mensagem
    await mensagem.pin()

    #confirma
    await ctx.send(
        "mensagem enviada e fixada nas #regras. "
    )

#token do bot
import os

keep_alive()

bot.run(
    os.getenv("TOKEN"),
    reconnect=True
)
