---
# Front matter
title: "Математические основы защиты информации и информационной безопасности. Отчет по лабораторной работе №2"
subtitle: "Шифры перестановки"
author: "Лубышева Ярослава Михайловна"
group: NFImd-01-23
institute: RUDN University, Moscow, Russian Federation

# Generic otions
lang: ru-RU
toc-title: "Содержание"

# Bibliography
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

# Pdf output format
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
### Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Misc options
indent: true
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text

---

# Цель работы
Выполнить задание к лабораторной работе № 2 [1].

# Задание
1) Изучить шифры перестановки: маршрутное шифрование, шифрование с помощью решеток, шифр по талице Виженера.
2) Реализовать программно каждый шифр.

# Выполнение лабораторной работы
Для реализации каждого вида шифрования была написана программа на языке программирования Python (@fig:1 - @fig:4).

![Первая часть программной реализации шифров](images/1.jpg){#fig:1 width=100%} 

![Программная реализация маршрутного шифрования](images/2.jpg){#fig:2 width=100%} 

![Программная реализация шифрования с помощью решеток](images/3.jpg){#fig:3 width=100%} 

![Программная реализация шифра по талице Виженера](images/4.jpg){#fig:4 width=100%} 


Результаты работы маршрутного шифрования представлены на следующем рисунке (@fig:5).

![Результат работы программы для маршрутного шифрования](images/5.jpg){#fig:5 width=100%}


Результаты работы шифрования с помощью решеток представлены на следующем рисунке (@fig:6).

![Результат работы программы для шифрования с помощью решеток](images/6.jpg){#fig:6 width=100%}


Результаты работы шифра по талице Виженера представлены на следующем рисунке (@fig:7).

![Результат работы программы для шифра по талице Виженера](images/7.jpg){#fig:7 width=100%}

# Выводы
Выполнено задание к лабораторной работе № 2. 

# Список литературы
1. Методические материалы курса
