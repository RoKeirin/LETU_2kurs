import requests
import webbrowser

class WikipediaSearcher:
    def __init__(self):
        self.base_url = "https://ru.wikipedia.org/w/api.php"

    def get_search_results(self, query):
        params = {
            'action': 'opensearch',
            'search': query,
            'limit': 10,
            'namespace': 0,
            'format': 'json'
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

    def display_results(self, results):
        titles = results[1]
        links = results[3]
        if not titles:
            print("Результаты не найдены. Введите -2, чтобы сделать новый запрос")
            return

        for index, title in enumerate(titles, start=1):
            print(f"{index}: {title}")

        print("Укажите номер статьи (или введите -2 для другого запроса)")

    def open_article(self, link):
        webbrowser.open(link)

    def run(self):
        while True:
            user_input = input("Введите ваш запрос (или введите -1 для окончания работы): ")
            if user_input == "-1":
                print("Работа закончена.")
                break

            results = self.get_search_results(user_input)
            while True:
                self.display_results(results)
                choice = input("Ваш выбор: ")

                if choice == "-2":
                    break
                elif choice.isdigit():
                    index = int(choice) - 1
                    if 0 <= index < len(results[1]):
                        print(f"Opening {results[1][index]} ...")
                        self.open_article(results[3][index])
                    else:
                        print("Некорректный ввод.")
                else:
                    print("Неправильный номер. Пожалуйста, введите правильный номер.")


if __name__ == "__main__":
    searcher = WikipediaSearcher()
    searcher.run()
