import os
import requests
from bs4 import BeautifulSoup
import moviepy.editor as mp
import random


def download_file(url):
    local_filename = url.split('/')[-1]
    if os.path.exists(local_filename):
        return local_filename

    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:   # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename


def get_videos(q):
    downloaded_videos = []

    url = 'https://www.shutterstock.com/video/search/?searchterm=' + q
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    videos = soup.select('li.clip-item')
    # for video in videos:
    for video in videos[0:3]:
        src = video.get('data-preview_url')
        src = 'http:' + src
        print src
        filename = download_file(src)
        downloaded_videos.append(filename)

    return downloaded_videos


def mash(phrase1, phrase2, outfile=None):
    phrase1_videos = get_videos(phrase1)
    phrase2_videos = get_videos(phrase2)
    videos = phrase1_videos + phrase2_videos
    random.shuffle(videos)

    clips = []
    for video in videos:
        clip = mp.VideoFileClip(video)
        start = clip.duration / 2
        clip = clip.subclip(start, start + 0.3)
        clips.append(clip)

    if outfile is None:
        outfile = phrase1 + phrase2 + '.mp4'
        outfile = outfile.replace(' ', '_')

    composite = mp.concatenate_videoclips(clips, method='compose')
    composite.write_videofile(outfile, fps=24)


if __name__ == '__main__':
    from sys import argv

    mash(argv[1], argv[2])
