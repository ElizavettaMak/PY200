from typing import Union
import doctest

class OilReserves:
    def __init__(self, reserves: Union[int, float]):
        """
        Создание объекта "Запасы нефти"

        :param reserves: Запасы нефти

        Примеры:
        >>> oil = OilReserves(100) #инициализация экземпляра класса
        >>> oil = OilReserves(-100)
        Traceback (most recent call last):
        ...
        ValueError: Запасы должны быть положительным числом
        >>> oil = OilReserves("100")
        Traceback (most recent call last):
        ...
        TypeError: Запасы должны быть типа int или float
        """
        self.reserves = None
        self.init_reserves(reserves)

    def init_reserves(self, reserves:Union[int, float]):
        """
        Подготовка к работе объекта "Запасы нефти"

        :param reserves: Запасы нефти
        :raise ValueError: Если запасы нефти являются отрицательным числом, то вызываем ошибку
        """
        if not isinstance(reserves, (int, float)):
            raise TypeError("Запасы должны быть типа int или float")
        if reserves <= 0:
            raise ValueError("Запасы должны быть положительным числом")
        self.reserves = reserves

    def calculation_reserves(self, area: Union[int, float], thickness: Union[int, float], porosity: Union[int, float], solution: Union[int, float], conversion_factor: Union[int, float]):
        """
        Пересчёт запасов нефти со своими параметрами"

        :param area: Площадь нефтяной залежи
        :param thickness: Нефтенасыщенная толщина пласта
        :param porosity: Пористость пласта
        :param solution: Доля насыщенности пласта нефтью
        :param conversion_factor: Пересчётный коэффициент из пластовых условий в стандартные

        :raise ValueError: Если параметр является отрицательным числом, то вызываем ошибку

        :return: Пересчитанные запасы нефти

        Примеры:
        >>> oil.calculation_reserves(1000, 4, 0.15, 0.6, 0.8)
        """

        if not isinstance(area, (int, float)):
            raise TypeError("Площадь должна быть типа int или float")
        if area <= 0:
            raise ValueError("Площадь должна быть положительным числом")
        if not isinstance(thickness, (int, float)):
            raise TypeError("Нефтенасыщенная толщина должна быть типа int или float")
        if thickness <= 0:
            raise ValueError("Нефтенасыщенная толщина должна быть положительным числом")
        if not isinstance(porosity, (int, float)):
            raise TypeError("Пористость должна быть типа int или float")
        if porosity <= 0:
            raise ValueError("Пористость должна быть положительным числом")
        if porosity > 1:
            raise ValueError("Пористость должна быть меньше 1")
        if not isinstance(solution, (int, float)):
            raise TypeError("Насыщенность пласта должна быть типа int или float")
        if solution <= 0:
            raise ValueError("Насыщенность пласта должна быть положительным числом")
        if solution > 1:
            raise ValueError("Насыщенность пласта должна быть меньше 1")
        if not isinstance(conversion_factor, (int, float)):
            raise TypeError("Пересчетный коэффициент должен быть типа int или float")
        if conversion_factor <= 0:
            raise ValueError("Пересчетный коэффициент должен быть положительным числом")
        if conversion_factor > 1:
            raise ValueError("Пересчетный коэффициент должен быть меньше 1")
        self.reserves = area * thickness * porosity * solution * conversion_factor

    def reserves_geological_tonn(self, density):
        """
        Перевод запасов нефти из куб.м в тонны

        :param density: Плотность нефти в стандартных условиях
        :return: Запасы нефти в тоннах
        :raise ValueError: Если плотность является отрицательным числом или больше 1, то вызываем ошибку

        Пример:
        >>> oil.reserves_geological_tonn(0.8)
        >>> oil.reserves_geological_tonn(-0.8)
        Traceback (most recent call last):
        ...
        ValueError: Плотность должна быть положительным числом
        >>> oil.reserves_geological_tonn(1.8)
        Traceback (most recent call last):
        ...
        ValueError: Плотность должна быть меньше 1
        """
        if not isinstance(density, (int, float)):
            raise TypeError("Плотность должна быть типа int или float")
        if density <= 0:
            raise ValueError("Плотность должна быть положительным числом")
        if density > 1:
            raise ValueError("Плотность должна быть меньше 1")
        self.reserves = self.reserves * density

    def reserves_recoverable(self, recovery_factor):
        """
        Расчёт извлекаемых запасов нефти

        :param recovery_factor: Коэффициент извлечения нефти
        :return: Начальные извлекаемые запасы
        :raise ValueError: Если коэффициент извлечения нефти является отрицательным числом или больше 1, то вызываем ошибку

        Пример:
        >>> oil.reserves_recoverable(0.9)
        >>> oil.reserves_recoverable(-0.9)
        Traceback (most recent call last):
        ...
        ValueError: Коэффициент извлечения нефти должен положительным числом
        >>> oil.reserves_recoverable(1.9)
        Traceback (most recent call last):
        ...
        ValueError: Коэффициент извлечения нефти должен быть меньше 1
        """
        if not isinstance(recovery_factor, (int, float)):
            raise TypeError("Коэффициент извлечения нефти должен быть типа int или float")
        if recovery_factor <= 0:
            raise ValueError("Коэффициент извлечения нефти должен положительным числом")
        if recovery_factor > 1:
            raise ValueError("Коэффициент извлечения нефти должен быть меньше 1")
        self.reserves = self.reserves * recovery_factor

    def reserves_recoverable_remaining(self, cumulative_oil_production):
        """
        Расчёт остаточных запасов нефти

        :param cumulative_oil_production: Накопленная добыча нефти
        :return: Остаточные запасы нефти
        :raise ValueError: Если накопленная добыча нефти является отрицательным числом или больше запасов в пласте, то вызываем ошибку

        Пример:
        >>> oil.reserves_recoverable_remaining(10)
        >>> oil.reserves_recoverable_remaining(-10)
        Traceback (most recent call last):
        ...
        ValueError: Накопленная добыча нефти должна быть положительным числом
        >>> oil.reserves_recoverable_remaining("10")
        Traceback (most recent call last):
        ...
        TypeError: Накопленная добыча нефти должна быть типа int или float
        """
        if not isinstance(cumulative_oil_production, (int, float)):
            raise TypeError("Накопленная добыча нефти должна быть типа int или float")
        if cumulative_oil_production <= 0:
            raise ValueError("Накопленная добыча нефти должна быть положительным числом")
        if self.reserves < cumulative_oil_production:
            raise ValueError("Ошибка! Накопленная добыча нефти не может быть больше извлекаемых запасов")
        self.reserves -= cumulative_oil_production

oil = OilReserves(100)
oil.reserves_geological_tonn(0.8)
print(oil.reserves)
oil.reserves_recoverable(0.9)
print(oil.reserves)
oil.reserves_recoverable_remaining(10)
print(oil.reserves)
oil.calculation_reserves(1000, 4, 0.15, 0.6, 0.8)
print(oil.reserves)
oil.reserves_recoverable(0.5)
print(oil.reserves)
oil.reserves_recoverable_remaining(10)
print(oil.reserves)

if __name__ == "__main__":
     doctest.testmod()
     pass
