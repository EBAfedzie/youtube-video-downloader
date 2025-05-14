import pytube

try:
    # Ask the user to enter url of YouTube video
    video_url = input('Enter url: ')

    # Create an instance of YouTube video
    video_instance = pytube.YouTube(video_url)
    stream = video_instance.streams.get_highest_resolution()

    # Download the video
    stream.download()
    print("Download completed!")

except Exception as e:
    print(f"An error occurred: {e}")
