from collections import defaultdict


class Statistics:
    #Класс для вычисления и вывода статистики
    def __init__(self, addresses):
        self.addresses = addresses

    def find_duplicates(self):
        #поиск похожих адресов
        counter = defaultdict(int)
        for address in self.addresses:
            counter[address.as_key()] += 1

        duplicates = {key: count for key, count in counter.items() if count > 1}
        return duplicates

    def floor_statistics(self):
        #собираем информацию для каждого города."""
        stats = defaultdict(lambda: defaultdict(int))
        for address in self.addresses:
            stats[address.city][address.floor] += 1
        return stats

    def print_statistics(self, duplicates, floor_stats):
        #вывод статистики
        print("\nДублирующиеся записи:")
        for (city, street, house, floor), count in duplicates.items():
            print(f"Адрес: {street} {house}, {city}, Этаж: {floor} - {count} вхождений")

        print("\nСтатистика по этажам:")
        for city, floors in floor_stats.items():
            print(f"\n{city}:")
            for floor, count in sorted(floors.items(), key=lambda x: x[0]):
                print(f"{floor} этажный: {count} домов")
