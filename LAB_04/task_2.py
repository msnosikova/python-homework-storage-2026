#!/usr/bin/env python3

class BankAccount:
    """
    Класс банковского счета.

    :param owner: Имя владельца счета.
    :param init_balance: начальный баланс.
    """
    def __init__(self, owner, init_balance):
        self.__owner = owner
        self.__history = []
        try:
            init_balance = float(init_balance)
        except (ValueError, TypeError):
            print("Ошибка! Баланс должен быть числом.")
            init_balance = 0
        if init_balance < 0:
            print("Ошибка! Баланс должен быть положительным числом.")
            init_balance = 0

        self.__balance = init_balance


    @property
    def owner(self):
        """
        Возвращает имя владельца счета.
        """
        return self.__owner


    @property
    def balance(self):
        """
        Возвращает текущий баланс счета.
        """
        return self.__balance


    @property
    def history(self):
        """
        Возвращает копию истории транзакций
        """
        return self.__history.copy()


    def deposit(self, summa):
        """
        Пополняет счет на определенную сумму.

        :param summa: Сумма пополнения.
        """
        try:
            summa = float(summa)
        except (ValueError, TypeError):
            print("Ошибка! Сумма должна быть числом.")
            return
        if summa <= 0:
            print("Ошибка! Сумма поплнения счета должна быть больше 0.")
            return
        self.__balance += summa
        self.__history.append(f"Пополнение счета на {summa} рублей. Баланс: {self.__balance} рублей.")
        print(f"Счет пополнен на {summa} рублей. Текущий баланс: {self.__balance} рублей.")


    def withdrawal(self, summa):
        """
        Снимает определенную сумму со счета.

        :param summa: Сумма, которую надо снять.
        """
        try:
            summa = float(summa)
        except (ValueError, TypeError):
            print("Ошибка! Сумма должна быть числом.")
            return
        if summa <= 0:
            print("Ошибка! Сумма снятия счета должна быть больше 0.")
            return
        if summa > self.__balance:
            print(f"Ошибка! Недостаточно средств.")
            return
        self.__balance -= summa
        self.__history.append(f"Снятие со счета: {summa} рублей. Баланс: {self.__balance} рублей.")
        print(f"Со счета снято {summa} рублей. Текущий баланс: {self.__balance} рублей.")

        
    def get_info(self):
        """
        Возвращает строку с информацией о счете.

        :return: Строка с описанием.
        """
        return f"Владелец: {self.__owner}, Баланс: {self.__balance} рублей."


    @classmethod
    def from_dict(cls, data):
        """
        Создает объект BankAccount из словаря.

        :param data: словарь с ключами "owner" и "init_balance".
        :return: Новый объект BankAccount.
        """
        return cls(owner=data["owner"], init_balance=data["init_balance"])

    
class SavingAccount(BankAccount):
    """
    Сберегательный счет - наследник BankAccount.
    Добавляет процентную ставку и ограничение на снятие (не более 50% за операцию).

    :param owner: Имя владельца счета.
    :param init_balance: Начальный баланс.
    :param bet: Процентная ставка (% годовых).
    """
    def __init__(self, owner, init_balance, bet):
        super().__init__(owner, init_balance)
        self.__bet = bet


    @property
    def bet(self):
        """
        Возвращает процентную ставку.
        """
        return self.__bet


    def add_procent(self):
        """
        Начисляет проценты на текущий баланс.
        """
        procent = self.balance * (self.__bet / 100)
        self._BankAccount__balance += procent
        self._BankAccount__history.append(f"Начисление процентов: +{procent} рублей. Баланс: {self.balance} рублей.")
        print(f"Начислено {procent} рублей ({self.__bet}%). Текущий баланс: {self.balance} рублей.")


    def withdrawal(self, summa):
        """
        Снимает сумму со счета: не более 50% баланс.

        :param summa: Сумма снятия.
        """
        try:
            summa = float(summa)
        except (ValueError, TypeError):
            print("Ошибка! Сумма должна быть числом.")
            return
        if summa <= 0:
            print("Ошибка! Сумма снятия должна быть больше 0.")
            return
        if summa > self.balance * 0.5:
            print(f"Ошибка! Со сберегательного счета нельзя снять больше 50% от суммы баланса.\n Максимум: {self.balance * 0.5} рублей.")
            return
        if summa > self.balance:
            print(f"Ошибка! Недостаточно средств. Доступно: {self.balance} рублей.")
            return
        self._BankAccount__balance -= summa
        self._BankAccount__history.append(f"Снятие со счета: {summa}рублей. Баланс: {self.balance} рублей.")
        print(f"Со счета снято {summa} рублей. Текущий баланс: {self.balance} рублей.")

    def get_info(self):
        """
        Возвращает строку с информацию о сберегательном счете.

        :return: Строка с описанием.
        """
        return f"{super().get_info()}, Ставка: {self.__bet}%"


if __name__ == '__main__':
    print("\n Через конструктор:")
    account = BankAccount(owner="Акакий", init_balance=15000)
    saving = SavingAccount(owner="Акакий", init_balance= 15000, bet=12)
    print(account.get_info())
    print(saving.get_info())

    print("\n Через from_dict")
    data = {"owner": "Мария", "init_balance": 1000000}
    account_from_dict = BankAccount.from_dict(data)
    print(f"Счет из словаря: {account_from_dict.get_info()}")

    print("\n Корректные операции:")
    account.deposit(550)
    account.withdrawal(1000)
    saving.deposit(5)
    saving.withdrawal(4000)

    print("\n Ошибки операций: \n Попытка пополнить на отрицательную сумму:")
    account.deposit(-125)

    print("\n Попытка снять больше, чем есть на счете:")
    account.withdrawal(20000)

    print("\n Попытка снять со сберегательного счета больше 50%:")
    saving.withdrawal(10000)

    print("\n Попытка изменить баланс счета напрямую:")
    try:
        account.balance = 125000
    except AttributeError as e:
        print(f"Ошибка: {e}")
    print(f"Баланс после попытки изменения: {account.balance}")

    print("\n История операций:")
    print("\n История обычного счета:")
    for action in account.history:
        print("-", action)

    print("\n История сберегательного счета:")
    for action in saving.history:
        print("-", action)

    print("Начисление процентов:")
    saving.add_procent()

    print("Снятие денег")
    accounts = [account, saving]
    for acc in accounts:
        print(f"Попытка снять 5000 рублей со счета {acc.owner}:")
        acc.withdrawal(5000)
