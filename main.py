import yt_dlp
import ffmpeg
import os

lista_url = [
     'https://youtu.be/3_WKK_YamAo?si=ZyJyfgHAzshHmJ1j',
     'https://youtu.be/28hYUZMufDg?si=uRfcRXKBaaL0oQLY',
     'https://youtu.be/CJOZc02VwJM?si=tWUYkww1Z0KDl3ef',
     'https://youtu.be/r7qovpFAGrQ?si=QMtNCP-b3aTnjcoW',
     ]
tam_lista = len(lista_url)
caminho_video = './audios'
extensao = '*.webm'

yt_opts = {
        'ffmpeg_location':'./ffmpeg/bin',
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
        }],
        'format':'bestaudio/best',
        'outtmpl': f'{caminho_video}/%(title)s.%(ext)s'
}
try:
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        cont=0
        while cont < tam_lista:
             ydl.download([lista_url[cont]])
             print(lista_url[cont].title)
             print("Download concluido com sucesso!")
             cont+=1
except Exception as e:
        print(f"Ocorreu um erro, erro: {e}")
            