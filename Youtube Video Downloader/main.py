import pytube

video_list = []

print("Enter URLs and to Terminate enter 'START' ")

while True:
    url = input("")
    if url == 'START':
        break
    video_list.append(url)
for x, i in enumerate(video_list):
    v = pytube.YouTube(i)


    for j in v.streams:
        if 'progressive="True"' in str(j):
            print(j)
    itag = int(input("Enter itag to the corresponding resolution: "))
    stream = v.streams.get_by_itag(itag)
    print(f"Downloading video {x + 1}......")
    stream.download()
    print("DONE! ... Output in the same directory as this script")