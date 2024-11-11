#Скачайте любую открытку из интернета, определите область, которую Вам нужно вырезать из данного изображения (обрезать текст, часть фото и т.д.).
# Напишите программу, которая выполнит эту операцию. Сохраните изображения в текущую папку под новым именем.

from PIL import Image
input_image_path = 'C:/Users/AlexSash/Downloads/otkritka.jpg'
output_image_path = 'C:/Users/AlexSash/PycharmProjects/lab8/Images'

image = Image.open(input_image_path)

cropped_image = image.crop((70, 50, 800, 600))
cropped_image.show()
cropped_image.save(f'{output_image_path}/228.jpg')
print("Saved")
