# `Ввод информации пользователем
username = input("Введите имя пользователя: ")
title = input("Введите название заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату выполнения заметки в формате 'день-месяц-год': ")

# Выводим все данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Название заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки в формате 'день-месяц-год'", created_date)
print("Дата выполнениея заметки формате 'день-месяц-год'", issue_date)