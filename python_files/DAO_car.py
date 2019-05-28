import sqlite3
import sqlite3
import matplotlib.pyplot as plt
import json


class Dao:
   
    def __init__(self):
       pass

    @staticmethod
    def get_connection():
        conn = sqlite3.connect ("car.db")
        return conn   

    @staticmethod
    def save_make(make_name, model, year, price, zip_code):
        conn=Dao.get_connection()

        sql="INSERT INTO makes(make_name, model_name, year, price, zip) VALUES (?,?,?,?, ?)"
        conn.execute(sql, (make_name, model, year, price, zip_code))
        conn.commit()
        conn.close()
        

    @staticmethod
    def save_mrsp(mrsp):
        conn=Dao.get_connection()

        sql="INSERT INTO makes(mrsp) VALUES (?)"
        conn.execute(sql, (mrsp))
        conn.commit()
        conn.close()
        


    @staticmethod
    def save_model(model_name):
        conn=Dao.get_connection()
        sql="INSERT INTO models(model_name) VALUES (?)"
        conn.execute(sql, (model_name))
        conn.commit()
        conn.close()

    
    @staticmethod
    def save_makes_models(make_id, model_id):
        conn=Dao.get_connection() 
        sql='INSERT INTO makes_models (make_id, model_id)) VALUES (?,?)'
        conn.execute(sql, (make_id, model_id))
        conn.commit()
        conn.close()
        

    

    @staticmethod
    def select():
        conn=Dao.get_connection()
        sql='SELECT * FROM movies'
        conn.execute(sql)
        conn.commit()
        conn.close()


    @staticmethod
    def graph_plot(make_list, model_list):
        conn = sqlite3.connect('car.db')
        c = conn.cursor()
        c.execute('SELECT year, price FROM makes WHERE make_name=? AND model_name=?;', (make_list[0], model_list[0]))
        data_car1= c.fetchall()
        

        
        c.execute('SELECT year, price FROM makes WHERE make_name=? AND model_name=?;', (make_list[1], model_list[1]))
        data_car2=c.fetchall()
        c.close()
        conn.close()

        data_car1.sort(reverse=True)
        data_car2.sort(reverse=True)
        years_car1=[]
        prices_car1=[]

        for row in data_car1:
            years_car1.append(row[0])
            prices_car1.append(row[1])
            
        years_car2=[]
        prices_car2=[]
        for row in data_car2:
            years_car2.append(row[0])
            prices_car2.append(row[1])

        # plt.plot(years_car1, prices_car1, label=make_list[0]+model_list[0])
        # plt.plot(years_car2, prices_car2, label=make_list[1]+model_list[1])
        # plt.xlabel('Year')
        # plt.ylabel('Price')
        # plt.legend()
        # plt.show()
        graph_dict= {'x1': prices_car1, 'y1':years_car1, 
                    'x2': prices_car2, 'y2':years_car2,
                    'makeModel1':make_list[0]+', '+ model_list[0],
                    'makeModel2':make_list[1]+', '+ model_list[1],
                    }
    
        graph_data=json.dumps(graph_dict)

        return graph_data







# if __name__ == "__main__":
#     Dao.select()