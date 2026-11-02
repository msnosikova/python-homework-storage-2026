#!/usr/bin/env python3

import random
from abc import ABC, abstractmethod

MIN_AGE = 0
MAX_AGE = 114
RETIREMENT_AGE = 62
GENDERS = ["мужской", "женский"]


class Person(ABC):
    """
    Класс человека с его характеристиками.

    :param name: Имя человека.
    :param gender: Пол человека.
    :param age: Возраст.
    """
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


    @property
    def name(self):
        """
        Возвращает имя человека.
        """
        return self.__name


    @name.setter
    def name(self, value):
        """
        Устанавливает имя с валидацией.
        :param value: Имя человека.
        """
        if not isinstance(value, str) or not value.strip():
            print("Ошибка! 'Имя' не должно быть пустым")
            return
        self.__name = value.strip()


    @property
    def gender(self):
        """
        Возвращает пол человека
        """    
        return self.__gender


    @gender.setter
    def gender(self, value):
        """
        Устанавливает пол с валидацией.
        :param value: Пол человека.
        """
        if not isinstance(value, str) or value.strip().lower() not in GENDERS:
            print(f"Ошибка! 'Пол' должен быть одним из: {GENDERS}")
            return
        self.__gender = value.strip().lower()


    @property
    def age(self):
        """
        Возвращает возраст человека.
        """
        return self.__age 


    @age.setter
    def age(self, value):
        """
        Устанавливает возраст с валидацией.

        :param value: Возраст человека.
        """
        try:
            value = int(value)
        except (ValueError, TypeError):
            print("Ошибка! 'Возраст' должно быть целым числом")
            return
        if value < MIN_AGE or value > MAX_AGE:
            print(f"Ошибка! 'Возраст' должен быть в диапазоне от {MIN_AGE} до {MAX_AGE}")
            return
        self.__age = value 


    def get_info(self):
        """
        Возвращает строку с информацией о человеке.

        :return: Строка с описанием.
        """
        return f"Имя: {self.__name}, Пол: {self.__gender}, Возраст: {self.__age} лет"


    def is_adult(self):
        """
        Проверяет, является ли человек совершеннолетним.

        :return: True, если возраст >= 18, иначе False.
        """
        return self.__age >= 18


    @classmethod
    def create_person(cls, name, gender, age):
        """
        Создаёт объект Person через переменные.

        :param name: Имя.
        :param gender: Пол.
        :param age: Возраст.
        :return: Новый объект Person.
        """
        return cls(name=name, gender=gender, age=age)


class Employee(Person):
    """
    Класс сотрудника — наследник Person.
    Добавляет должность, зарплату и расходы.

    :param name: Имя сотрудника.
    :param gender: Пол сотрудника.
    :param age: Возраст сотрудника.
    :param position: Должность сотрудника.
    :param salary: Зарплата сотрудника.
    :param expenses: Расходы в месяц.
    """

    def __init__(self, name, gender, age, position, salary, expenses):
        super().__init__(name, gender, age)
        self.position = position
        self.salary = salary
        self.expenses = expenses


    @property
    def position(self):
        """Возвращает должность сотрудника."""
        return self.__position


    @position.setter
    def position(self, value):
        """
        Устанавливает должность с валидацией.

        :param value: Должность сотрудника.
        """
        if not isinstance(value, str) or not value.strip():
            print("Ошибка! 'Должность' должна быть непустой строкой.")
            return
        self.__position = value.strip()


    @property
    def salary(self):
        """Возвращает зарплату сотрудника."""
        return self.__salary


    @salary.setter
    def salary(self, value):
        """
        Устанавливает зарплату с валидацией.

        :param value: Зарплата сотрудника.
        """
        try:
            value = float(value)
        except (ValueError, TypeError):
            print("Ошибка! 'Зарплата' должна быть числом.")
            return
        if value <= 0:
            print("Ошибка! 'Зарплата' должна быть положительным числом.")
            return
        self.__salary = value


    @property
    def expenses(self):
        """Возвращает расходы в месяц."""
        return self.__expenses


    @expenses.setter
    def expenses(self, value):
        """
        Устанавливает расходы с валидацией.

        :param value: Расходы в месяц.
        """
        try:
            value = float(value)
        except (ValueError, TypeError):
            print("Ошибка! 'Расходы' должны быть числом.")
            return
        if value < 0:
            print("Ошибка! 'Расходы' не могут быть отрицательными.")
            return
        self.__expenses = value


    def get_info(self):
        """
        Возвращает строку с информацией о сотруднике.

        :return: Строка с описанием.
        """
        return f"{super().get_info()}, Должность: {self.__position}, Зарплата: {self.__salary} руб., Расходы: {self.__expenses} руб./мес."


    @abstractmethod
    def work(self):
        """
        Абстрактный метод работы. Должен быть переопределён в наследниках.
        """
        pass


    def income_for_months(self, months):
        """
        Оценивает приток денег за N месяцев.

        :param months: Количество месяцев.
        :return: Сумма притока денег.
        """
        try:
            months = int(months)
        except (ValueError, TypeError):
            print("Ошибка! Количество месяцев должно быть целым числом.")
            return 0
        if months <= 0:
            print("Ошибка! Количество месяцев должно быть положительным.")
            return 0
        return (self.__salary - self.__expenses) * months


    def savings_until_retirement(self):
        """
        Рассчитывает, сколько человек скопит денег до пенсии.

        :return: Сумма накоплений до пенсии.
        """
        years_to_retirement = RETIREMENT_AGE - self.age
        if years_to_retirement <= 0:
            print(f"{self.name} уже достиг пенсионного возраста.")
            return 0
        monthly_savings = self.__salary - self.__expenses
        if monthly_savings <= 0:
            print(f"{self.name} не может копить: расходы превышают или равны зарплате.")
            return 0
        return monthly_savings * 12 * years_to_retirement


    def check_survival(self, months):
        """
        Симулирует жизнь сотрудника в течение N месяцев.
        Если расходы превышают зарплату, показывает, на каком месяце человек умирает.

        :param months: Количество месяцев для проверки.
        """
        try:
            months = int(months)
        except (ValueError, TypeError):
            print("Ошибка! Количество месяцев должно быть целым числом.")
            return
        if months <= 0:
            print("Ошибка! Количество месяцев должно быть положительным.")
            return
        balance = 0
        print(f"Симуляция жизни {self.name} на {months} месяцев:")
        print(f"Зарплата: {self.__salary} руб./мес., Расходы: {self.__expenses} руб./мес.")
        for month in range(1, months + 1):
            balance += self.__salary - self.__expenses
            print(f"Месяц {month}: Баланс = {balance} руб.")

            if balance < 0:
                print(f"{self.name} умер на {month}-м месяце! Не хватило денег, чтобы выжить((")
                return

        print(f"{self.name} живет нормально! Итоговый баланс: {balance} руб.")

class Manager(Employee):
    """
    Менеджер — наследник Employee.
    Добавляет список подчинённых и методы управления ими.

    :param name: Имя менеджера.
    :param gender: Пол менеджера.
    :param age: Возраст менеджера.
    :param position: Должность менеджера.
    :param salary: Зарплата менеджера.
    :param expenses: Расходы менеджера в месяц.
    """

    def __init__(self, name, gender, age, position, salary, expenses):
        super().__init__(name, gender, age, position, salary, expenses)
        self.__subordinates = []  


    def add_subordinate(self, employee):
        """
        Добавляет подчинённого.

        :param employee: Объект сотрудника.
        """
        self.__subordinates.append(employee)
        print(f"{employee.name} добавлен в подчинение к {self.name}.")


    def remove_subordinate(self, employee):
        """
        Удаляет подчинённого.

        :param employee: Объект сотрудника.
        """
        if employee in self.__subordinates:
            self.__subordinates.remove(employee)
            print(f"{employee.name} удалён из подчинения {self.name}.")
        else:
            print(f"{employee.name} не является подчинённым {self.name}.")  


    def hold_meeting(self):
        """Проводит митинг для всех подчинённых."""
        if not self.__subordinates:
            print(f"{self.name} проводит митинг, но подчинённых нет.")
            return
        print(f"{self.name} проводит митинг для {len(self.__subordinates)} подчинённых:")
        for sub in self.__subordinates:
            print(f"  - {sub.name} ({sub.position})")

    def get_info(self):
        """
        Возвращает строку с информацией о менеджере.

        :return: Строка с описанием.
        """
        return f"{super().get_info()}, Подчинённых: {len(self.__subordinates)}"

    def work(self):
        """Менеджер управляет командой."""
        print(f"{self.name} управляет командой из {len(self.__subordinates)} человек.")


class Developer(Employee):
    """
    Разработчик — наследник Employee.
    Добавляет список языков программирования.

    :param name: Имя разработчика.
    :param gender: Пол разработчика.
    :param age: Возраст разработчика.
    :param position: Должность разработчика.
    :param salary: Зарплата разработчика.
    :param expenses: Расходы разработчика в месяц.
    :param languages: Список языков программирования.
    """

    def __init__(self, name, gender, age, position, salary, expenses, languages):
        super().__init__(name, gender, age, position, salary, expenses)
        self.__languages = languages


    def write_code(self):
        """Пишет код на случайном языке из списка."""
        if not self.__languages:
            print(f"{self.name} не знает ни одного языка программирования.")
            return
        lang = random.choice(self.__languages)
        print(f"{self.name} пишет код на языке {lang}.")


    def get_info(self):
        """
        Возвращает строку с информацией о разработчике.

        :return: Строка с описанием.
        """
        return f"{super().get_info()}, Языки: {', '.join(self.__languages)}"


    def work(self):
        """Разработчик пишет код."""
        self.write_code()


class Designer(Employee):
    """
    Дизайнер — наследник Employee.
    Добавляет список инструментов.

    :param name: Имя дизайнера.
    :param gender: Пол дизайнера.
    :param age: Возраст дизайнера.
    :param position: Должность дизайнера.
    :param salary: Зарплата дизайнера.
    :param expenses: Расходы дизайнера в месяц.
    :param tools: Список инструментов.
    """


    def __init__(self, name, gender, age, position, salary, expenses, tools):
        super().__init__(name, gender, age, position, salary, expenses)
        self.__tools = tools


    def create_mockup(self):
        """Создаёт макет с использованием случайного инструмента."""
        if not self.__tools:
            print(f"{self.name} не имеет инструментов для работы.")
            return
        tool = random.choice(self.__tools)
        print(f"{self.name} создаёт макет с помощью {tool}.")


    def get_info(self):
        """
        Возвращает строку с информацией о дизайнере.

        :return: Строка с описанием.
        """
        return f"{super().get_info()}, Инструменты: {', '.join(self.__tools)}"


    def work(self):
        """Дизайнер создаёт макеты."""
        self.create_mockup()


if __name__ == '__main__':
    print("\n Создание через конструктор: ")
    manager = Manager(
        name="Михаил",
        gender="мужской",
        age=28,
        position="Менеджер проектов",
        salary=150000,
        expenses=120000
    )
    developer = Developer(
        name="Николай",
        gender="мужской",
        age=36,
        position="Разработчик",
        salary=120000,
        expenses=80000,
        languages=["Python", "С++", "JavaScript"]
    )
    designer = Designer(
        name="Наташа",
        gender="женский",
        age=24,
        position="Дизайнер",
        salary=100000,
        expenses=95000,
        tools=["Figma", "Photoshop", "Illustrator"]
    )
    print(manager.get_info())
    print(developer.get_info())
    print(designer.get_info())

    print("\n Создание через create_person:")
    person = Person.create_person("Марина", "женский", 27)
    print(person.get_info())

    print("\n Проверка совершеннолетия: ")
    print(f"{manager.name} совершеннолетний: {manager.is_adult()}")
    print(f"{developer.name} совершеннолетняя: {developer.is_adult()}")

    print("\n Управление подчинёнными: ")
    manager.add_subordinate(developer)
    manager.add_subordinate(designer)

    print("\n Митинг:")
    manager.hold_meeting()

    print("\n Полиморфизм: get_info: ")
    employees = [manager, developer, designer]
    for emp in employees:
        print("-", emp.get_info())

    print("Полиморфизм: work: ")
    for emp in employees:
        emp.work()

    print("\n Приток денег за полгода:")
    for emp in employees:
        income = emp.income_for_months(6)
        print(f"- {emp.name}: {income} руб.")

    print("\n Накопления до пенсии: ")
    for emp in employees:
        savings = emp.savings_until_retirement()
        print(f"- {emp.name}: {savings} руб.")

    print("\nСимуляция жизни (6 месяцев):")
    manager.check_survival(6)

    print("\n Проверка выживания: ")
    bad_manager = Manager(
    name="Бедолага студент",
    gender="мужской",
    age=19,
    position="Стажёр",
    salary=30000,
    expenses=40000
    )
    bad_manager.check_survival(6)

    print("\n Валидация полей: ")
    print("Попытка создать человека с недопустимым возрастом:")
    bad_developer = Developer(
    name="Тест",
    gender="мужской",
    age=200,
    position="Тест",
    salary=50000,
    expenses=0,
    languages=["Python"]
    )

    print("Попытка создать человека с недопустимым полом:")
    bad_developer_2 = Developer(
    name="Тест",
    gender="инопланетянин",
    age=25,
    position="Тест",
    salary=50000,
    expenses=0,
    languages=["Python"]
    )

    print("Попытка создать сотрудника с отрицательной зарплатой:")
    вad_designer = Designer(
    name="Тест",
    gender="женский",
    age=50,
    position="Тест",
    salary=-1000,
    expenses=0,
    tools=["Fotoshop"]
    )
