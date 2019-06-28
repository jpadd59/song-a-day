import discord
import random
import datetime
import time

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('G#help'):
        await message.channel.send('```Commands:
                                   'G#time; shows you the current time
                                   'G#enable; used to start sending a song a day')
        
    if message.content.startswith('G#time'):
        from datetime import datetime
        await message.channel.send(datetime.now().strftime('%H:%M'))

    if message.content.startswith('G#enable'):
        await message.channel.send('Enabled! I will give you a song every 24 hours!')
        playing = 'True'

    while playing == 'True':
        songs = [
('```Artist; Oliver Tree                                                                                                  '

'Song; All that                                                                                                                '

'Album; Alien Boy EP                                                                                                      '
          
'Genre; Hip-hop/Rap                                                                                                       '

'Link;``` https://www.youtube.com/watch?v=oztbFSBHXis)'),

('```Artist; Halsey                                                                                                '

'Song; Sorry                                                                                                                '

'Album; Hopeless Fountain Kingdom                                                                                                     '
          
'Genre; Electropop                                                                                                     '

'Link;``` https://www.youtube.com/watch?v=tEnCoocmPQM)'),

('```Artist; Mario Golf                                                                                                '

'Song; Hh                                                                                                                '

'Album; Animal Kingdom                                                                                                     '
          
'Genre; Pop/Indie                                                                                                     '

'Link;``` https://youtube.com/watch?v=yU1qIGD8u0I)'),

('```Artist; My Chemical Romance                                                                                             '

'Song; Im Not Okay (I promise)                                                                                                             '

'Album; Three Cheers for Sweet Revenge                                                                                                   '
          
'Genre; Punk rock/Alternative                                                                                                    '

'Link;``` https://www.youtube.com/watch?v=53EV229jBgk)'),

('```Artist; Hobo Johnson                                                                                                 '

'Song; Creve Coeur 1                                                                                                            '

'Album; The Rise of Hobo Johnson                                                                                                    '
          
'Genre; Hip-hop/Rap                                                                                                       '

'Link;``` https://www.youtube.com/watch?v=iHAUv_vur_Y)'),

('```Artist; Hobo Johnson                                                                                                 '

'Song; Creve Coeur 1                                                                                                            '

'Album; The Rise of Hobo Johnson                                                                                                    '
          
'Genre; Hip-hop/Rap                                                                                                       '

'Link;``` https://www.youtube.com/watch?v=iHAUv_vur_Y)'),

('```Artist; White Zombie ft. Iggy Pop                                                                                                 '

'Song; Black Sunshine                                                                                                            '

'Album; La Sexorcisto: Devil Music Vol. 1                                                                                                    '
          
'Genre; Metal/Groove metal                                                                                                      '

'Link;``` https://www.youtube.com/watch?v=iHAUv_vur_Y)'),

('```Artist; Hobo Johnson                                                                                                 '

'Song; Creve Coeur 1                                                                                                            '

'Album; The Rise of Hobo Johnson                                                                                                    '
          
'Genre; Metal/Groove metal                                                                                                      '

'Link;``` https://www.youtube.com/watch?v=iHAUv_vur_Y)'),

 ]
        await message.channel.send(random.choice(songs))
        time.sleep(86400)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTkxNjUwMDgyMzc4NzQzODEy.XQz3NA.u_Py4Iqu9vdOSvU82VGpuyUzWRs')
