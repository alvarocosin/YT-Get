#Downloads YouTube video in MP3 format
from pytube import YouTube, Playlist
import os, sys

def DownloadVideo(link, extension, destination):
    yt = YouTube(link)

    if(extension == '.mp3'):
        video = yt.streams.filter(only_audio=True).first()
    else:
        video = yt.streams.get_highest_resolution()
        
    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)

    if(extension == '.mp3'):
        new_file = base + '.mp3'
    else:
        new_file = base + '.mp4'
    os.rename(out_file, new_file)
def DownloadPlaylist(link, extension, destination):
    playlist = Playlist(link)

    videos = list()
    if(extension == '.mp3'):
        for p in playlist.videos:
            p = p.streams.filter(only_audio=True).first().download(output_path=destination)
            base, ext = os.path.splitext(p)
            new_file = base + '.mp3'
            os.rename(p, new_file) 
    else:
        for p in playlist.videos:
            p = p.streams.get_highest_resolution().download(output_path=destination)
            base, ext = os.path.splitext(p)
            new_file = base + '.mp4'
            os.rename(p, new_file)    

if(str(sys.argv[1]) == 'playlist'):
    DownloadPlaylist(str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))
else:
    DownloadVideo(str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))


