#Модифицируйте задачу 8.1 так: спросите еще у пользователя, имя того, кого он хочет поздравить, добавьте на заданную открытку текст «…., поздравляю!»,
# где вместо …. вставьте полученное имя  (выведите его разным цветом и шрифтами, посередине вверху или внизу фото). Найдите в сети интернет решение,
# как сделать надпись жирным текстом (по умолчанию, такого параметра нет). Сохраните новую открытку в файл с расширением png.

from PIL import Image, ImageDraw, ImageFont
import os
input_image_path = 'C:/Users/AlexSash/Downloads/otkritka.jpg'
output_image_path = 'C:/Users/AlexSash/PycharmProjects/lab8/Images'

image = Image.open(input_image_path)

cropped_image = image.crop((70, 50, 800, 600))
cropped_image.save(f'{output_image_path}/228.jpg')

name = input("Введите имя человека, которого вы хотите поздравить: ")

draw = ImageDraw.Draw(cropped_image)
font_size = 32

try:
    font = ImageFont.truetype("C:/Users/AlexSash/Downloads/Arial.ttf", font_size)
    font1 = ImageFont.truetype("C:/Users/AlexSash/Downloads/ArialBold.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

text = f"{name}, поздравляю!"
bbox = draw.textbbox((0,0), text, font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

x = (cropped_image.height - text_width) // 2
y = 20

draw.text((x, y), text, font=font, fill = (255, 0, 0))
output_filename = f'congratulation_{name}.png'
output_full_path = os.path.join(output_image_path, output_filename)

cropped_image.save(output_full_path)
print("Saved")
