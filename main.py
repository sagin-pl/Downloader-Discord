import asyncio
import requests
import discord
from discord.ext import commands
import ffmpeg
import json
import os
import random

client = commands.Bot(command_prefix='^')


@client.command()
async def sagin(ctx, link='n', res="hd", raw="n"):
    if link=='n':
        await ctx.send("Podaj Link gegerze")
    else:
        r = requests.post("https://api.sagin.pl/szuragV2", json = {
        "settings": res,
        "url": link
        })
        try:
            trackingURL = json.loads(r.text)['url']

            uuuid = str(trackingURL).split("/")[-1]

            data = requests.get(trackingURL).json()[uuuid]

            embed=discord.Embed(title="Sagin.pl", url="https://sagin.pl")
            embed.add_field(name="LINK", value="0%", inline=True)
            embed.set_image(url="https://witryny.sagin.pl/saginlogo.gif")
            emb = await ctx.send(embed=embed)
            while True:
                data = requests.get(trackingURL).json()[uuuid]
                if "https" in str(data):
                    if not raw=='n':
                        await ctx.send(data)
                        await emb.delete()
                        return
                    embed=discord.Embed(title="FILM", url=str(data))
                    embed.add_field(name="LINK", value=data, inline=True)
                    embed.set_image(url="https://witryny.sagin.pl/saginlogo.gif")
                    await emb.edit(embed=embed)
                    break
                else:
                    embed=discord.Embed(title="Sagin.pl", url="https://sagin.pl")
                    embed.add_field(name="LINK", value="Przetwarzanie filmu... " + str(data) + "%", inline=True)
                    embed.set_image(url="https://witryny.sagin.pl/saginlogo.gif")
                    await emb.edit(embed=embed)

                await asyncio.sleep(1)
        except Exception as E:

            r = requests.post("https://api.sagin.pl/szurag", json = {
            "settings": res,
            "url": link
            })

            trackingURL = json.loads(r.text)['url']

            uuuid = str(trackingURL).split("/")[-1]

            data = requests.get(trackingURL).json()[uuuid]

            embed=discord.Embed(title="Sagin.pl", url="https://sagin.pl")
            embed.add_field(name="LINK", value="0%", inline=True)
            embed.set_image(url="https://witryny.sagin.pl/saginlogo.gif")
            emb = await ctx.send(embed=embed)
            while True:
                data = requests.get(trackingURL).json()[uuuid]
                if "https" in str(data):

                    if not raw=='n':
                        await ctx.send(data)
                        await emb.delete()
                        return

                    embed=discord.Embed(title="FILM", url=str(data))
                    embed.add_field(name="LINK", value=data, inline=True)
                    embed.set_image(url="https://witryny.sagin.pl/saginlogo.gif")
                    await emb.edit(embed=embed)
                    break
                else:
                    embed=discord.Embed(title="Sagin.pl", url="https://sagin.pl")
                    embed.add_field(name="LINK", value="Przetwarzanie filmu... " + str(data) + "%", inline=True)
                    embed.set_image(url="https://witryny.sagin.pl/saginlogo.gif")
                    await emb.edit(embed=embed)

                await asyncio.sleep(1)
            
client.run("Tajne to jest")
