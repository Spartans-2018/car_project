from wrapper import Inventory_req
import requests
import time

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
    def budget_search(budget, car_type, milieage, zip_code, color):
        url= IR.lookup_budjet()
        response= requests.get(url.format(zip_code, car_type, color, milieage, budget))
        budget_dict= response.json()

        return budget_dict


    @staticmethod
    def budget_search_anymileage(budget, car_type,zip_code, color):
        url= IR.lookup_budget_anymileage()
        response= requests.get(url.format(zip_code, car_type, color, budget))
        budget_dict= response.json()

        return budget_dict

    @staticmethod
    def new_car_search(make, model, zip_code):
        url = IR.lookup_new_car()
        response= requests.get(url.format(zip_code, make, model))
        new_car_dict= response.json()

        return new_car_dict


    @staticmethod
    def new_car_search_years(make, model, zip_code, year):
        url= IR.lookup_new_car_years()
        # response= requests.get(url.format(zip_code, year, make, model))

        response= Query.get(url.format(zip_code, year, make, model))
        new_car_years_dict= response.json()

        return new_car_years_dict

    @staticmethod
    def nintees_car_search(years, make, model):
        url=IR.look_up_ninetees()
        # response=requests.get(url.format(years, make, model))

        response= Query.get(url.format(years, make, model))
        ninetees_car_dict=response.json()

        return ninetees_car_dict

    @staticmethod
    def get(url):
        try:
            return requests.get(url)
        except Exception:
            # sleep for a bit in case that helps
            time.sleep(2)
            # try again
            return Query.get(url)


# res=Query.new_car_search_years('honda', 'civic', '07030', '1990,1989,1988')
# print(res['stats'])