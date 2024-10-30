import pytest
import main


# Класс для проверки сортировки
class TestMath:

    # Функция для выполнения теста (a+b)
    @pytest.fixture
    def sum(self):
        return 4,5,'+'

    # Функция для выполнения теста (a-b)
    @pytest.fixture
    def sub(self):
        return 4,5,'-' #-1

    # Функция для выполнения теста (a*b)
    @pytest.fixture
    def mult(self):
        return 20

    # Функция для выполнения теста (a/b)
    @pytest.fixture
    def div(self):
        return 0.8

    # Тестируем программу на корр-х данных (a+b)
    def test_on_sum(self,sum):
        a,b,op = sum
        assert main.math_95945439(a,b,op) == 9

    # Тестируем программу на некорр-х данных (a+b)
    def test_on_unk(self, sum):
        a, b, op = sum
        with pytest.raises(TypeError):
            assert main.math_95945439('4', b, '/') #==9