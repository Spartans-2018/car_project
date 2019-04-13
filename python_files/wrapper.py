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
        url= 'https://marketcheck-prod.apigee.net/v1/search?api_key=2yAkthxFVYVxl2go2veb8zmxB8IVKfXl&radius=75&zip={}&body_type={}&miles_range={}&price_range={}&rows=50'

        return url