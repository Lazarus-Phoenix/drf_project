# Для модели курса добавьте в сериализатор поле вывода количества уроков. Поле реализуйте с помощью 
## SerializerMethodField()
___

 Добавил новую модель в приложение users: <br>

Платежи <br>

пользователь, <br>
дата оплаты, <br>
оплаченный курс или урок, <br>
сумма оплаты, <br>
способ оплаты: наличные или перевод на счет. <br>
Поля  <br>
пользователь 
,  <br>
оплаченный курс <br>
 и  <br>
отдельно оплаченный урок <br>
___
# Реализована вложенность в сериализаторе курсов
# Настроил фильтрацию для эндпоинта вывода списка платежей с возможностями:

1. # менять порядок сортировки по дате оплаты,
![ordering=payment_date.png](static/media/ordering%3Dpayment_date.png)
![ordering=-payment_date.png](static/media/ordering%3D-payment_date.png)
2. # фильтровать по курсу или уроку,

![payments.png](static/media/payments.png)
![payd_course=11.png](static/media/payd_course%3D11.png)
![payd_lesson=7.png](static/media/payd_lesson%3D7.png)
3. # фильтровать по способу оплаты.

![sorting_payment_method=cash.png](static/media/sorting_payment_method%3Dcash.png)
![sorting_payment_method=transfer.png](static/media/sorting_payment_method%3Dtransfer.png)
---

# отсечка описания прошлого дз 
___

# GET запрос в courses
![Снимок экрана от 2025-03-15 01-04-35.png](static/media/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-03-15%2001-04-35.png)
# POST отправка в courses
![Снимок экрана от 2025-03-15 02-07-23.png](static/media/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-03-15%2002-07-23.png)
# GET проверка доставленного POST отправлением
![Снимок экрана от 2025-03-15 02-12-05.png](static/media/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-03-15%2002-12-05.png)
# PUT оправка внесение изменений
![Снимок экрана от 2025-03-15 03-03-28.png](static/media/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-03-15%2003-03-28.png)
# GET проверка доставленных PUT изменений
![Снимок экрана от 2025-03-15 03-08-18.png](static/media/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-03-15%2003-08-18.png)
# GET контрольный в голову проверка доставленных PUT изменений
![Снимок экрана от 2025-03-15 03-10-08.png](static/media/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-03-15%2003-10-08.png)
# Уходим след в след , заметая следы .
![Снимок экрана от 2025-03-15 03-10-18.png](static/media/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-03-15%2003-10-18.png)
# Уходим удаляя пошагово в обратном порядке созданное дерево, сначала ветви потом ствол
![Снимок экрана от 2025-03-15 03-11-22.png](static/media/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-03-15%2003-11-22.png)

![Снимок экрана от 2025-03-15 03-11-55.png](static/media/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-03-15%2003-11-55.png)

![Снимок экрана от 2025-03-15 03-12-01.png](static/media/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-03-15%2003-12-01.png)
# CRUD полностью продемонстрирован, проект совершив полный Demo CRUD вернулся в исходное состояние
![Снимок экрана от 2025-03-15 03-12-25.png](static/media/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-03-15%2003-12-25.png)
