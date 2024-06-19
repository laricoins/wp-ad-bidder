тестирование поискового запроса


из неофф АПИ запрос предоставлен
https://www.youtube.com/channel/UCfgVtGopuwW6y_5kyf32-fQ

***********************
https://search.wb.ru/exactmatch/ru/common/v5/search?ab_testid=promok&appType=1&curr=rub&dest=-445297&page=[[PAGE]]&query=[[KEYWORD]]&resultset=catalog



*************************************


для теста используем
https://search.wb.ru/exactmatch/ru/common/v5/search?ab_testid=promok&appType=1&curr=rub&dest=-445297&page=1&query=матрас%20160х200&resultset=catalog


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



"""
if pos['position']:
   logger.info(f"Позиция товара {id} пр запросу '{SearchPhrase}' ==> {pos['position']} cpm ={position['cpm']}")
   positionIsSetPosition = position['products'][SetPosition]
   print(positionIsSetPosition)
   log = positionIsSetPosition.get('log',False)
 #  cpm = positionIsSetPosition.get('log').get('cpm',False)
   logger.info(f"На  заказанной позиции {SetPosition} ставка {log}")

#print(position)
products = position['products']
#print(products)

print(f"Поисковая фраза: {SearchPhrase}")
print(f"Номер рекламной компании: {advertId}")
print(f"Номер продвигаемой карточки: {id}")
print(f"установить на место: {SetPosition}")
print(f"Максимальное значение ставки за 1000 показов: {MaxCpm}")
print(f"Минимальное значение ставки за 1000 показов: {MinCpm}")
print(f"Шаг изменения ставки: {StepCpm}")

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

"""


# 3 выдача общая есть  проверь заказанную позицию  SetPositionFind ==4 и SetPositionFind + 1 = 5	
#возможно через АПИ запросить цену ??? если они разные то мягко завершаем
#если текущая позиция не свовпадает с ожидаемой

# если текущая позиция меньше чем SetPosition установи ставку из CartCurr



#    if ThisCard['position'] < CartCurr['position']:
#       SetCmp = int(CartCurr['cpm'])+1
#       logger.info(f"Устанавливаем цену для позииции {SearchPhrase} ==> {SetCmp}")
	   

#print(ApiToken)
#response = get_promotion_adverts(ApiToken,  advertId, logger)
#print(response)






#1 проверили что АПИ ключ хороший  если плохо то умри  doo2()
# 2 сделали запрос на поисковую фразу если есть выдача то 3    если плохо то умри
# 3 выдача общая есть  проверь заказанную позицию  SetPositionFind ==4 и SetPositionFind + 1 = 5 если есть выдача cpm то 4 если плохо то умри
# 4 узнали ай ди и cpm SetPositionFind  если   SetPositionFind  ==  SetPosition  узнали цену SetPositionFind + 1 если цена SetPositionFind + 1 == (1+ SetPositionFind.цена) то все хорошо иначе изменяем цену == на (SetPositionFind + 1).цена
#pos = find_position_of_product(SearchPhrase,id)
#print(DonCompeteWith)	



 