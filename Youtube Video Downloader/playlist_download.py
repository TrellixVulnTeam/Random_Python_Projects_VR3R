# import pytube
#
# url = 'https://www.youtube.com/playlist?list=PLR_U_GiDWFf0T10BQjdq42JfNRH-DppPN'
#
# playlist = pytube.Playlist(url)
#
# for url in playlist:
#     video = pytube.YouTube(url)
#     stream = video.streams.get_by_itag(18)
#     stream.download()