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
        datas = Base.objects.all().values_list('num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'powerball', 'id')
        for data in datas:
            play = list(data)
            inning = play.pop()
            powerball = play.pop()
            if powerball in play:
                print('catchup in {} game'.format(inning))