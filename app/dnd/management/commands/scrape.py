import requests
import time
import random
import json
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from dnd.management.helpers import get_random_ua, get_referrer
from dnd.management.spells.spell import Spell

#headers = {
#    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
#}



class Command(BaseCommand):
    help = 'Scrapes D&D Beyond for spells'
    
    def handle(self, *args, **kwargs):
        
        spell_list = ["fireball"]
        """
        for page in range(1,2):
            
            URL = f"https://www.dndbeyond.com/spells?page={page}"
            ua = get_random_ua()
            ref = get_referrer(page)
            headers = {'User-Agent' : ua, 'referer': ref}

            page = requests.get(URL, headers=headers)

            soup = BeautifulSoup(page.content, "html.parser")
            spell_list.extend([i['data-slug'] for i in soup.find_all('div', class_="info", data_slug_="")])
            print(spell_list)
            
            seconds = random.uniform(60, 120)
            time.sleep(seconds)
        """

        #ignore = open("ignore.txt", "a")

        for spell_name in spell_list:
            URL = f"https://www.dndbeyond.com/spells/{spell_name}/more-info"

            ua = get_random_ua()
            ref = get_referrer(spell_name)
            headers = {'User-Agent' : ua, 'referer': ref}

            page = requests.get(URL, headers=headers)

            soup = BeautifulSoup(page.text, "html.parser")

            # name = soup.find_all('h1', class_="page-title") # this should come from the list endpoint
            main_data = soup.find_all('div', class_="ddb-statblock-item")
            desc = soup.find('div', class_="more-info-body-description")
            tags = soup.find('div', class_="more-info-footer-tags")
            class_tags = soup.find('div', class_="more-info-footer-classes")

            spell_level = None
            spell_concentration = False
            spell_ritual = False
            spell_casting_time = None
            spell_range = None
            spell_area = None
            spell_area_shape = None
            spell_components = None
            spell_duration = None
            spell_school = None
            spell_attack_save = None
            spell_damage_effect = None
            spell_description = None
            spell_tags = []
            spell_classes = []

            for data in main_data:
                label = data.find('div', class_='ddb-statblock-item-label').get_text().strip()
                # the `' '.join(mystring.split())` trick removes long whitespaces in range
                value = ' '.join(data.find('div', class_='ddb-statblock-item-value').get_text().strip().split())
                match label:
                    case "Level":
                        spell_level = value
                    case "Casting Time":
                        value = value.split()
                        if value[-1] == "Ritual":
                            spell_ritual = True
                            value = value[:-1]
                        ' '.join(value)
                        spell_casting_time = value
                    case "Range/Area":
                        value = value.replace('(', '').replace(')', '').replace('*', '').split()
                        if len(value) == 1:
                            spell_range = value[0]
                        if len(value) == 2:
                            spell_range = value[0] + ' ' + value[1]
                        if len(value) == 3:
                            spell_range = value[0]
                            spell_area = value[1] + ' ' + value[2]
                        if len(value) == 4:
                            spell_range = value[0] + ' ' + value[1]
                            spell_area = value[2] + ' ' + value[3]
                    case "Components":
                        spell_components = value
                    case "Duration":
                        spell_duration = value
                        value = value.split()
                        if value[0] == "Concentration":
                            spell_concentration = True
                            value = value[1:]
                        ' '.join(value)
                    case "School":
                        spell_school = value
                    case "Attack/Save":
                        spell_attack_save = value
                    case "Damage/Effect":
                        spell_damage_effect = value

            try:
                spell_description = desc.get_text().strip()
            except:
                continue

            tags = tags.find_all('div', class_='tag')
            for tag in tags:
                spell_tags.append(tag.get_text().strip())

            class_tags = class_tags.find_all('div', class_='tag')
            for tag in class_tags:
                spell_classes.append(tag.get_text().strip())

            #TODO some spells actually have hyphen in them, and this converts all of them into spaces regardless
            spell_name = ' '.join(spell_name.title().split('-'))                      
                            
            temp_shape = soup.find(class_ = "aoe-size" )
            start = temp_shape.rfind("i-aoe-") + 6
            spell_area_shape = temp_shape[start:start+4]
            
            current = Spell(spell_name)
            current.level = spell_level
            current.concentration = spell_concentration
            current.ritual = spell_ritual
            current.casting_time = spell_casting_time
            current.range = spell_range
            current.area = spell_area
            current.area_shape = spell_area_shape
            current.components = spell_components
            current.duration = spell_duration
            current.school = spell_school
            current.attack_save = spell_attack_save
            current.damage_effect = spell_damage_effect
            current.description = spell_description
            current.tags = spell_tags
            current.classes = spell_classes
            """
            print(spell_name)
            print(spell_level)
            print(spell_concentration)
            print(spell_ritual)
            print(spell_casting_time)
            print(spell_range)
            print(spell_area)
            print(spell_area_shape)
            print(spell_components)
            print(spell_duration)
            print(spell_school)
            print(spell_attack_save)
            print(spell_damage_effect)
            print(spell_description)
            print(spell_tags)
            print(spell_classes)
            """
            print("\n")
            jsonSpell = json.dumps(current.__dict__)
            print(jsonSpell)

            seconds = random.uniform(60, 120)
            time.sleep(seconds)
    
        #ignore.close()