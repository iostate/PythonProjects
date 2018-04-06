# # Dependency for album cover download
# from urllib import request
#
# thumbnail_path = "https://i.ytimg.com/vi/uijHb5U1pD8/default.jpg"
# album_cover = request.urlretrieve(thumbnail_path, "albumcover.jpg")

import requests
f = open('image.jpg', 'wb')
f.write(requests.get('https://i.ytimg.com/vi/uijHb5U1pD8/default.jpg').content)
f.close()