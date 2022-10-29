from PIL import Image
from rembg import remove

input = Image.open('elon.jpeg')
output = remove(input)
output.save('output.png')

# Expected - Progress . . . 

# (env) mahimairaja@Computer DAY_18 % python3 main.py
# Downloading...
# From: https://drive.google.com/uc?id=1tCU5MM1LhRgGou5OpmpjBQbSrYIUoYab
# To: /Users/mahimairaja/.u2net/u2net.onnx
# 100%|████████████████████████████████████████| 176M/176M [00:28<00:00, 6.19MB/s]
