from typing import Union
import doctest

class GasReserves:
    def __init__(self, reserves: Union[int, float]):
        """
        Создание объекта "Запасы газа"

        :param reserves: Запасы газа

        Примеры:
        >>> gas = GasReserves(100) #инициализация экземпляра класса
        >>> gas = GasReserves(-100)
        Traceback (most recent call last):
        ...
        ValueError: Запасы должны быть положительным числом
        >>> gas = GasReserves("100")
        Traceback (most recent call last):
        ...
        TypeError: Запасы должны быть типа int или float
        """

        self.reserves = None
        self.init_reserves(reserves)

    def init_reserves(self, reserves: Union[int, float]):
        """
        Подготовка к работе объекта "Запасы газа"

        :param reserves: Запасы газа
        :raise ValueError: Если запасы газа являются отрицательным числом, то вызываем ошибку
        """

        if not isinstance(reserves, (int, float)):
            raise TypeError("Запасы должны быть типа int или float")
        if reserves <= 0:
            raise ValueError("Запасы должны быть положительным числом")
        self.reserves = reserves

    def calculation_reserves(self, area: Union[int, float], thickness: Union[int, float], porosity: Union[int, float], solution: Union[int, float], conversion_factor: Union[int, float], reservoir_pressure: Union[int, float]):
        """
        Пересчёт запасов газа со своими параметрами"

        :param area: Площадь газовой залежи
        :param thickness: Газонасыщенная толщина пласта
        :param porosity: Пористость пласта
        :param solution: Доля насыщенности пласта газом
        :param conversion_factor: Пересчётный коэффициент из пластовых условий в стандартные

        :raise ValueError: Если параметр является отрицательным числом, то вызываем ошибку

        :return: Пересчитанные запасы газа

        Примеры:
        >>> gas.calculation_reserves(1000, 4, 0.15, 0.6, 0.8, 40)
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
        if not isinstance(reservoir_pressure, (int, float)):
            raise TypeError("Пластовое давление должно быть типа int или float")
        if reservoir_pressure <= 0:
            raise ValueError("Пластовое давление должно быть положительным числом")
        self.reserves = area * thickness * porosity * solution * conversion_factor * (reservoir_pressure - 1)

    def reserves_recoverable(self, recovery_factor):
        """
        Расчёт извлекаемых запасов газа

        :param recovery_factor: Коэффициент извлечения газа
        :return: Начальные извлекаемые запасы
        :raise ValueError: Если коэффициент извлечения газа является отрицательным числом или больше 1, то вызываем ошибку

        Пример:
        >>> gas.reserves_recoverable(0.9)
        >>> gas.reserves_recoverable(-0.9)
        Traceback (most recent call last):
        ...
        ValueError: Коэффициент извлечения газа должен положительным числом
        >>> gas.reserves_recoverable(1.9)
        Traceback (most recent call last):
        ...
        ValueError: Коэффициент извлечения газа должен быть меньше 1
        """
        if not isinstance(recovery_factor, (int, float)):
            raise TypeError("Коэффициент извлечения газа должен быть типа int или float")
        if recovery_factor <= 0:
            raise ValueError("Коэффициент извлечения газа должен положительным числом")
        if recovery_factor > 1:
            raise ValueError("Коэффициент извлечения газа должен быть меньше 1")
        self.reserves = self.reserves * recovery_factor

    def reserves_recoverable_remaining(self, cumulative_gas_production):
        """
        Расчёт остаточных запасов газа

        :param cumulative_gas_production: Накопленная добыча газа
        :return: Остаточные запасы газа
        :raise ValueError: Если накопленная добыча газа является отрицательным числом или больше запасов в пласте, то вызываем ошибку

        Пример:
        >>> gas.reserves_recoverable_remaining(10)
        >>> gas.reserves_recoverable_remaining(-10)
        Traceback (most recent call last):
        ...
        ValueError: Накопленная добыча газа должна быть положительным числом
        >>> gas.reserves_recoverable_remaining("10")
        Traceback (most recent call last):
        ...
        TypeError: Накопленная добыча газа должна быть типа int или float
        """
        if not isinstance(cumulative_gas_production, (int, float)):
            raise TypeError("Накопленная добыча газа должна быть типа int или float")
        if cumulative_gas_production <= 0:
            raise ValueError("Накопленная добыча газа должна быть положительным числом")
        if self.reserves < cumulative_gas_production:
            raise ValueError("Ошибка! Накопленная добыча газа не может быть больше извлекаемых запасов")
        self.reserves -= cumulative_gas_production

gas = GasReserves(100)
gas.reserves_recoverable(0.9)
print(gas.reserves)
gas.reserves_recoverable_remaining(10)
print(gas.reserves)
gas.calculation_reserves(1000, 4, 0.15, 0.6, 0.8, 40)
print(gas.reserves)
gas.reserves_recoverable(0.5)
print(gas.reserves)
gas.reserves_recoverable_remaining(1000)
print(gas.reserves)

if __name__ == "__main__":
     doctest.testmod()
     pass
