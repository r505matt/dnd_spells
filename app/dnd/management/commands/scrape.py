import requests
import time
import random
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}



class Command(BaseCommand):
    help = 'Scrapes D&D Beyond for spells'
    
    def handle(self, *args, **kwargs):
        
        spell_list = ['hypnotic-pattern']
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
            URL = f"https://www.dndbeyond.com/spells/{spell_name}/more-info"

            page = requests.get(URL, headers=headers)

            soup = BeautifulSoup(page.text, "html.parser")

            # name = soup.find_all('h1', class_="page-title") # this should come from the list endpoint
            main_data = soup.find_all('div', class_="ddb-statblock-item")
            desc = soup.find('div', class_="more-info-body-description")
            tags = soup.find('div', class_="more-info-footer-tags")
            class_tags = soup.find('div', class_="more-info-footer-classes")

            spell_level = None
            spell_casting_time = None
            spell_range_area = None
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
                        spell_casting_time = value
                    case "Range/Area":
                        spell_range_area = value
                    case "Components":
                        spell_components = value
                    case "Duration":
                        spell_duration = value
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

            print(spell_name)
            print(spell_level)
            print(spell_casting_time)
            print(spell_range_area)
            print(spell_components)
            print(spell_duration)
            print(spell_school)
            print(spell_attack_save)
            print(spell_damage_effect)
            print(spell_description)
            print(spell_tags)
            print(spell_classes)
            print("\n")

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

            #names = soup.select('page-title')
            #for name in names:
            #   print(name.text)


            
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
            """