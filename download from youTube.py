import pytube as p
print('>>>>>>> download video from youTube <<<<<<<'.capitalize())
url = input('Enter the url for video : '.capitalize())
p.YouTube(url).streams.get_highest_resolution().download('D:\PC VEDIO\downloaded by my programme')

