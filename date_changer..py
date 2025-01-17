username = "Гость"
title = "Памятка"
content = "совершить важный звонок к вечеру"
status = "Статус заметки"
created_date = "17-01-2025"
issue_date = "17-01-2025"
temp_issue_date = created_date[: 5]
temp_created_date = issue_date[: 5]
print("Имя пользователя: ", username)
print("Название заметки: ", title)
print("Описание заиетки: ", content)
print("Статус заметки: ", status)
print("Дата создания заметки: ", temp_created_date)
print("Дата выполнения заметки: ", temp_issue_date)