from exif import Image

with open('image.jpg', 'rb') as image_file:
    my_image = Image(image_file)
    val_dict = my_image.get_all()

for i, j in val_dict.items():
    print(f'{i : <21} : {j}')