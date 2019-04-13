import operator
import json


class Manage_budget_data:
    def __init__(self):
        pass


    def sort_mileage(self, budget_dict):
        list_of_dicts=budget_dict['listings']
        list_of_dicts.sort(key=operator.itemgetter('miles'))
        five_car_list=[]

        for i in range(5):
            try:
                #print(list_of_dicts[i]['build']['make'], list_of_dicts[i]['build']['model'], list_of_dicts[i]['price'], list_of_dicts[i]['miles'])
                five_car_dict={'make':list_of_dicts[i]['build']['make'],
                    'model': list_of_dicts[i]['build']['model'],
                    'price': list_of_dicts[i]['price'],
                    'mileage': list_of_dicts[i]['miles'],
                    'photo': list_of_dicts[i]['media']['photo_links'][0]
                  }
                five_car_list.append(five_car_dict)
            except:
                continue

        five_car_data= json.dumps(five_car_list)

        return five_car_data