
from PIL import Image , ImageOps
from io import BytesIO
from django.core.files import File

def process_image(img_path):
    im = Image.open(img_path)

    thumb_io = BytesIO() 
    thum_img = im.resize((200,300))
    thum_img.save(thumb_io, 'png')
    thumbnail = File(thumb_io, name='thum.png')

    medium_img_io = BytesIO() 
    medium_img = im.resize((500,500))
    medium_img.save(medium_img_io, 'png')
    medium_img = File(medium_img_io, name='medium_img.png')

    large_img_io = BytesIO() 
    large_img = im.resize((1024,768))
    large_img.save(large_img_io, 'png')
    large_img = File(large_img_io, name='large_img.png')

    gray_img_io = BytesIO() 
    gray_img = ImageOps.grayscale(im)
    gray_img.save(gray_img_io, 'png')
    gray_img = File(gray_img_io, name='gray_img.png')

    return thumbnail,medium_img,large_img,gray_img