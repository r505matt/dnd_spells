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
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}



class Command(BaseCommand):
    help = 'Scrapes D&D Beyond for spells'
    
    def handle(self, *args, **kwargs):
        
        spell_list = ['aura-of-vitality']
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
        
    
        print("\n\nStart\n\n")
        for spell_name in spell_list:
            URL = f"https://www.dndbeyond.com/spells/{spell_name}"
            page = requests.get(URL, headers=headers)

            soup = BeautifulSoup(page.content, "html.parser")
            #main stats of the spell, concentration is appended to duration, ritual is appended to casting time, shape is part of range
            #order of main data: level, cast time (ritual), range/area (shape), components, duration (concentration), school, attack/save, damage/effect
            name = soup.find_all('h1', class_="page-title")
            main_data = soup.find_all('div', class_="ddb-statblock-item")
            desc = soup.find_all('div', class_="more-info-content")
            tags = soup.find_all('p', class_="tags spell-tags")
            class_tags = soup.find_all('p', class_="tags available-for")


            
            print("\n\nNext\n")
            print("-----------------------")
            print(soup.prettify())
            #for data in name:
            #    value = data.contents[0]
            #    print(repr(value.stripped_strings))
            print("-----------------------")

            
            #label has name of model to relate to, value has the value. conc/rit/area and area shape are part of value
            #for rit/area, data after other value. concentration comes before duration though
            #repr turns the soup.stripped_strings object into a string
            for data in main_data:
                label, value = data.contents[1], data.contents[3]
                for child in label.stripped_strings:
                    print(repr(child))
                for child in value.stripped_strings:
                    print(repr(child))
                print(value)
                    
                print("-----------------------")

        
            seconds = random.uniform(3.5, 6.5)
            time.sleep(seconds)
            