from moviepy.editor import VideoFileClip, CompositeVideoClip
import requests
import pathlib


def download_video(url, name):
    response = requests.get(url)
    with open(f'{name}.mp4', 'wb') as v:
        v.write(response.content)


def convert_to_gif(name, size=0.25, speed=1.5):
    video = VideoFileClip(f'{name}.mp4').resize(size).speedx(speed)
    video = CompositeVideoClip([video])
    video.write_gif(f'{name}.gif', fps=15, program='ffmpeg', verbose=False, logger=None, tempfiles=False)
    return f'{pathlib.Path().resolve()}\{name}.gif'


def download_tiktok_and_convert_to_gif(url, name='current', size=0.25, speed=1.5):
    download_video(name=name, url=url)
    return convert_to_gif(name=name, size=size, speed=speed)


if __name__ == '__main__':
    url = input('Please enter the URL: ')
    try:
        print('Please wait... Converting to GIF')
        gif = download_tiktok_and_convert_to_gif(url)
    except Exception:
        print('Error: Wrong URL provided')
    else:
        print('Success! Video was converted to GIF and can be found here: ', gif)
