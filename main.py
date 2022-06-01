import requests
from pprint import pprint

class Superhero():
    def __init__(self,name):
        self.name = name
    def get_dict(self):
        url = 'https://superheroapi.com/api/2619421814940190/'
        url_method = '/search/' + self.name
        response = requests.get(url + url_method)
        return response.json()
    def id_hero(self):
        find_id_from_dict = self.get_dict().get('results')
        for x in find_id_from_dict:
            id = x['id']
            break
        return id
    def true_hero(self): # т.к. сайт выдает список из несколько супергероев с одинаковыми именами, примем за канон того героя, который имеет более ранний id
        url = 'https://superheroapi.com/api/2619421814940190/' + self.id_hero()
        response = requests.get(url)
        return response.json()
    # def intelligence(self):
    #     smart = self.true_hero()['powerstats']['intelligence']
    #     self.intelligence = smart
    #     return smart

    # def find_smartest_hero(self,hero_1, hero_2, hero_3):
    #     dict_hero = {}
    #     dict_hero[hero_1.name] = int(hero_1.intelligence)
    #     dict_hero[hero_2.name] = int(hero_2.intelligence)
    #     dict_hero[hero_3.name] = int(hero_3.intelligence)
    #     for name, smart in dict_hero.items():
    #         if all(x <= smart for x in dict_hero.values()):
    #             answer = (f'The superhero with the greatest intelligence ({dict_hero[name]}) is {name}')
    #     return answer
    def intelligence_2(self, heroes):
        for hero in heroes:
            smart = hero.true_hero()['powerstats']['intelligence']
            hero.intelligence = smart
        return smart
    def find_smartest_hero_2(self, heroes):
        dict_hero = {}
        for hero in heroes:
            dict_hero[hero.name] = int(hero.intelligence)
        for name, smart in dict_hero.items():
            if all(x <= smart for x in dict_hero.values()):
                answer = (f'The superhero with the greatest intelligence ({dict_hero[name]}) is {name}')
        return answer


hulk = Superhero('Hulk')
captain_america = Superhero('Captain America')
thanos = Superhero('Thanos')

# hulk.intelligence()
# captain_america.intelligence()
# thanos.intelligence()
# print(hulk.find_smartest_hero(hulk,captain_america,thanos))

hulk.intelligence_2([hulk,captain_america,thanos]) # передаем список супер героев для присваивания им характеристики intelligence
# print(thanos.intelligence)
print(captain_america.find_smartest_hero_2([hulk,captain_america,thanos]))