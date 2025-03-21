### Для модели курса добавлено в сериализатор поле вывода количества уроков. 

Поле реализовал с помощью 
## SerializerMethodField()
___

 Добавил новую модель в приложение users:  Платежи <br>

пользователь, <br>
дата оплаты, <br>
оплаченный курс или урок, <br>
сумма оплаты, <br>
способ оплаты: наличные или перевод на счет. <br>
Поля  <br>
пользователь  <br>
оплаченный курс и  <br>
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
