#!/bin/bash

# Установка зависимостей
pip install -r requirements.txt

# Запуск тестов и генерация отчета
pytest -vv --html=report.html --self-contained-html