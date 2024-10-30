import pytest
import main


# Класс для проверки сортировки
class TestSorting:

    # Функция для выполнения теста (от мин. к макс. список)
    @pytest.fixture
    def ordered_example(self):
        return [1, 2, 3]

    # Функция для выполнения теста (неупорядоченный список)
    @pytest.fixture
    def unordered_example(self):
        return [1, 3, 2]

    # Функция для выполнения теста (равн.)
    @pytest.fixture
    def equal_example(self):
        return [1, 1, 1]

    # Тестируем программу на корр-х данных (упорядоченных от мин. к макс.)
    def test_on_ordered(self,ordered_example):
        assert main.sort(ordered_example) == [1, 2, 3]

    # Тестируем программу на корр-х данных (неупорядоченных значениях)
    def test_on_unordered(self,unordered_example):
        assert main.sort(unordered_example) == [1, 2, 3]

    # Тест функции на равных по величине значениях
    def test_on_equal(self, equal_example):
        assert main.sort(equal_example) == [1, 1, 1]

    # Тест с неккор. данными
    def test_on_int_input(self):
        with pytest.raises(TypeError):
            main.sort(123)