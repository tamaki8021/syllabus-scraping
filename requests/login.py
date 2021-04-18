from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.support.select import Select
import chromedriver_binary
import func


driver = webdriver.Chrome()

# driver.get("https://t-portal.main.teikyo-u.ac.jp/start/auth/login")
#
# username = driver.find_element_by_css_selector('#loginId')
# print(username)
# password = driver.find_element_by_css_selector('#passwordId')
# username.send_keys("学籍番号")
# password.send_keys("パスワード")
# password.send_keys(keys.ENTER)

driver.get("https://www.e-campus.gr.jp/syllabus/kanri/hachioji/public/syllabus/2021")

# 学科
select_discipline = "経済学科"

# 1, 2, 3, 4の中から選ぶ
select_others = "3"

# 1 or 2
select_semester_num = "1"

# 必修・選択
select_choice_type = "選択"

el_discipline = driver.find_element_by_id("discipline-select")
el_others_gtade = driver.find_element_by_id("q_others_grade_id")
el_semester = driver.find_element_by_id("q_semester_id_eq")
el_choice_type = driver.find_element_by_id("q_choice_type_id_eq")

Select(el_discipline).select_by_visible_text(select_discipline)
Select(el_others_gtade).select_by_value(select_others)
Select(el_semester).select_by_value(select_semester_num)
Select(el_choice_type).select_by_visible_text(select_choice_type)

# enter key
el_choice_type.send_keys(keys.ENTER)

cur_url = driver.current_url
print(cur_url)

nextUrl, nextSoup = func.setup(cur_url)
curriculums = nextSoup.select("body > div.container > div.row > div.span12 > div.section > div.section-content > div.span6 > div > a")

for curriculum in curriculums:
    print(curriculum.getText())
