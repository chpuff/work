---
## Front matter
lang: ru-RU
title: Информационная безопасность. Лабораторная работа № 7 на тему "Элементы криптографии. Однократное гаммирование"
author: Горбунова Ярослава Михайловна
group: NFIbd-01-19
institute: RUDN University, Moscow, Russian Federation

## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

# Содержание
* Цели и задачи
* Выполнение
* Результаты
* Список литературы

# Цели и задачи
Освоить на практике применение режима однократного гаммирования

# Выполнение
## Выполнение
![Схема однократного использования Вернама](images/scheme.jpg)

## Выполнение
![Формула 7.1](images/71.jpg)

![Формула 7.2](images/72.jpg)

где C_i — i-й символ получившегося зашифрованного послания, P_i — i-й
символ открытого текста, K_i — i-й символ ключа, i = 1, m. Размерности
открытого текста и ключа должны совпадать, и полученный шифротекст
будет такой же длины

## Выполнение
![Программа (1)](images/1.jpg){#fig:1 width=100%}

## Выполнение
![Программа (2)](images/2.jpg){#fig:2 width=100%}

## Выполнение
![Программа (3)](images/3.jpg){#fig:3 width=100%}

## Выполнение
![Вывод работы программы](images/4.jpg){#fig:4 width=100%}

# Результаты
Освоено на практике применение режима однократного гаммирования

# Список литературы
1. Методические материалы курса
