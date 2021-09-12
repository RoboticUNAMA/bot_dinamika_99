import discord
from datetime import datetime
# from keep_alive import keep_alive

TOKEN = 'ODg1NDI4OTE5MDQ0NTcxMTM2.YTm58A.76VzbRD1y0TCEXEWKmSKwBoLxc4'

client = discord.Client()

hadir = []

user = []

myinfo = []

pesan = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # await client.change_presence(activity=discord.Streaming(name='Coding', url='https://www.twitch.tv/UR_TWITCH_GOES_HERE You cant do YT only Twitch.'))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Bang Juna Ngoding~"))

@client.event
async def on_message(message):
    error = False

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!myinfo'):
        myinfo.clear()
        myinfo.append(message.author)
        await message.channel.send(myinfo)

    if message.content.startswith('--help'):
        await message.channel.send('**!hello**\n**!myinfo**\n**!tgl**\n**!jam**\n**!hadir**\n**!cekhadir**\n**!resethadir**')

    # =========================================================================
    # PRIVILEGE
    # =========================================================================
    if message.content.startswith('!alert'):
        role = message.guild.get_role(824197002865803294) # id pengurus
        if role in message.author.roles:
            pengumuman = message.content.split("_")
            pengumuman = pengumuman[1]
            await message.delete()
            await message.channel.send(pengumuman)
        else:
            await message.channel.send('Kamu bukan pengurus!')

    if message.content.startswith('!resethadir'):
        if message.author.id == 287968294869270530: # id juna
            user.clear()
            hadir.clear()
            await message.channel.send('Daftar hadir berhasil di reset')
        else:
            await message.channel.send('Kamu bukan bang <@287968294869270530> !')
    # =========================================================================
    # END OF PRIVILEGE
    # =========================================================================

    # =========================================================================
    # ABSENSI
    # =========================================================================
    if message.content.startswith('!tgl'):
        await message.channel.send("Hari ini tanggal "+datetime.today().strftime('%d-%m-%Y'))
    
    if message.content.startswith('!jam'):
        await message.channel.send("Sekarang pukul "+datetime.today().strftime('%H:%M:%S')+" WIB")

    if message.content.startswith('!cekhadir'):
        await message.channel.send("Daftar Hadir: "+str(datetime.today().strftime('%d-%m-%Y')))
        if len(hadir) == 0:
            await message.channel.send("Belum ada yang hadir, Ketik **!hadir** untuk mengisi absensi.")
        else:    
            await message.channel.send("\n".join(hadir))

    if message.content.startswith('!hadir'):
        role = message.guild.get_role(824901052901359616) # id maru
        if role in message.author.roles:
            if user.count(message.author.name) == 1:
                await message.channel.send("Kamu telah hadir hari ini, ketik **!cekhadir** untuk melihat")
            else:
                user.append(message.author.name)
                hadir.append(str(len(hadir)+1)+". "+message.author.name+" ("+str(datetime.today().strftime('%H:%M:%S'))+")")
                await message.channel.send("Daftar Hadir: "+str(datetime.today().strftime('%d-%m-%Y')))
                await message.channel.send("\n".join(hadir))
        else:
            await message.channel.send("Kamu bukan MARU")
    # =========================================================================
    # END OF ABSENSI
    # =========================================================================

    # =========================================================================
    # INTRO AUTO ROLE
    # =========================================================================
    if message.content.startswith('!Perkenalkan') or message.content.startswith('!perkenalkan'):
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
        elif divisi == "desain" or divisi == "mekanik" or divisi == "mekanika" or divisi == "desain & mekanik" or divisi == "desain & mekanika" or divisi == "desain dan mekanik" or divisi == "desain dan mekanika":
            role_divisi = discord.utils.get(message.author.guild.roles, name="Divisi Desain & Mekanik")
            await message.author.add_roles(role_divisi)
        else:
            error = True
            await message.channel.send('Divisi tidak tersedia/typo, coba lagi.')

        if error != True:
            if divisi == "pemrograman" or divisi == "pemograman":
                await message.channel.send('Halo, '+panggilan+'! Selamat bergabung di UKM ROBOTIC divisi Pemrograman')
            elif divisi == "elektronika" or divisi == "teknisi":
                await message.channel.send('Halo, '+panggilan+'! Selamat bergabung di UKM ROBOTIC divisi Elektronika')
            elif divisi == "desain" or divisi == "mekanik" or divisi == "mekanika" or divisi == "desain & mekanik" or divisi == "desain & mekanika" or divisi == "desain dan mekanik" or divisi == "desain & mekanika":
                await message.channel.send('Halo, '+panggilan+'! Selamat bergabung di UKM ROBOTIC divisi Desain & Mekanik')
    else:
        pesan.clear()
        pesan.append(message.content.split(":"))
        if pesan[0].count("Nama") == 1:
            await message.channel.send('Format tidak sesuai, gunakan prefix **!Perkenalkan**')
    # =========================================================================
    # END OF INTRO AUTO ROLE
    # =========================================================================

# keep_alive()
client.run(TOKEN)