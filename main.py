import unittest # Импорт необходимых модулей
from flask.wrappers import Response
from app import app


class AppTestCase(unittest.TestCase): # Класс AppTestCase является наследником класса unittest.TestCase. Содержит методы (тесты): проверяют функционал приложения
    def setUp(self): # Метод, который выполнится перед каждым методом. Создает клиент Flask, который будет использоваться для отправки HTTP-запросов
        self.app = app.test_client()

    def test_home_route(self): # Тестирование функции, отвечающей за загрузку главной страницы
        response: Response = self.app.get('/') # Отправляем GET-запрос на домашнюю страницу
        self.assertEqual(response.status_code, 200) # Проверяем, что код состояния равен 200
        self.assertIn(str('Пройти анкету'), response.data.decode('utf-8')) # Проверка наличия строки "Пройти анкету" на странице

    def test_survey_route_get(self): # Тестирование функции, отвечающей за загрузку страницы с анкетой
        response: Response = self.app.get('/survey') # Отправляем GET-запрос на страницу с анкетой
        self.assertEqual(response.status_code, 200) # Проверяем, что код состояния равен 200
        self.assertIn(str('Анкета'), response.data.decode('utf-8')) # Проверка наличия строки "Анкета" на странице

    def test_survey_route_post(self): # Тестирование функции, отвечающей за загрузку страницы с анкетой
        form_data = { # Словарь содержащий данные формы, которые будут отправлены в POST запросе
            'name': 'Maksim',
            'question_1': 'Очень просто',
            'question_2': 'Скорее просто',
            'question_3': 'Непонятна',
            'question_4': 'Хороший',
            'question_5': 'Совсем не актуальное',
            'question_6': 'Скорее просто',
            'question_7': 'Нормально',
            'question_8': 'Я не считаю его слишком надежным',
            'question_9': 'Скорее недоволен/льна',
            'question_10': 'Я не знаю',
        }

        response: Response = self.app.post('/survey', data=form_data, follow_redirects=True) # Отправляем GET-запрос на страницу с анкетой
        self.assertEqual(response.status_code, 200) # Проверяем, что код состояния равен 200
        self.assertIn(str('Спасибо за заполнение анкеты!'), response.data.decode('utf-8')) # Проверка наличия строки "Спасибо за заполнение анкеты!" на странице
        self.assertTrue(str('Имя пользователя: Maksim'), response.data.decode('utf-8')) # Проверка наличия уже заполненной формы "Имя пользователя: Maksim" на странице

        with open('test.txt', 'r', encoding='utf-8') as file: # Открытие файла 'test.txt' в режиме чтения ('r').
            file_contents = file.read() # Проверка содержимого файла, чтобы убедиться, что данные были записаны в файл
            self.assertTrue('Имя пользователя: Maksim' in file_contents)
            self.assertTrue('question_1: Очень просто' in file_contents)
            self.assertTrue('question_2: Скорее просто' in file_contents)
            self.assertTrue('question_3: Непонятна' in file_contents)
            self.assertTrue('question_4: Хороший' in file_contents)
            self.assertTrue('question_5: Совсем не актуальное' in file_contents)
            self.assertTrue('question_6: Скорее просто' in file_contents)
            self.assertTrue('question_7: Нормально' in file_contents)
            self.assertTrue('question_8: Я не считаю его слишком надежным' in file_contents)
            self.assertTrue('question_9: Скорее недоволен/льна' in file_contents)
            self.assertTrue('question_10: Я не знаю' in file_contents)

if __name__ == '__main__':
    unittest.main() # запускаем все тесты
