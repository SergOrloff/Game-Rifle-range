# Инструкция по работе с программой "Тир"

## Описание программы
"Тир" — это простая игра, написанная на языке Python с использованием библиотеки Pygame. Цель игры заключается в том, чтобы набрать как можно больше очков, кликая по целям, которые появляются в случайных местах на экране. Вы также можете выбрать уровень сложности, который влияет на размер цели.

## Установка и запуск
Для того, чтобы запустить игру, вам необходимо установить Python и Pygame.

1. Установите Python с официального сайта: https://www.python.org/
2. Установите Pygame: 
   ```shell
   pip install pygame
   ```
3. Скачайте или клонируйте репозиторий с игрой.

## Структура проекта

```
tir_game/
├── img/
│   ├── image.jpg
│   ├── target.png
├── sound/
│   ├── hit.wav
│   ├── end.wav
├── tir_game.py
```

* `img/` - папка с изображениями.
  * `image.jpg` - иконка окна игры.
  * `target.png` - изображение цели.
* `sound/` - папка со звуковыми эффектами.
  * `hit.wav` - звук при попадании по цели.
  * `end.wav` - звук при завершении игры.
* `tir_game.py` - основной файл игры.

## Запуск игры
Для запуска игры выполните команду:
```shell
python tir_game.py
```

## Управление игрой

1. При запуске игры появится диалоговое окно для выбора уровня сложности. Введите один из предложенных уровней:
   - Легкий
   - Нормальный
   - Сложный

2. Игра начнется автоматически. Цель появится в случайной позиции на экране. Вам нужно кликнуть по ней мышкой.

3. За каждое попадание по цели вы получаете одно очко, и цель перемещается в новое случайное место.

4. Время игры ограничено 30 секундами. Оставшееся время и текущий счет отображаются в верхнем левом углу экрана.

5. Игра заканчивается, когда время истекает. Появится финальная заставка с вашим результатом и предложением выйти из игры.

## Завершение игры
После завершения игры вы можете закрыть окно, или кликнуть по экрану, чтобы завершить программу.

## Пример использования
```shell
python tir_game.py
```

## Примечания
- Убедитесь, что все необходимые файлы (изображения и звуковые эффекты) находятся в соответствующих папках (`img/` и `sound/`).
- Если у вас возникли проблемы с запуском игры, проверьте установку Pygame и правильность путей к файлам.

## Лицензия
Эта игра предоставляется "как есть" без каких-либо гарантий. Используйте на свой страх и риск.

## Авторы
Автор программы: **Сергей Орлов**

## Контакты
Если у вас есть вопросы или предложения, вы можете связаться с автором по электронной почте: ***6202818@gmail.com***