def my_func(name, surname, yy, city, email, phone):
    print(name.capitalize(), surname.capitalize(), yy, city.capitalize(), email, phone)


my_func(name=input('Ваше имя: '), surname=input('Ваша фамилия: '),
        yy=input('Год Вашего рождения: '), city=input('Город проживания: '),
        email=input('email: '), phone=input('Номер телефона: '))
