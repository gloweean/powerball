import time
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.models import Base


class Command(BaseCommand):
    def handle(self, *args, **options):
        driver = webdriver.Chrome(settings.WEBDRIVER_PATH)
        driver.implicitly_wait(2)
        
        # URL 접근
        driver.get('https://thelott.com/powerball/results')
        driver.implicitly_wait(3)
        
        inqiury_button = driver.find_elements(By.CSS_SELECTOR, "span[data-test-id='draw no.-tab']")
        
        # draw no click
        draw_no_button = inqiury_button[0]
        draw_no_button.click()
        driver.implicitly_wait(2)
        
        '''
        이 부분이 반복되어야 하는 부분
        '''
        # 가장 최근의 draw number 찾기
        searching_element_draw_number = driver.find_element(By.CSS_SELECTOR, "div[class='drawname']")
        most_recent_draw = int(searching_element_draw_number.text.split('No. ')[1])
        
        # 반복하기
        for draw in range(1, most_recent_draw + 1):
            # database에 있을 경우 pass
            if Base.objects.filter(draw=draw).exists():
                print("draw {} is already exist > pass".format(draw))
                pass
            else:
                # input field search & input
                input_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
                length = len(input_box.get_attribute('value'))
                input_box.send_keys(length * Keys.BACKSPACE)
                input_box.send_keys('{}'.format(draw))
                
                # find button click
                find_button = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='button-find']")
                find_button.click()
                
                time.sleep(1.5)
                
                result = driver.find_element(By.CSS_SELECTOR, "section[class='row collapse results-search']")
                
                text = result.text
                
                result_set = text.split('\n')
                
                number_set = [content for i, content in enumerate(result_set) if
                              i >= result_set.index('Draw {}'.format(draw))][:-2]
                print(number_set)
                
                # database 연동
                powerball = int(number_set.pop())
                
                number_set.pop(0)
                draw_date_str = number_set.pop(0)
                draw_date = datetime.strptime(draw_date_str, "%a, %d %b %Y").date()
                
                number_set = [int(num) for num in number_set]
                number_set.sort()
                
                num1 = number_set.pop(0)
                num2 = number_set.pop(0)
                num3 = number_set.pop(0)
                num4 = number_set.pop(0)
                num5 = number_set.pop(0)
                
                try:
                    num6 = number_set.pop(0)
                except:
                    num6 = None
                
                # base 입력
                Base.objects.get_or_create(
                    draw=draw,
                    draw_date=draw_date,
                    num1=num1,
                    num2=num2,
                    num3=num3,
                    num4=num4,
                    num5=num5,
                    num6=num6,
                    powerball=powerball,
                )
                
                print([draw, draw_date, num1, num2, num3, num4, num5, num6, powerball])
        
        '''
        여기까지가 원하는 HTML 만드는 부분
        '''
        
        # html_source = driver.page_source
        # soup = BeautifulSoup(html_source, "html.parser")
        #
        # search_section = soup.find('section', {'class': ['row', 'collapse', 'results-search']})
        # number_container = search_section.find('div', {'class': ['au-target', 'row', 'align-middle', 'collapse', 'draw-details-top-bottom']})
        #
        # numbers = number_container.find_all('span')
        #
        # print(numbers)
        # for i in numbers:
        #     print(i.content)
