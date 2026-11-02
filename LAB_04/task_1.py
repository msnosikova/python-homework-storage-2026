#!/usr/bin/env python3

MAX_SPEED = 300
MIN_SPEED = 0
MAX_CAPACITY = 200
MIN_CAPACITY = 1

class Transport:
    """
    Класс транспортного средства.

    :param speed: скорость транспорта (км/ч)
    :param capacity: вместимость транспорта (количество мест)
    """
    def __init__(self, speed, capacity):
        self.__speed = MIN_SPEED
        self.__capacity = MIN_CAPACITY
        self.speed = speed
        self.capacity = capacity

    @property
    def speed(self):
        """
        Возвращает текущую скорость транспорта
        """
        return self.__speed


    @speed.setter
    def speed(self, value):
        """
        Устанавливает скорость и проверяет её корректность. 

        :param value: Новое значение скорости
        """
        try:
            value = int(value)
        except (ValueError, TypeError):
            print(f"Ошибка!\n Значение скорости должно быть целым числом.")
            return
        if value < MIN_SPEED or value > MAX_SPEED:
            print(f"Ошибка!\n Скорость должна быть в диапазоне от {MIN_SPEED} до {MAX_SPEED}")
            return
        self.__speed = value


    @property
    def capacity(self):
        """
        Возвращает текущую вместимость транспорта
        """
        return self.__capacity


    @capacity.setter 
    def capacity(self, value):
        """
        Устанавливает вместимость и проверяет её корректность.

        :param value: Новое значение вместимости
        """
        try:
            value = int(value)
        except (ValueError, TypeError):
            print(f"Ошибка!\n Вместимость жолжна быть целым числом.")
            return
        if value < MIN_CAPACITY or value > MAX_CAPACITY:
            print(f"Ошибка:\n вместимость должна быть в диапазоне от {MIN_CAPACITY} до {MAX_CAPACITY}")
            return
        self.__capacity = value


    def get_info(self):
        """
        Возвращает строку с характеристиками транспорта

        :return: Строка с описанием
        """ 
        return f"Скорость: {self.__speed} км/ч \n Вместимость: {self.__capacity}"


    def is_speed_exceeded(self, limit):
        """
        Проверка предела разрешенной скорости. 

        :param limit: Пороговое значение скорости
        :return: True, если скорость выше порога, иначе - False
        """ 
        return self.__speed > limit


    @classmethod
    def from_dict(cls, data):
        """
        Создает объект Transort из словаря. Необходимо для уникальных параметров для этого дочернего класса.

        :param data: Словарь с ключами "speed", "capacity", "route"
        :return: Новый объект bus
        """
        return cls(speed = data["speed"], capacity = data["capacity"])


class Bus(Transport):
    """
    Автобус - наследник Transport.
    Добавляет маршрут

    :param speed: Скорость (км/ч)
    :param capacity: Вместимость (количество мест)
    :param route: Маршрут автобуса
    """
    def __init__(self, speed, capacity, route):
        super().__init__(speed, capacity)
        self.__route = route


    @property
    def route(self):
        """
        Возвращает маршрут автобуса
        """
        return self.__route


    @classmethod
    def from_dict(cls, data):
        """
        Создает объект Bus из словаря

        :param data: Словарь с ключами "speed", "capacity", "route"
        :return: Новый объект Bus
        """
        return cls(
            speed=data["speed"],
            capacity=data["capacity"],
            route=data["route"]
        )
    

    def get_info(self):
        """
        Возвращает строку с характеристиками автобуса

        :return: Строка с описанием
        """
        return f"{super().get_info()},\n Маршрут: {self.__route}"


class Truck(Transport):
    """
    Грузовик - наследник Transort.
    Добавляет грузоподъемность и расчет стоимости перевозки.

    :param speed: Скорость (км/ч)
    :param capacity: Вместимость (количество мест)
    :param load_capacity: Грузоподъемность (т)
    """

    def __init__(self, speed, capacity, load_capacity):
        super().__init__(speed, capacity)
        self.load_capacity = load_capacity


    def calculate_delivery_cost(self, distance, price_for_km):
        """
        Рассчитывает стоимость перевозки 

        :param distance: Расстояние в км
        :param price_for_km: Цена за км
        :return: Стоимость перевозки
        """
        return distance * price_for_km


    def get_info(self):
        """
        Возвращает строку с характеристиками грузовика

        :return: Строка с описанием
        """
        return f"{super().get_info()}, \n Грузоподъемность: {self.load_capacity} тонн"


class Taxi(Transport):
    """
    Такси - наследник Transort.
    Добавляет тариф и расчет стоимости поездки.

    :param speed: Скорость (км/ч)
    :param capacity: Вместимость (количетсво мест)
    :param rate: Тариф за километр
    """
    def __init__(self, speed, capacity, rate):
        super().__init__(speed, capacity)
        self.rate = rate 

    def calculate_trip_cost(self, distance):
        """
        Рассчитывает стоимость поездки.

        :param distance: Расстояние в км
        :return: Стоимость поездки
        """
        return distance * self.rate


    def get_info(self):
        """
        Возвращает строку с характеристиками такси
        :return: Строка с описанием
        """
        return f"{super().get_info()},\n Тариф: {self.rate} рублей/км"


if __name__ == '__main__':
    print("Создание через конструктор:")
    bus = Bus(speed=65, capacity=52, route="Санкт-Петербург - Великий Новгород")
    truck = Truck(speed=45, capacity=1, load_capacity=11.50)
    taxi = Taxi(speed=75, capacity=4, rate = 20.15)

    print(bus.get_info())
    print(truck.get_info())
    print(taxi.get_info())


    print("Создание через классовый метод")
    data_bus = {"speed": 68, "capacity": 45, "route": "Санкт-Петербург - Великий Новгород"}
    bus_from_dict = Bus.from_dict(data_bus)
    print(f"Автобус из словаря: {bus_from_dict.get_info()}")

    data_transport = {"speed": 100, "capacity": 4}
    transport_from_dict = Transport.from_dict(data_transport)
    print(f"Транспорт из словаря: {transport_from_dict.get_info()}")


    print("Попытка задать недопустимую скорость или вместимость")  
    bad_transport_1 = Transport(speed=30, capacity=0)
    print(f"Результат: {bad_transport_1.get_info()}")
    bad_transport_2 = Transport(speed=1000, capacity=25)
    print(f"Результат: {bad_transport_2.get_info()}")


    print("Вызов методов без создания объекта")
    try: 
        Transport.get_info()
    except TypeError as i:
        print(f"Ошибка: {i}")


    print("Полиморфный вызов методов для списка разных транспортных средств")
    many_transort = [bus, truck, taxi]
    print("Информация о всех транспортных средствах:")
    for t in many_transort:
        print( "--", t.get_info())

    print("Проверка превышения скорости (порог 60 км/ч):")
    for t in many_transort:
        exceeded = t.is_speed_exceeded(60)
        print(f" - {t.__class__.__name__}: {'превысил' if exceeded else 'не превысил'}")

    print("Расчет стоимости поездки на 150 км")
    print(f" - Грузовик: {truck.calculate_delivery_cost(150, 18.04)} руб")
    print(f"- Такси: {taxi.calculate_trip_cost(100)} руб")
