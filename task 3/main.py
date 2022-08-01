"""Test of the library."""


from csvfilms.editor import Editor
from csvfilms.film import Film, best_top, worst_top, average_rating

FILE_NAME = 'фільми.csv'

# читання фільмів
film_file_editor = Editor(Film, FILE_NAME)
film_file_editor.read()

films = film_file_editor.items

# відображення фільмів
print('\n----------------------------------------фільми')
for film in films:
    print(film, end='\n\n')

# видалення фільму із файлу
film_file_editor.remove(2)
# додавання нового фільму у файл
film_file_editor.add(Film('new_film', 'cool film', '4.9'))

# відображення фільмів після змін
print('\n------------------------фільми після оновлення')
for film in films:
    print(film, end='\n\n')

# порівняння фільмів
print('\n--------------------Топ 5 з найвищим рейтингом')
for film in best_top(films):
    print(film, end='\n\n')
print('\n-------------------Топ 5 з найнижчим рейтингом')
for film in worst_top(films):
    print(film, end='\n\n')
print('\n-------------Середній рейтинг серед фільмів = ', average_rating(films))
