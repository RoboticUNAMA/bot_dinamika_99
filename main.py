import discord
# from keep_alive import keep_alive

TOKEN = 'ODg1NDI4OTE5MDQ0NTcxMTM2.YTm58A.x6p1xfonKokVftwws4L6Qirxaqc'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    error = False

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!roles'):
        guild = client.get_guild(824196238756675594)
        await message.channel.send(", ".join([str(r.id) for r in guild.roles]))

    if message.content.startswith('!Perkenalkan'):
        msg = message.content.splitlines()

        nama = msg[1].split(":")
        nama = nama[1].strip()

        panggilan = msg[2].split(":")
        panggilan = panggilan[1].strip()

        prodi = msg[3].split(":")
        prodi = prodi[1].strip().lower()
        role_prodi = ""

        angkatan = msg[4].split(":")
        angkatan = angkatan[1].strip()
        role_angkatan = ""

        divisi = msg[5].split(":")
        divisi = divisi[1].strip().lower()
        role_divisi = ""

        if prodi == "teknik informatika" or prodi == "ti" or prodi == "it":
            role_prodi = discord.utils.get(message.author.guild.roles, name="TI")
            await message.author.add_roles(role_prodi)
        elif prodi == "sistem informasi" or prodi == "si":
            role_prodi = discord.utils.get(message.author.guild.roles, name="SI")
            await message.author.add_roles(role_prodi)
        elif prodi == "sistem komputer" or prodi == "sk":
            role_prodi = discord.utils.get(message.author.guild.roles, name="SK")
            await message.author.add_roles(role_prodi)
        else:
            await message.channel.send('Prodi Tidak Terdaftar di Server')

        if angkatan == "2017":
            role_angkatan = discord.utils.get(message.author.guild.roles, name="Angkatan "+angkatan)
            await message.author.add_roles(role_angkatan)
        elif angkatan == "2018":
            role_angkatan = discord.utils.get(message.author.guild.roles, name="Angkatan "+angkatan)
            await message.author.add_roles(role_angkatan)
        elif angkatan == "2019":
            role_angkatan = discord.utils.get(message.author.guild.roles, name="Angkatan "+angkatan)
            await message.author.add_roles(role_angkatan)
        elif angkatan == "2020":
            role_angkatan = discord.utils.get(message.author.guild.roles, name="Angkatan "+angkatan)
            await message.author.add_roles(role_angkatan)
        elif angkatan == "2021":
            role_angkatan = discord.utils.get(message.author.guild.roles, name="Angkatan "+angkatan)
            await message.author.add_roles(role_angkatan)
        elif angkatan == "2022":
            role_angkatan = discord.utils.get(message.author.guild.roles, name="Angkatan "+angkatan)
            await message.author.add_roles(role_angkatan)
        elif angkatan == "2023":
            role_angkatan = discord.utils.get(message.author.guild.roles, name="Angkatan "+angkatan)
            await message.author.add_roles(role_angkatan)
        elif angkatan == "2024":
            role_angkatan = discord.utils.get(message.author.guild.roles, name="Angkatan "+angkatan)
            await message.author.add_roles(role_angkatan)
        elif angkatan == "2025":
            role_angkatan = discord.utils.get(message.author.guild.roles, name="Angkatan "+angkatan)
            await message.author.add_roles(role_angkatan)
        else:
            error = True
            await message.channel.send('Tahun Angkatan Tidak Terdaftar di Server')

        if divisi == "pemrograman" or divisi == "pemograman":
            role_divisi = discord.utils.get(message.author.guild.roles, name="Divisi Pemrograman")
            await message.author.add_roles(role_divisi)
        elif divisi == "elektronika" or divisi == "teknisi":
            role_divisi = discord.utils.get(message.author.guild.roles, name="Divisi Elektronika")
            await message.author.add_roles(role_divisi)
        elif divisi == "desain" or divisi == "mekanik" or divisi == "mekanika" or divisi == "desain & mekanik" or divisi == "desain & mekanika" or divisi == "desain dan mekanik" or divisi == "desain & mekanika":
            role_divisi = discord.utils.get(message.author.guild.roles, name="Divisi Desain & Mekanik")
            await message.author.add_roles(role_divisi)
        else:
            error = True
            await message.channel.send('Divisi tidak tersedia/typo, coba lagi.')
        if error != True:
          await message.channel.send('Halo, '+panggilan+'! Selamat bergabung di UKM ROBOTIC divisi '+divisi.title())
    
# keep_alive()
client.run(TOKEN)