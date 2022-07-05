import requests
import time
import random
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}



class Command(BaseCommand):
    help = 'Scrapes D&D Beyond for spells'
    
    def handle(self, *args, **kwargs):
        spell_list = []
        """
        for page in range(1,2):
            
            URL = f"https://www.dndbeyond.com/spells?page={page}"
            page = requests.get(URL, headers=headers)

            soup = BeautifulSoup(page.content, "html.parser")
            spell_list.extend([i['data-slug'] for i in soup.find_all('div', class_="info", data_slug_="")])
            print(spell_list)
            
            seconds = random.uniform(3.5, 6.5)
            time.sleep(seconds)
        """
        for spell_name in spell_list:
            URL = f"https://www.dndbeyond.com/spells/{spell_name}"
            page = requests.get(URL, headers=headers)

            soup = BeautifulSoup(page.content, "html.parser")
            #main stats of the spell, concentration is appended to duration, ritual is appended to casting time, shape is part of range
            #order of main data: level, cast time (ritual), range/area (shape), components, duration (concentration), school, attack/save, damage/effect
            main_data = soup.find_all('div', class_="ddb-statblock-item")
            desc = soup.find_all('div', class_="more-info-content")
            tags = soup.find_all('p', class_="tags spell-tags")
            class_tags = soup.find_all('p', class_="tags available-for")

            print("-----------------------")
            for data in main_data:
                print(data)
                print("-----------------------")

            #seconds = random.uniform(3.5, 6.5)
            #time.sleep(seconds)
            break