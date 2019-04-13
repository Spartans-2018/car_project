from wrapper import Inventory_req
import requests

IR=Inventory_req()

class Query:

    def __init__(self):
        pass


    @staticmethod
    def search(zip_code, year, make, model, state):
        
        url=IR.lookup_compare()
        response=requests.get(url.format(zip_code, year, make, model, state))
        lookup_dict=response.json()
        return lookup_dict


    @staticmethod
    def search1(zip_code, ymm, state):
        url=IR.lookup_compare()
        response=requests.get(url.format(zip_code, ymm, state))
        lookup_dict=response.json()
        return lookup_dict

    @staticmethod
    def search2(zip_code, year, make, model):
        url = IR.lookup_compare()
        response= requests.get(url.format(zip_code, year, make, model))
        lookup_dict= response.json()
        return lookup_dict

    @staticmethod
    def budget_search(budget, car_type, milieage, zip_code):
        url= IR.lookup_budjet()
        response= requests.get(url.format(zip_code, car_type, milieage, budget))
        budget_dict= response.json()

        return budget_dict




#print (Query.search2('07030', '2011', 'honda', 'accord'))