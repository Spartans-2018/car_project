
from queryMarketCheck import Query
from controller_car import Controller
from DAO_car import Dao
from program_manager import Manage_budget_data as MD
from program_manager import Manage_new_car_search as NC

from flask import Flask, jsonify, request, render_template
import json
import time



app = Flask(__name__, template_folder= 'ui\src\index.html')





@app.route('/search_make/<make>', methods= ['GET'])
def search_make (make):
    model=[]
    if make=='Honda':
        model=["Civic", "Accord"]
        print (model)
    elif make=='BMW':
        model=["3 Series", "5 Series", 'X3', 'X5']
        print(model)
    elif make=='Audi':
        model=['A4', 'A6', 'Q5', 'Q7']
        print(model)

    elif make=='Toyota':
        model=['Corolla', 'Camry', 'RAV4']

    elif make== 'Nissan':
        model= ['Sentra', 'Altima']
    
    model_jason=json.dumps(model)

    return model_jason

# @app.route('/search/<make>/<model>/<fromyear>/<toyear>', methods=['GET'])
# def complete_make(make, model, fromyear, toyear):

#     diction={'make': make, 'From Year': fromyear}
#     make_dict=jsonify(carsearch=diction)
#     return make_dict



# @app.route('/search/test/', methods= ['GET'])
# def test_dict():
#     diction={'price':0, 'make':"Honda"}
#     make_dict=jsonify(Carsearch=diction)
#     return make_dict


@app.route('/search-car/<zip_code>/<year>/<make>/<model>/', methods=['GET'])
def search_car(zip_code, year, make, model, state):
    
    "Call on queryMarket to search for the car on Market Check API"
    make_list=make.split(',')
    model_list=model.split(',')
    
    ymm=year+'%7C'+str(make_list[0])+'%7C'+str(model_list[0])+'%2C'+year+'%7C'+str(make_list[1])+'%7C'+str(model_list[1])

    car_dict=Query.search1(zip_code, ymm, state)

   # Controller().test_dict(car_dict)

    # time.sleep(15)
    car_data=jsonify(car_dict)



    graph_data= Controller().handle_car_api_data(car_dict)
    
    return graph_data

@app.route('/search-cars/<zip_code>/<from_year>/<to_year>/<make>/<model>', methods=['GET'])
def search_car1(zip_code, from_year, to_year, make, model):
    make_list = make.split(',')
    model_list = model.split(',')
    zip_code_list= zip_code.split(',')

    from_year_list = from_year.split(',')
    to_year_list = to_year.split(',')

    from_year_list = [int(x) for x in from_year_list]
    from_year_list.sort()
    to_year_list = [int(x) for x in to_year_list]
    to_year_list.sort(reverse=True)
    p=0

    if from_year_list[0]==to_year_list[0]:
        year_range= from_year_list[0]

    else:
        year_range=list(range(from_year_list[0], to_year_list[0]+1))
    

    
    for i in range (len(make_list)):
        for j in year_range:
            year= str(j)
            car_dict=Query().search2(zip_code_list[i],year, make_list[i], model_list[i])
            p=p+1
            Controller().handle_data(car_dict, zip_code_list[i]) 
            # time.sleep(2)


    
    graph_data= Dao.graph_plot(make_list, model_list)

    return graph_data

@app.route('/search-budget/<budget>/<car_type>/<milieage>/<zip_code>/<color>', methods=['GET'])
def budget_search(budget, car_type, milieage, zip_code, color):

    # budget_range_tup=(int(budget)-500, int(budget)+500)
    # budget_range_str= str(budget_range_tup[0]) +'-'+str(budget_range_tup[1])
    # milieage_range_str='0'+ milieage

    # budget_dict=Query.budget_search(budget_range_str, car_type, milieage_range_str, zip_code, color)
   
    # return budget_data

   # budget_data=MD().sort_mileage(budget_dict)

   
    budget_dict= MD().budget_search_manager(budget, car_type, milieage, zip_code, color)
    budget_data= jsonify(budget_dict)

    # with open('./ui/src/js/components/car_data1.json', 'w' ) as fp:
    #     json.dump(budget_dict['listings'], fp)

    return budget_data




@app.route('/search-newcar/<make>/<model>/<zip_code>', methods= ['GET'])
def new_car_search(make, model, zip_code):

    new_car_graph_data= NC().new_car_years(make, model, zip_code)
    
    
    
    return new_car_graph_data

    


  




if __name__ == "__main__":
    app.run(debug=True)