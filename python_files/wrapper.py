# create wrapper class to access MarketCheck API
import requests

class Inventory_req:

    def __init__(self):
        pass



    @staticmethod   
    def lookup_compare():
        
        url = "https://marketcheck-prod.apigee.net/v1/search?api_key=2yAkthxFVYVxl2go2veb8zmxB8IVKfXl&radius=75&zip={}&year={}&make={}&model={}&state={}"
        url1= 'https://marketcheck-prod.apigee.net/v1/search?api_key=2yAkthxFVYVxl2go2veb8zmxB8IVKfXl&radius=75&zip={}&ymmt={}&state={}'
        url2= 'https://marketcheck-prod.apigee.net/v1/search?api_key=2yAkthxFVYVxl2go2veb8zmxB8IVKfXl&radius=100&zip={}&year={}&make={}&model={}&rows=50&stats=price'
        return url2

    @staticmethod
    def lookup_budjet():
        url= 'https://marketcheck-prod.apigee.net/v1/search?api_key=2yAkthxFVYVxl2go2veb8zmxB8IVKfXl&radius=75&zip={}&body_type={}&exterior_color={}&miles_range={}&price_range={}&rows=50&photo_links=true'

        return url

    @staticmethod
    def lookup_budget_anymileage():
        url= 'https://marketcheck-prod.apigee.net/v1/search?api_key=2yAkthxFVYVxl2go2veb8zmxB8IVKfXl&radius=75&zip={}&body_type={}&exterior_color={}&price_range={}&rows=50&photo_links=true'
        # url1= 'https://marketcheck-prod.apigee.net/v1/search?api_key=2yAkthxFVYVxl2go2veb8zmxB8IVKfXl&radius=75&zip=07030&body_type=SUV&exterior_color=black&price_range=12000-15000&photo_links=true'

        return url

    @staticmethod
    def lookup_new_car():
        url='https://marketcheck-prod.apigee.net/v1/search?api_key=2yAkthxFVYVxl2go2veb8zmxB8IVKfXl&radius=75&zip={}&car_type=new&make={}&model={}&rows=50&stats=price&photo_links=true'

        return url


    @staticmethod
    def lookup_new_car_years():
        url='https://marketcheck-prod.apigee.net/v1/search?api_key=2yAkthxFVYVxl2go2veb8zmxB8IVKfXl&radius=75&zip={}&car_type=used&year={}&make={}&model={}&rows=50&stats=price&photo_links=true'

        return url

    @staticmethod
    def look_up_ninetees():
        url= 'https://marketcheck-prod.apigee.net/v1/search?api_key=2yAkthxFVYVxl2go2veb8zmxB8IVKfXl&year={}&make={}&model={}&stats=price'

        return url