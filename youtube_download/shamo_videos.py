from pytube import YouTube
from videos_download import VideosDownload
from user_input import *


def shamo_videos(videos=None, folder_name=None):

    while not (videos):
        try:
            videos = [YouTube(videos) for videos in get_links()]
            break

        except Exception as e:
            print(e)

    download_dir = get_download_dir(folder_name)

    # [print(f"{i+1:^4} | Author: {video.author:.20} | Video title: {video.title:<40} | Length: {seconds_to_min(video.length)}")
    #  for i, video in enumerate(videos)]

    output_text = ""
    for i, video in enumerate(videos):
        author = video.author[:10] + \
            "..." if len(video.author) > 10 else video.author
        title = video.title
        length = seconds_to_min(video.length)
        num = str(i+1)

        output_text += f"{num:<4} | Author: {author:<15} | Length: {length:^5} | Video title: {title}\n"

    print(output_text)

    selected_videos = get_selection(videos)

    download = VideosDownload(selected_videos, download_dir)
    download.filters_prompt()

    if download.filtered:
        download.print_stream_qs()

    download.get_streams_prompt()
    download.print_streams_filesize()
    download.get_download_prompt()


if __name__ == "__main__":
    shamo_videos()
