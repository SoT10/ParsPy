#pip install beautifulsoup4, lxml(парсер)

from bs4 import BeautifulSoup

soup = BeautifulSoup(src, "lxml") #где src - это дом архитектура сайта

#title = soup.title
#print(title) - выводит значение тега title кода src <title>"значение"</title>
#print(title.text) - выводит значение тега title без самого тега "значение"
#print(title.string) - аналогично


#.find() и .find_all()
#teg_h1 = soup.find("h1") - поиск по тегам, find находит первый попавшийся
#teg_h2 = soup.find_all("h2") - поиск по тегам, выводит все значения тега, которые есть на сайте
#user_name = soup.find("div", class_="user_name") - поиск имени пользователя, вывод = <div class=user_name>
                                                                                         #<span>Anderson</span>
                                                                                         # </div>                                
#print(user_name.text.strip) - вывод имени пользователя без лишних символов вывод = Anderson

#user_name1 = soup.find("div", class_="user_name").find("span").text
#print(user_name1) - вывод имени пользователя аналогично user_name
#find_all_info = soup.find("class_ = "user_name").find_all("span")

# for i in find_all_info:
#     find_all_info1 = append(i.text)
#     print(find_all_info1)

#для того чтобы забрать значение какого либо аттрибута используем метод get
#url = item.get("href") - например, значение href="http://music.ru", вывод = http://music.ru

#.find_parent и .find_parents
# на примере:
# <div class="her">
#     <div class="leftegg">
#         <div>НАйс</div>
#         <h1>Bich, i am so big</h1>
#         <div class="rightegg">
#             fucking left egg is so big 
#         </div>
#     </div>
# </div>
# right_egg = soup.find(class_="rightegg").find_parent()
# вывод = <div>НАйс</div>                        то есть он начинает смотреть указанный див снизу,
#         <h1>Bich, i am so big</h1>             в методе parent он доходит до первого родительского тега
#         <div class="rightegg">                 в методе parents он доходит до html тега
#             fucking left egg is so big         если ставим ограничение на поиск .find_parent("div", "leftegg")
#         </div>                                 то дойдет до значения <div class="leftegg">


# .next_element и .previous_element

# work_next_el = soup.find(class_ = "user_info").next_element - вывод = "пустая строка"
# work_next_el = soup.find(class_ = "user_info").next_element.next_element  - вывод = <h1(или иной тег)>'значение'</h1>

# для того чтобы не писать два раза .next_element можно использовать .find_next
# work_next_el = soup.find(class_ = "user_info").next_element.next_element == work_next_el = soup.find(class_ = "user_info").find_next

# .previous_element - противоположность next_element
# soup.find_previous

# .find_next_sibling и .find_previous_sibling

# на примере:
# # <div class="her">
# #     <div class="leftegg">
# #         <div>НАйс</div>
# #         <h1>Bich, i am so big</h1>
# #         <div class="rightegg">
# #             fucking left egg is so big 
# #         </div>
# #          <div class="stop">
# #             fucking left egg is so big 
# #         </div>
# #     </div>
# # </div>
# next_sibling = soup.find(class_ = "rightegg").find_next_sibling() - вывод = <div class="stop">
#                                                                                 fucking left egg is so big 
#                                                                             </div>
# то есть метод дает значение следующего тега, .find_previous_sibling по аналогии

# find_all_word = soup.find_all("a", text = re.compile("Слово которое ищем")) - вывод = все теги, в которых есть значение слова 