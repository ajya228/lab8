#Создайте словарь, содержащий перечень пары «Название праздника – имя_файла с открыткой к нему». Спросите у пользователя, к какому празднику ему
# нужна открытка и выведите нужную открытку на экран.
from PIL import Image
cards = {
    "новый год": "C:/Users/AlexSash/PycharmProjects/lab8/Images/new_year_card.jpg",
    "день рождения": "C:/Users/AlexSash/PycharmProjects/lab8/Images/birthday_card.jpg",
    "8 марта": "C:/Users/AlexSash/PycharmProjects/lab8/Images/march_8_card.jpg",
    "день защитника отечества": "C:/Users/AlexSash/PycharmProjects/lab8/Images/23_february_card.jpg"
}

holiday = input("Какой праздник вам нужен? ").lower()

if holiday in cards:
    card_file = cards[holiday]
    print(f"Вот открытка к празднику '{holiday}': {card_file}")
    image = Image.open(card_file)
    image.show()
else:
    print("Извините, открытка к этому празднику не найдена.")
