from queryMarketCheck import Query
from controller_car import Controller
import time

# from_year=['2011', '2012', '2009']
# from_year = [int(x) for x in from_year]
# from_year.sort()
# year_range=list(range(from_year[0], from_year[2]+1))
# print (year_range)

# car_dict= Query.search2('07030', '2011', 'Honda', "Civic" )

# print (car_dict['stats']['price']['median'])


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

            varia=zip_code_list[i],year, make_list[i], model_list[i]
            p=p+1



            car_dict=Query().search2(zip_code_list[i],year, make_list[i], model_list[i])
            
            Controller().handle_data(car_dict)
        
            time.sleep(3)

    print(p)

search_car1('07030,07030', '2017,2018', '2017,2018', 'Honda,Audi', 'Civic,A4')