
import sqlite3
from flask import Flask, jsonify
from DAO_car import Dao
import pandas as  pd
import numpy as np

from numpy import median
class Controller:
    def __init__(self):
        pass

    @staticmethod
    def get_connection():
        conn = sqlite3.connect ("car.db")
        return conn 



    def handle_car_api_data(self, car_dict):

       
        # title= movie_dict['Title']
        # year=movie_dict['Year']
        # runtime= movie_dict['Runtime']
        # genre= movie_dict['Genre']
        # Dao.save_movie(title, year, runtime, genre)


        car_price=[]
        for i in range (len(car_dict['listings'])):
            try:
                list_price=car_dict['listings'][i]['price']
                car_price.append(list_price)

            except:
                continue

        price= round(median(car_price), 0)
        make=[]
        model=[]
        # make.append(car_dict['listings'][0]['build']['make'])
        # model.append(car_dict['listings'][0]['build']['model'])
        year=car_dict['listings'][0]['build']['year']
        zip_code= car_dict['listings'][0]['dealer']['zip']

        for i in range(len(car_dict['listings'])):
            try:
                make_elem=car_dict['listings'][i]['build']['make']
                model_elem= car_dict['listings'][i]['build']['model']
                if make_elem not in make:
                   make.append(make_elem)
                elif model_elem not in model:
                    model.append(model_elem)
                
            except:
                continue

        
        print (make)
        print (model)

        Dao.save_make(make[0], model[0], year, price, zip_code)
        Dao.save_make(make[1], model[1], year, price, zip_code)
        graph_data= Dao.graph_plot(make,model)

        return graph_data



    def handle_data(self, car_dict, zip_code):
        
        for i in range(len(car_dict['listings'])):
            try:
                make=car_dict['listings'][i]['build']['make']
                model= car_dict['listings'][i]['build']['model']
                year=car_dict['listings'][i]['build']['year']
                break
                
            except:
                continue

        
        
        price= car_dict['stats']['price']['median']
        
        Dao.save_make(make, model, year, price, zip_code)
        

        

        

    
    def graph_controller(self, car_dict):
        pass
        
    

