import time
from file_parser import FileParser
from statistics import Statistics

class Application:

    #основной класс приложения
    def run(self):
        while True:
            user_input = input("\nВведите путь до файла (или '0' для выхода): ").strip()
            if user_input.lower() == '0':
                print("Завершение работы.")
                break

            try:
                start_time = time.time()
                parser = FileParser(user_input)
                addresses = parser.parse()

                if not addresses:
                    print("Файл пуст или содержит ошибки.")
                    continue

                statistics = Statistics(addresses)
                duplicates = statistics.find_duplicates()
                floor_stats = statistics.floor_statistics()
                statistics.print_statistics(duplicates, floor_stats)

                elapsed_time = time.time() - start_time
                print(f"\nВремя обработки файла: {elapsed_time:.2f} секунд")
            except Exception as e:
                print(f"Ошибка обработки файла: {e}")


if __name__ == "__main__":
    app = Application()
    app.run()
