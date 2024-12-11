class Address:


    #класс для представления одного адреса

    def __init__(self, city, street, house, floor):
        self.city = city
        self.street = street
        self.house = int(house)
        self.floor = int(floor)

    def __str__(self):
        return f"Адрес: Улица {self.street} {self.house}, {self.city}, Этаж: {self.floor}"

    def as_key(self):
        #Возвращает объект в виде ключа для поиска дубликатов
        return (self.city, self.street, self.house, self.floor)

