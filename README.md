# BankCards

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