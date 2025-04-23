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


#

# pip install yt-dlp mutagen
# sudo apt install ffmpeg

#import os
#import json
#import yt_dlp
#
#FOLDER_DEST = "./musics"
#METADATA_JSON = "./metadata.json"
#
#os.makedirs(FOLDER_DEST, exist_ok=True)
#
#if os.path.exists(METADATA_JSON):
#    with open(METADATA_JSON, "r", encoding="utf-8") as f:
#        metadata = json.load(f)
#else:
#    metadata = []
#
#idsInMetadata = {m["id"] for m in metadata}

#def get_video_ids(url_playlist):
#    ydl_opts = {
#        "quiet": True,
#        "extract_flat": True,
#        "skip_download": True,
#        "nocheckcertificate": True,
#    }
#
#    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#        info = ydl.extract_info(url_playlist, download=False)
#        return info.get("entries", [])
#
#def download_videos(video_id):
#    ydl_opts = {
#        "format": "m4a/bestaudio/best",
#        "outtmpl": os.path.join(FOLDER_DEST, "%(title)s.%(ext)s"),
#        "quiet": False,
#        "nocheckcertificate": True,
#    }#
#
#    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#        info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=True)
#        videoData = {
#            "id": info.get("id"),
#            "title": info.get("title"),
#            "uploader": info.get("uploader"),
#            "upload_date": info.get("upload_date"),
#            "duration": info.get("duration"),
#            "webpage_url": info.get("webpage_url"),
#        }
#        return videoData
#
#def download_playlist_musics(url_playlist):
#    videos = get_video_ids(url_playlist)
#
#    for video in videos:
#        video_id = video.get("id")
#        if not video_id or video_id in idsInMetadata:
#            print(f"🔁 Skipping: {video.get('title')}")
#            continue

#        try:
#            print(f"Downloading: {video.get('title')}")
#            videoData = download_videos(video_id)
#            metadata.append(videoData)

#            with open(METADATA_JSON, "w", encoding="utf-8") as f:
#                json.dump(metadata, f, indent=4, ensure_ascii=False)
#
#            print(f"✅ Done: {videoData.get('title')}")
#
#        except Exception as e:
#            print(f"❌ Error {video.get('title')}: {e}")
#
#if __name__ == "__main__":
#    url = "https://www.youtube.com/playlist?list=playlistid"
#    download_playlist_musics(url)


