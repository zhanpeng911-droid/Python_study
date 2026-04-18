from pytesseract import pytesseract

# from PIL import Image
# import pytesseract
# text = pytesseract.image_to_string(Image.open('1.jpeg'), lang='chi_sim')
# print(text)


import tesserocr
from PIL import Image

image = Image.open('1.png')
# 指定使用中文简体语言包
result = tesserocr.image_to_text(image, lang='chi_sim')
print(result)


















