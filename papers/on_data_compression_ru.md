# О методах сжатия данных
В этой короткой статье читателю представляется новый метод сжатия данных.

## Воспринимаемое количество информации
Пусть `I(S\X)` - количество информации в `X`, воспринимаемое субъектом `S`.
Субъектом может выступать абсолютно что угодно. 
Одними из самых распространенных примеров являются люди и носители информации.
Для определенности будем обозначать их `U` и `M`.

Количество информации, воспринимаемое человеком, невозможно корректно описать численно.
Однако, для двух информационных объектов `X, Y` и пользователем `U` можно говорить об отношении между `I(U\X)` и `I(U\Y)`: если `U` говорит: "`X` содержит больше информации, чем `Y`", то имеет место `I(U\X) > I(U\Y)`.

При этом имеется ввиду возможность восприятия вообще всей содержащейся внутри `X` информации.
Например, если речь идет о JPEG-фотографии, то `I(U\X)` включает в себя как само количество информации в изображении, так и его количество во всей мета-информации.

С другой стороны, количество информации на на носителях легко описывается численно количеством бит.
Более того, в силу ограниченности их емкости, встает задача его уменьшения, решаемая с помощью методов сжатия данных.

## Методы сжатия данных
Сжатием данных `X` называется ее кодирование в форме, содержащей меньшее число бит.
При этом обычно рассматривается два типа сжатия: с потерями и без.

Пусть `Y` является результатом некоторого кодирования `X`.
Тогда можно описать методы сжатия данных с использованием воспринимаемого количества информации.

### Сжатие без потерь 
Является случаем эффективного перекодирования информации без изменения воспринимаемого пользоватлем содержимого: `I(U\X) = I(U\Y)`, `I(M\X) > I(M\Y)`.

### Сжатие с потерями
Использует особенности восприятия человеком информации для ее более эффективного кодирования: `I(U\X) > I(U\Y)`, `I(M\X) > I(M\Y)`.

### Сжатие с использованием методов стеганографии
Стоит заметить, что упомянутые два вида не описывают все возможные взаимоотношения между `I(U\X), I(U\Y)` и `I(M\X), I(M\Y)`.
Из оставшихся взаимоотношений лишь одно имеет смысл с точки зрения сжатия данных: `I(U\X) < I(U\Y)`, `I(M\X) ~ I(M\Y)`. В последнем выражении `~` означает, что воспринимаемое `M` количество информации изменилось несущественно, неважно, в какую сторону.

Оно описывает встраивание дополнительной информации в `X` таким образом, что пользователь имеет к ней доступ, но носитель информации не имеет представления о ее существовании.
Иначе говоря, частный случай использования методов стеганографии, при котором размер контейнера `X` на носителе информации увеличивается не так сильно, как количество информации в нем, а секретность встроенной информации не играет роли.