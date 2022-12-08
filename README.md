# BankCards

[![bank_card](https://github.com/ilnarkz/BankCards/actions/workflows/ci.yaml/badge.svg)](https://github.com/ilnarkz/BankCards/actions/workflows/ci.yaml) [![Maintainability](https://api.codeclimate.com/v1/badges/d89821910d9df7dea9d5/maintainability)](https://codeclimate.com/github/ilnarkz/BankCards/maintainability)

BankCard - это веб-приложение для генерации, активирования/деактивирования, просмотра деталей и удаления карт.

[BankCard on Railway](https://web-production-04b6.up.railway.app/)

## 1. Установка
### 1.1 Клонирование репозитория и установка зависимостей

```bash
git clone https://github.com/ilnarkz/BankCards
cd BankCards
```

Установка зависимостей

```bash
make install
```


### 1.2 Активация виртуального окружения

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Запуск утилиты

```bash
make start
```

### Качество кода

Для проверки качества кода используйте

```bash
make lint
```