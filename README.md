# wp-ad-bidder
wildberries биддер по управлению рекламными кампаниями "Поиск+Каталог" исключительно в поисковой выдаче, без каталога.


в общем поступила задача создать систему управления АД ВБ.


мини ТЗ ниже
*****************
Здравствуйте. Есть потребность создать биддер по управлению рекламными кампаниями "Поиск+Каталог" исключительно в поисковой выдаче, без каталога. Кто-то сможет помочь в этом вопросе? 
ТЗ:
Необходимо, чтобы биддер привязывался к определённым артикулам конкурентов (до 10), максимально быстро мониторил выдачу по конкретному ключевому запросу и всегда перебивал максимальную ставку выбранных конкурентов на 1 рубль. Это всё должно происходить в рамках заданных максимальной и минамальной ставок, т.е., если конкурент установит ставку выше моей максимальной ставки, то мой биддер должен выбрать заранее установленную ставку на такой случай. Если конкуренты отключат рекламу, то биддер должен установить минимальную указанную ставку.

*****************


накидал пока куски кода, заказчик слился при запросе цены в 300 рублей
**************

кому интересно развите пишите
https://t.me/ddnitecry
*********************
идеология
1  реклама выключена позиция 23
2 включаем рекламу  на позицию 4

состояние
1 органик
2 органик
3 органик
4 органик
5 органик
6 органик
7 органик
8 реклама за 2901 руб

из всего я узнаю позицию 4
могу узнать позицию 8 и установить 2902

вероятно тогда я стану на 1 позиции 


из нюансов -- заказанная 4 позиция не будет соответствовать 1 текущей


*************************
внедренный механизм
находим 4 позицию, далее находим 4 5 6 7 8 ставку за 2901 руб  (!  возможен пропуск товаров по АЙДИ пропускаемых) и ее устанавливаем свою 2902

проверка что ставка == 2901+1  и место меньше или равно 4

*****************************************
пример 

F:\CRYPTO_COINS\random\wp-ad-bidder\web-test1>python test.py <br>
2024-06-19 09:52:35,506 - WB AD Bibber - INFO - Запустили<br>
2024-06-19 09:52:35,703 - WB AD Bibber - INFO - Товар 153361292 не в выдаче или реклама не включена<br>
2024-06-19 09:53:35,715 - WB AD Bibber - INFO - Запустили<br>
2024-06-19 09:53:35,851 - WB AD Bibber - INFO - Товар 153361292 не в выдаче или реклама не включена<br>
2024-06-19 09:54:35,876 - WB AD Bibber - INFO - Запустили<br>
2024-06-19 09:54:36,070 - WB AD Bibber - INFO - Товар 153361292 выдаче на позиции 38 но реклама не включена<br>
2024-06-19 09:55:36,135 - WB AD Bibber - INFO - Запустили<br>
2024-06-19 09:55:36,253 - WB AD Bibber - INFO - Товар 153361292 не в выдаче или реклама не включена<br>
2024-06-19 09:56:36,271 - WB AD Bibber - INFO - Запустили<br>
2024-06-19 09:56:36,461 - WB AD Bibber - INFO - Товар 153361292 не в выдаче или реклама не включена<br>
2024-06-19 09:57:36,478 - WB AD Bibber - INFO - Запустили<br>
2024-06-19 09:57:42,195 - WB AD Bibber - INFO - Товар 153361292 выдаче на позиции 43 но реклама не включена<br>


*************************
осталось толко запилить установку ставки.







**************************

благодарности
https://www.wildberries.ru/brands/paradise-dream  

paradise-dream   Матрас 160х200   
за техническую и инфо поддержку
