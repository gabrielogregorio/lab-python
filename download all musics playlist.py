import yt_dlp as youtube_dl

ref = '0-999'

def baixar_playlist_como_mp3(url_playlist):
    opcoes_ydl = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'playlist_items': ref,
        # 'playlist-start': 1, 
   }

    with youtube_dl.YoutubeDL(opcoes_ydl) as ydl:
        print(ref)
        ydl.download([url_playlist])

link_playlist = "https://www.youtube.com/playlist?list=PLgqgYgA9TzKjh-x60HSZr34gYkZNi9sQP"
baixar_playlist_como_mp3(link_playlist)


