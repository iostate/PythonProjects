import urllib.request

resource = urllib.request.urlopen("http://i0.kym-cdn.com/photos/images/newsfeed/001/248/525/3e4.jpg")

output = open("file01.jpg", "wb")
output.write(resource.read())
output.close()