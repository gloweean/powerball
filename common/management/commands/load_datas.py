from django.core.management.base import BaseCommand
from common.models import Base, Population
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from django.conf import settings
import time


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

        # input 넣고
        input_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        input_box.send_keys('1')
        
        # find button click
        find_button = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='button-find']")
        find_button.click()
        
        time.sleep(3)

        result = driver.find_element(By.CSS_SELECTOR, "section[class='row collapse results-search']")
        
        text = result.text
        
        
        result_set = text.split('\n')
        
        print(result_set)

        
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
        

