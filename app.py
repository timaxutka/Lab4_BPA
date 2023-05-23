from flask import Flask, render_template, request # Импорт модулей из библиотеки Flask

app = Flask(__name__) # Создание экземпляра приложения Flask


@app.route('/') # Декоратор, который связывает путь "/" с функцией home
def home():
    return render_template('home.html') # Отображение страницы из файла home.html


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST': # Проверка, является ли метод запроса POST. Это позволяет определить, была ли отправлена форма на сервер для обработки.
        name = request.form.get('name') # Получение значения поля 'name' из данных формы, отправленной методом POST. Значение сохраняется в переменную name.
        answers = {} # Создание пустого словаря answers, который будет содержать ответы пользователя на вопросы анкеты.
        for i in range(1, 11): # Цикл от 1 до 10
            question = f'question_{i}' # Определяем переменную 'question' конкретным вопросом из файла survey.html
            answer = request.form.get(question) # Получаем значение поля 'question_{i}' из данных формы, отправленной методом POST. Значение сохраняется в переменную answer.
            answers[question] = answer # Сохранение ответа пользователя в словаре answers. Ключом словаря является имя вопроса, а значением - ответ пользователя.

        with open('test.txt', 'a', encoding='utf-8') as file: # Открытие файла 'test.txt' в режиме добавления ('a').
            file.write(f'Имя пользователя: {name}\n\n') # Запись строки с именем пользователя в файл

            for question, answer in answers.items(): # Цикл for, который перебирает пары ключ-значение в словаре answers
                file.write(f'{question}: {answer}\n') # Запись строки в файл, содержащей вопрос и соответствующий ему ответ пользователя
            file.write("\n\n")

        return render_template('thankyou.html') # Этот шаблон будет отображаться после успешной отправки анкеты.
    return render_template('survey.html') # Возврат HTML-шаблона 'survey.html' в качестве ответа на запрос, если метод запроса не является POST. Это отображает анкету для заполнения.


if __name__ == '__main__': # Проверка, является ли текущий модуль основным модулем программы.
    app.run() # Запуск веб-приложения
