import urllib.request as req
import base64
from PIL import Image
#image_url=input("Enter the url") '''This is for user input,when user suplies the url i have commented this part,but this will work if you uncomment ,and comment the 2 supplied url'''
#image_url ="https://i.ytimg.com/vi/Ks-_Mh1QhMc/hqdefault.jpg"
image_url ="https://auto.ndtvimg.com/car-images/medium/jeep/compass/jeep-compass.jpg?v=2"
req.urlretrieve(image_url, "image1.jpg")
from PIL import Image

image_open = Image.open('image1.jpg')
width, height = image_open.size
print("Size of the image =",width,"*",height)


compression= Image.open("image1.jpg")
compression = compression.resize((320,568),Image.ANTIALIAS)
compression.save("image_after_compression.jpg",optimize=True,quality=95)


with open("image1.jpg","rb") as convert:
    print(base64.b64encode(convert.read()))



