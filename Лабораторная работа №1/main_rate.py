from typing import Union
import doctest

class LiquidRate:
    def __init__(self, rate: Union[int, float]):
        """
        Создание объекта "Дебит жидкости"

        :param rate: Дебит жидкости

        Примеры:
        >>> rate1 = LiquidRate(100) #инициализация экземпляра класса
        >>> rate1 = LiquidRate(-100)
        Traceback (most recent call last):
        ...
        ValueError: Дебит жидкости должен быть положительным числом
        >>> rate1 = LiquidRate("100")
        Traceback (most recent call last):
        ...
        TypeError: Дебит жидкости должен быть типа int или float
        """
        self.rate = None
        self.init_rate(rate)

    def init_rate(self, rate:Union[int, float]):
        """
        Подготовка к работе объекта "Дебит жидкости"

        :param rate: Дебит жидкости
        :raise ValueError: Если дебит жидкости является отрицательным числом, то вызываем ошибку
        """
        if not isinstance(rate, (int, float)):
            raise TypeError("Дебит жидкости должен быть типа int или float")
        if rate <= 0:
            raise ValueError("Дебит жидкости должен быть положительным числом")
        self.rate = rate

    def calculation_rate(self, permeability: Union[int, float], thickness: Union[int, float], viscosity: Union[int, float], reservoir_pressure: Union[int, float], bottom_hole_pressure: Union[int, float]):
        """
        Пересчёт дебита жидкости со своими параметрами"

        :param permeability: Проницаемость
        :param thickness: Толщина пласта
        :param viscosity: Вязкость флюида
        :param reservoir_pressure: Пластовое давление
        :param bottom_hole_pressure: Забойное давление

        :raise ValueError: Если параметр является отрицательным числом, то вызываем ошибку

        :return: Пересчитанный дебит жидкости

        Примеры:
        >>> rate1.calculation_rate(10, 4, 2, 300, 200)
        """

        if not isinstance(permeability, (int, float)):
            raise TypeError("Площадь должна быть типа int или float")
        if permeability <= 0:
            raise ValueError("Площадь должна быть положительным числом")
        if not isinstance(thickness, (int, float)):
            raise TypeError("Нефтенасыщенная толщина должна быть типа int или float")
        if thickness <= 0:
            raise ValueError("Нефтенасыщенная толщина должна быть положительным числом")
        if not isinstance(viscosity, (int, float)):
            raise TypeError("Пористость должна быть типа int или float")
        if viscosity <= 0:
            raise ValueError("Пористость должна быть положительным числом")
        if not isinstance(reservoir_pressure, (int, float)):
            raise TypeError("Пластовое давление должно быть типа int или float")
        if reservoir_pressure <= 0:
            raise ValueError("Пластовое давление должно быть положительным числом")
        if not isinstance(bottom_hole_pressure, (int, float)):
            raise TypeError("Забойное давление должно быть типа int или float")
        if bottom_hole_pressure <= 0:
            raise ValueError("Забойное давление должно быть положительным числом")

        self.rate = permeability * thickness * (reservoir_pressure - bottom_hole_pressure) / (viscosity * 10.13 * 18.41)

    def rate_oil(self, water):
        """
        Расчёт дебита нефти в потоке жидкости

        :param water: Доля воды в потоке (обводненность)
        :return: Дебит нефти
        :raise ValueError: Если дебит жидкости является отрицательным числом или больше 1, то вызываем ошибку

        Пример:
        >>> rate1.rate_oil(0.5)
        >>> rate1.rate_oil(-0.5)
        Traceback (most recent call last):
        ...
        ValueError: Обводненность должна быть положительным числом
        >>> rate1.rate_oil(1.5)
        Traceback (most recent call last):
        ...
        ValueError: Обводненность должна быть меньше 1
        >>> rate1.rate_oil("0.5")
        Traceback (most recent call last):
        ...
        TypeError: Обводненность должна быть типа int или float
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Обводненность должна быть типа int или float")
        if water <= 0:
            raise ValueError("Обводненность должна быть положительным числом")
        if water > 1:
            raise ValueError("Обводненность должна быть меньше 1")
        self.rate = self.rate * (1-water)

rate1 = LiquidRate(100)
print(rate1)
rate1.calculation_rate(10, 4, 2, 300, 200)
print(rate1.rate)
rate1.rate_oil(0.5)
print(rate1.rate)

if __name__ == "__main__":
     doctest.testmod()
     pass
