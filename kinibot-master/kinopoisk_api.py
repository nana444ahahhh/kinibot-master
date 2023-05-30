import requests
import config
import os


class KinopoiskAPI:
    @staticmethod
    def __get_api_response(film):
        headers = {
            'accept': 'application/json',
            'X-API-KEY': config.KINOPOISK_TOKEN
        }
        response = requests.get(
            f'https://api.kinopoisk.dev/v1.2/movie/search?page=1&limit=10&query={film}',
            headers=headers)
        file = response.json()

        return file

    def download_poster(self, film):

        file = self.__get_api_response(film)
        try:
            for film_name in file["docs"]:
                if film_name["name"].lower() == film.lower():
                    img_data = requests.get(film_name["poster"]).content
            with open('img.jpg', 'wb') as handler:
                handler.write(img_data)
        except requests.exceptions.MissingSchema:
            path = 'img.jpg'
            os.remove(path)
            print("Фотография не найдена")

    def search(self, film):
        file = self.__get_api_response(film)
        print(file)

        res = []
        for film_name in file["docs"]:
            if film_name["name"]:
                if film_name["name"] not in res:
                    res.append(film_name["name"])
        return res

    def get_film_rating(self, film):
        file = self.__get_api_response(film)
        for film_name in file["docs"]:
            if film_name["name"].lower() == film.lower():
                return film_name["rating"]

    def get_film_year(self, film):
        file = self.__get_api_response(film)
        for film_name in file["docs"]:
            if film_name["name"].lower() == film.lower():
                return film_name["year"]

    def get_film_countries(self, film):
        file = self.__get_api_response(film)
        for film_name in file["docs"]:
            if film_name["name"].lower() == film.lower():
                return ", ".join(film_name["countries"])

    def get_film_genres(self, film):
        file = self.__get_api_response(film)
        for film_name in file["docs"]:
            if film_name["name"].lower() == film.lower():
                return ", ".join(film_name["genres"])

    def get_film_short_description(self, film):
        file = self.__get_api_response(film)
        for film_name in file["docs"]:
            if film_name["name"].lower() == film.lower():
                return film_name["shortDescription"]

    def get_film_full_description(self, film):
        file = self.__get_api_response(film)
        for film_name in file["docs"]:
            if film_name["name"].lower() == film.lower():
                return film_name["description"]
