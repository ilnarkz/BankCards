# BankCards

[![Maintainability](https://api.codeclimate.com/v1/badges/9530a2b41aaf6c83a67f/maintainability)](https://codeclimate.com/github/ilnarkz/BankCards/maintainability) [![bank_card](https://github.com/ilnarkz/BankCards/actions/workflows/ci.yaml/badge.svg)](https://github.com/ilnarkz/BankCards/actions/workflows/ci.yaml)

BankCard - это веб-приложение для генерации, просмотра деталей и удаления карт.

1. Установка
1.1 Клонирование репозитория и установка зависимостей

```bash
git clone https://github.com/ilnarkz/BankCards
cd BankCards
```

Установка зависимостей

```bash
make install
```


1.2 Активация виртуального окружения

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Запуск утилиты

```bash
make start
```

## Качество кода

Для проверки качества кода используйте

```bash
make lint
```