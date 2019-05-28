import operator
import json
from queryMarketCheck import Query
from flask import Flask, jsonify, request, render_template
import json
import time
from numpy import median
from datetime import datetime

class Manage_budget_data:
    def __init__(self):
        pass

    def budget_search_manager(self, budget, car_type, milieage, zip_code, color):
        budget_range_tup=(int(budget)-500, int(budget)+500)
        budget_range_str= str(budget_range_tup[0]) +'-'+str(budget_range_tup[1])
        milieage_range_str='0-'+ milieage
        if milieage !='any':
            budget_dict=Query.budget_search(budget_range_str, car_type, milieage_range_str, zip_code, color)
        else:
            budget_dict=Query.budget_search_anymileage(budget_range_str, car_type, zip_code, color)


        sorted_dict=Manage_budget_data().sort_mileage(budget_dict)

        return sorted_dict



    def sort_mileage(self, budget_dict):
        list_of_dicts=budget_dict['listings']
        list_of_dicts.sort(key=operator.itemgetter('miles'))

        luxury_list=['BMW', "Lexus", 'Audi', 'Mercedes', 'infiniti']
        domestic_list=['Chevrolet', 'Dodge', 'Ram', 'Ford', 'Chrysler']
        foreign_list=['Honda', 'Toyota', 'Mazda', 'Acura']
        # # five_car_list=[]

        # for i in range(5):
        #     try:
        #         #print(list_of_dicts[i]['build']['make'], list_of_dicts[i]['build']['model'], list_of_dicts[i]['price'], list_of_dicts[i]['miles'])
        #         five_car_dict={'make':list_of_dicts[i]['build']['make'],
        #                         'model': list_of_dicts[i]['build']['model'],
        #                         'price': list_of_dicts[i]['price'],
        #                         'miles': list_of_dicts[i]['miles'],
        #                         'photo': list_of_dicts[i]['media']['photo_links'][0]
        #           }
        #         five_car_list.append(five_car_dict)
        #     except:
        #         continue

        # five_car_data= json.dumps(five_car_list)
        rec_list=[]
        aux_list=[]
        for make in luxury_list:
            for i in range(len(list_of_dicts)):
                if len(aux_list)<2:
                    if make==list_of_dicts[i]['build']['make'] and make not in aux_list:
                        rec_list.append(list_of_dicts[i])
                        aux_list.append(make)
                else: break
                    
        aux_list=[]
        for make1 in domestic_list:
            for j in range(len(list_of_dicts)):
                if len(aux_list)<2:
                    if make1==list_of_dicts[j]['build']['make'] and make1 not in aux_list:
                        rec_list.append(list_of_dicts[j])
                        aux_list.append(make1)
                else: break

        aux_list=[]
        for make2 in foreign_list:
            for k in range(len(list_of_dicts)):
                if len(aux_list)<2:
                    car= list_of_dicts[k]['build']['make']
                    if make2==car and make2 not in aux_list:
                        rec_list.append(list_of_dicts[k])
                        aux_list.append(make2)
                else: break


        return rec_list

    
class Manage_new_car_search:
    def __init__(self):
        pass

    def new_car_years(self, make, model, zip_code):
        median_price_list=[]
        new_car_dict= Query.new_car_search(make, model, zip_code)
        median_price_list.append( Manage_new_car_search().roundup ( int (new_car_dict['stats']['price']['median'])))
        
        # years_list=['2018', '2016', '2014', '2012', '2009', '2001,2000,1999']
                #    '1980,1981,1982']

        years_list=Manage_new_car_search().years_data()
        for year in years_list:
            new_car_years_dict=Query.new_car_search_years(make, model, zip_code, year)

            try:
                median_price= int (new_car_years_dict['stats']['price']['median'])
                median_price_roundup= Manage_new_car_search().roundup(median_price)
            except: median_price_roundup= None


            
            median_price_list.append(median_price_roundup)

        curent_year=datetime.now().year
        years_list.insert(0, str(curent_year))
        years_list[-1]= str(curent_year-20)
        years_list.append(str(curent_year-30))
        
        ninetees_data=Manage_new_car_search().ninetees_data(make, model)

        
        median_price_list.append(ninetees_data[0])
        photo_ninetees=ninetees_data[1]
        
        
        photo=''
        for i in range (len(new_car_dict['listings'])):
            try:
                photo= new_car_dict['listings'][i]['media']['photo_links'][0]
                pass
            except:
                continue

        graph_dict= {'y1': median_price_list, 
                    'x1':years_list, 
                    'make_model': make+ ', '+ model,
                    'photo': photo,
                    # 'photo': new_car_dict['listings'][1]['media']['photo_links'][0],
                    'photo_nine': photo_ninetees}


        new_car_graph_data=json.dumps(graph_dict)



        """test graprh dict"""

        # graph_dict= {'y1': [27100, 24500, 17300, 13700, 10000, 7700, 4500, 3000], 
        #             'x1':['2019', '2018', '2016', '2014', '2012', '2009', '2000', '1990'], 
        #             'make_model': 'Honda, Accord',
        #             'photo': 'https://content.homenetiol.com/1280x960/92d50ad157264b64b6fd1ea0939b8d3e.jpg'}

        # new_car_graph_data=json.dumps(graph_dict)
        '''test graph'''

        return new_car_graph_data



    def ninetees_data(self, make, model):
        curent_year=datetime.now().year

        years_str=str(curent_year-29)+','+str(curent_year-28)+','+str(curent_year-27)
        ninetees_car_dict= Query.nintees_car_search(years_str, make,model)
        car_price=[]
        photo_ninetees=''
        for i in range (len(ninetees_car_dict['listings'])):
            try:
                list_price=ninetees_car_dict['listings'][i]['price']
                car_price.append(list_price)
            except:
                continue

        try:
            price= int (median(car_price))
            price_roundup= Manage_new_car_search().roundup(price)
        except:
            price= None
            price_roundup= None

        for i in range (len(ninetees_car_dict['listings'])):
            try:
                photo_ninetees=ninetees_car_dict['listings'][i]['media']['photo_links'][1]
                pass
            except:
                photo_ninetees=''

        return (price_roundup, photo_ninetees)


    @staticmethod
    def years_data():
        curent_year=datetime.now().year
        years_list=[]

        for year in range (curent_year-1, curent_year-8, -2):
            years_list.append(year)
        
        years_list.append(curent_year-10)

        years_list_str=[str(year) for year in years_list]
        twenty_years_str=str(curent_year-18)+','+str(curent_year-19)+','+str(curent_year-20)
        years_list_str.append(twenty_years_str)


        return years_list_str


    @staticmethod
    def roundup(x):
        return x if x % 100 == 0 else x + 100 - x % 100


#print (Manage_new_car_search().new_car_years('bmw', '3 series', '07030'))
#print (Manage_new_car_search().ninetees_data('bmw', '3 series') )

# print (Manage_new_car_search().years_data() )


test_dict=Manage_budget_data().budget_search_manager(20000, 'sedan', '70000-80000', '07030', 'black')
print (len(test_dict))