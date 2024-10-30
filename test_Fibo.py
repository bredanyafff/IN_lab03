import pytest
import main


# Класс для проверки чисел Фибоначчи
class TestFibo:

    # Функция для выполнения теста (fibo(6))
    @pytest.fixture
    def fibo_six(self):
        return 6

    # Тестируем программу на корр-х данных (fibo(6))
    def test_fibo_six(self,fibo_six):
        assert main.fibo(fibo_six) == 8

    # Тестируем программу на некорр-х данных (fibo(6))
    def test_on_unk(self, ):
        with pytest.raises(TypeError):
            assert main.fibo('6') #==9