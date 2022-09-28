---
# Front matter
title: "Информационная безопасность. Отчет по лабораторной работе № 4"
subtitle: "Дискреционное разграничение прав в Linux. Расширенные атрибуты"
author: "Горбунова Ярослава Михайловна"
group: NFIbd-01-19
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
Получение практических навыков работы в консоли с расширенными
атрибутами файлов [1].

# Выполнение лабораторной работы
1. От имени пользователя guest определите расширенные атрибуты файла (@fig:1_3)
/home/guest/dir1/file1 командой
lsattr /home/guest/dir1/file1

2. Установите командой
chmod 600 file1
на файл file1 права, разрешающие чтение и запись для владельца файла (@fig:1_3).

3. Попробуйте установить на файл /home/guest/dir1/file1 расширенный атрибут a от имени пользователя guest:
chattr +a /home/guest/dir1/file1
В ответ вы должны получить отказ от выполнения операции (@fig:1_3).

![Пункты 1-3](images/1_3.jpg){#fig:1_3 width=100%}

4. Зайдите на третью консоль с правами администратора либо повысьте
свои права с помощью команды su. Попробуйте установить расширенный атрибут a на файл /home/guest/dir1/file1 от имени суперпользователя (@fig:4):
chattr +a /home/guest/dir1/file1

![Пункт 4](images/4.jpg){#fig:4 width=100%}

5. От пользователя guest проверьте правильность установления атрибута (@fig:5_6):
lsattr /home/guest/dir1/file1

6. Выполните дозапись в файл file1 слова «test» командой
echo "test" /home/guest/dir1/file1
После этого выполните чтение файла file1 командой
cat /home/guest/dir1/file1
Убедитесь, что слово test было успешно записано в file1 (@fig:5_6).

![Пункты 5-6](images/5_6.jpg){#fig:5_6 width=100%}

7. Попробуйте удалить файл file1 либо стереть имеющуюся в нём информацию командой
echo "abcd" > /home/guest/dirl/file1
Попробуйте переименовать файл (@fig:7_8).

8. Попробуйте с помощью команды chmod 000 file1
установить на файл file1 права, например, запрещающие чтение и запись для владельца файла (@fig:7_8). Удалось ли вам успешно выполнить указанные команды? -- Не удалось.

![Пункты 7-8](images/7_8.jpg){#fig:7_8 width=100%}

9. Снимите расширенный атрибут a с файла /home/guest/dirl/file1 от
имени суперпользователя (@fig:9) командой
chattr -a /home/guest/dir1/file1

![Пункт 9](images/9.jpg){#fig:9 width=100%}

Повторите операции, которые вам ранее не удавалось выполнить. Ваши
наблюдения занесите в отчёт (@fig:9_1).

![Пункт 9. Повтор операций](images/9_1.jpg){#fig:9_1 width=100%}

10. Повторите ваши действия по шагам, заменив атрибут «a» атрибутом «i».
Удалось ли вам дозаписать информацию в файл? -- Не удалось. Ваши наблюдения занесите в отчёт (@fig:10_1 - @fig:10_3).

![Пункт 10. Повтор операций (1)](images/10_1.jpg){#fig:10_1 width=100%}

![Пункт 10. Добавление атрибута i](images/10_2.jpg){#fig:10_2 width=100%}

![Пункт 10. Повтор операций (2)](images/10_3.jpg){#fig:10_3 width=100%}

# Выводы
Получены практические навыки работы в консоли с расширенными атрибутами файлов.

# Список литературы
1. Методические материалы курса
