# astr='2011,2012'
# bstr='2010'
# print (astr.split(',')[1])
# print (bstr.split(',')[0])

import pandas as pd
import numpy as np
from numpy import median
import sqlite3
import matplotlib.pyplot as plt
import mpld3
import json





def search_car(zip_code, year, make, model, state):
    
    "Call on queryMarket to search for the car on Market Check API"
    
    make_lst=make.split(',')
    ll=len(make_lst)
    if len(make_lst)==1:
        make=make_lst[0]
    else:
        make=''
        for i in range(0,(len(make_lst)-1)):
            make=make+str(make_lst[i])+'%2C'

        make=make+str(make_lst[len(make_lst)-1])

    print (make)


# search_car('07030', '2011', 'bmw,audi,honda,ford', 'x3', 'nj')
false=''
true=''


car_dict={
  "listings": [
    {
      "build": {
        "antibrake_sys": "4-Wheel ABS", 
        "body_type": "Sedan", 
        "city_miles": "23 miles/gallon", 
        "cylinders": 4, 
        "doors": 4, 
        "drivetrain": "FWD", 
        "engine": "2.4L L4 DOHC 16V", 
        "engine_block": "I", 
        "engine_size": 2.4, 
        "fuel_type": "Regular Unleaded", 
        "highway_miles": "34 miles/gallon", 
        "made_in": "United States", 
        "make": "Honda", 
        "model": "Accord", 
        "overall_height": "58.10 Inches", 
        "overall_length": "194.90 Inches", 
        "overall_width": "72.70 Inches", 
        "std_seating": "5", 
        "steering_type": "R&P", 
        "tank_size": "18.5 gallon", 
        "transmission": "Automatic", 
        "trim": "EX-L", 
        "trim_r": "Ex-L Sedan", 
        "vehicle_type": "Car", 
        "year": 2011
      }, 
      "carfax_1_owner": false, 
      "carfax_clean_title": false, 
      "data_source": "mc", 
      "dealer": {
        "city": "Union City", 
        "country": "US", 
        "dealer_type": "independent", 
        "id": 1086703, 
        "latitude": "40.7775", 
        "longitude": "-74.0282", 
        "name": "City Auto Sales", 
        "phone": "201-746-4139", 
        "state": "NJ", 
        "street": "4014 Kennedy Blvd", 
        "website": "www.cityautonj.com", 
        "zip": "07087"
      }, 
      "dist": 1.9, 
      "dom": 5, 
      "dom_180": 5, 
      "dom_active": 5, 
      "exterior_color": "BLUE", 
      "first_seen_at": 1553723087, 
      "first_seen_at_date": "2019-03-27T21:44:47.000Z", 
      "heading": "2011 Honda Accord EX-L Sedan 4D", 
      "id": "1HGCP2F83BA034319-4abd25f5-9cf4-4ddd-9929-bfd2b5c6640e", 
      "interior_color": "Leather", 
      "inventory_type": "used", 
      "last_seen_at": 1553806851, 
      "last_seen_at_date": "2019-03-28T21:00:51.000Z", 
      "media": {
        "photo_links": [
          "https://imagescdn.dealercarsearch.com/DealerImages/15704/15704_newarrivalphoto.jpg"
        ]
      }, 
      "miles": 73000, 
      "ref_miles": 73000, 
      "ref_miles_dt": 1553734442, 
      "scraped_at": 1553723087, 
      "scraped_at_date": "2019-03-27T21:44:47.000Z", 
      "seller_type": "dealer", 
      "source": "www.cityautonj.com", 
      "stock_no": "034319", 
      "vdp_url": "https://www.cityautonj.com/2011-Honda-Accord/Used-Car/UnionCity-NJ/12536909/Details.aspx", 
      "vin": "1HGCP2F83BA034319"
    }, 
    {
      "build": {
        "antibrake_sys": "4-Wheel ABS", 
        "body_type": "Sedan", 
        "city_miles": "23 miles/gallon", 
        "cylinders": 4, 
        "doors": 4, 
        "drivetrain": "FWD", 
        "engine": "2.4L L4 DOHC 16V", 
        "engine_block": "I", 
        "engine_size": 2.4, 
        "fuel_type": "Regular Unleaded", 
        "highway_miles": "34 miles/gallon", 
        "made_in": "United States", 
        "make": "Honda", 
        "model": "Accord", 
        "overall_height": "58.10 Inches", 
        "overall_length": "194.90 Inches", 
        "overall_width": "72.70 Inches", 
        "std_seating": "5", 
        "steering_type": "R&P", 
        "tank_size": "18.5 gallon", 
        "transmission": "Automatic", 
        "trim": "SE", 
        "trim_r": "SE Sedan", 
        "vehicle_type": "Car", 
        "year": 2011
      }, 
      "carfax_1_owner": false, 
      "carfax_clean_title": false, 
      "data_source": "mc", 
      "dealer": {
        "city": "Belleville", 
        "country": "US", 
        "dealer_type": "independent", 
        "id": 1086060, 
        "latitude": "40.7823", 
        "longitude": "-74.1539", 
        "name": "WFA Auto Sales", 
        "state": "NJ", 
        "street": "36 WASHINGTON AVE", 
        "website": "wfaauto.com", 
        "zip": "07109"
      }, 
      "dist": 6.86, 
      "dom": 127, 
      "dom_180": 80, 
      "dom_active": 80, 
      "exterior_color": "Gray", 
      "first_seen_at": 1552927541, 
      "first_seen_at_date": "2019-03-18T16:45:41.000Z", 
      "heading": "2011 Honda Accord SE Sedan AT", 
      "id": "1HGCP2F6XBA112884-35846ae2-9981-4f19-9994-290d7abe9fe0", 
      "interior_color": "Leather", 
      "inventory_type": "used", 
      "last_seen_at": 1553881805, 
      "last_seen_at_date": "2019-03-29T17:50:05.000Z", 
      "media": {
        "photo_links": [
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733387914784.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733416657415.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733432280094.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733451808661.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733471649756.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733491805172.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733511179019.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733528990721.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733543208690.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733563363937.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733587581505.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733603049652.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733616645381.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733632891735.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733653672059.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733673671306.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733689764055.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733712419125.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733731480960.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733751323505.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/8572/12161531//636841733770853683.jpg"
        ]
      }, 
      "miles": 107386, 
      "msrp": 10495, 
      "price": 8995, 
      "ref_miles": 107386, 
      "ref_miles_dt": 1553806965, 
      "ref_price": 8995, 
      "ref_price_dt": 1553806965, 
      "scraped_at": 1552927541, 
      "scraped_at_date": "2019-03-18T16:45:41.000Z", 
      "seller_type": "dealer", 
      "source": "wfaauto.com", 
      "vdp_url": "https://wfaauto.com/2011-Honda-Accord/Used-Car/Belleville-NJ/12161531/Details.aspx", 
      "vin": "1HGCP2F6XBA112884"
    }, 
    {
      "build": {
        "antibrake_sys": "4-Wheel ABS", 
        "body_type": "Sedan", 
        "city_miles": "23 miles/gallon", 
        "cylinders": 4, 
        "doors": 4, 
        "drivetrain": "FWD", 
        "engine": "2.4L L4 DOHC 16V", 
        "engine_block": "I", 
        "engine_size": 2.4, 
        "fuel_type": "Regular Unleaded", 
        "highway_miles": "34 miles/gallon", 
        "made_in": "United States", 
        "make": "Honda", 
        "model": "Accord", 
        "overall_height": "58.10 Inches", 
        "overall_length": "194.90 Inches", 
        "overall_width": "72.70 Inches", 
        "std_seating": "5", 
        "steering_type": "R&P", 
        "tank_size": "18.5 gallon", 
        "transmission": "Automatic", 
        "trim": "EX-L", 
        "trim_r": "EX-L", 
        "vehicle_type": "Car", 
        "year": 2011
      }, 
      "carfax_1_owner": false, 
      "carfax_clean_title": false, 
      "data_source": "mc", 
      "dealer": {
        "city": "Lyndhurst", 
        "country": "US", 
        "dealer_type": "franchise", 
        "id": 1022488, 
        "latitude": "40.8079", 
        "longitude": "-74.1365", 
        "name": "Three County Volkswagen Corp", 
        "phone": "877-227-0498 877-438-7817", 
        "state": "NJ", 
        "street": "701 Riverside Avenue", 
        "website": "www.threecountyvw.com", 
        "zip": "07071"
      }, 
      "dist": 6.86, 
      "dom": 15, 
      "dom_180": 11, 
      "dom_active": 11, 
      "exterior_color": "Silver", 
      "first_seen_at": 1553005452, 
      "first_seen_at_date": "2019-03-19T14:24:12.000Z", 
      "heading": "2011 Honda Accord EX-L EX-L Sedan", 
      "id": "1HGCP2F82BA033310-0fe0493f-05f8-4f7e-bc99-93120f4a927b", 
      "inventory_type": "used", 
      "last_seen_at": 1553874225, 
      "last_seen_at_date": "2019-03-29T15:43:45.000Z", 
      "media": {
        "photo_links": [
          "https://pictures.dealer.com/t/threecountyvolkswagencorpvw/1087/9e9800e3055a29b0f37b242093f885f9x.jpg?impolicy=resize&w=190"
        ]
      }, 
      "miles": 59945, 
      "msrp": 11995, 
      "price": 11995, 
      "ref_miles": 59945, 
      "ref_miles_dt": 1553799409, 
      "ref_price": 11995, 
      "ref_price_dt": 1553799409, 
      "scraped_at": 1553005452, 
      "scraped_at_date": "2019-03-19T14:24:12.000Z", 
      "seller_type": "dealer", 
      "source": "www.threecountyvw.com", 
      "stock_no": "20356T", 
      "vdp_url": "https://www.threecountyvw.com/used/Honda/2011-Honda-Accord-4ea531f40a0e0a6b50c4cabfa2125710.htm", 
      "vin": "1HGCP2F82BA033310"
    }, 
    {
      "build": {
        "antibrake_sys": "4-Wheel ABS", 
        "body_type": "Sedan", 
        "city_miles": "20 miles/gallon", 
        "cylinders": 6, 
        "doors": 4, 
        "drivetrain": "FWD", 
        "engine": "3.5L V6 SOHC 24V", 
        "engine_block": "V", 
        "engine_size": 3.5, 
        "fuel_type": "Regular Unleaded", 
        "highway_miles": "30 miles/gallon", 
        "made_in": "United States", 
        "make": "Honda", 
        "model": "Accord", 
        "overall_height": "58.10 Inches", 
        "overall_length": "194.90 Inches", 
        "overall_width": "72.70 Inches", 
        "std_seating": "5", 
        "steering_type": "R&P", 
        "tank_size": "18.5 gallon", 
        "transmission": "Automatic", 
        "trim": "EX-L V-6", 
        "trim_r": "EX-L", 
        "vehicle_type": "Car", 
        "year": 2011
      }, 
      "carfax_1_owner": false, 
      "carfax_clean_title": false, 
      "data_source": "mc", 
      "dealer": {
        "city": "Hasbrouck Heights", 
        "country": "US", 
        "dealer_type": "franchise", 
        "id": 1080905, 
        "latitude": "40.8511", 
        "longitude": "-74.0757", 
        "name": "Autoeastern Nissan of Meadowlands", 
        "state": "NJ", 
        "street": "45 State Rt 17", 
        "website": "www.autoeasternnissan.com", 
        "zip": "07604-2802"
      }, 
      "dist": 7.38, 
      "dom": 577, 
      "dom_180": 577, 
      "dom_active": 577, 
      "exterior_color": "Crystal Black Pearl", 
      "first_seen_at": 1533042683, 
      "first_seen_at_date": "2018-07-31T13:11:23.000Z", 
      "heading": "2011 Honda Accord Sdn EX-L", 
      "id": "1HGCP3F89BA002416-2f32171b-d84c-4fab-9a22-de12061d2662", 
      "interior_color": "Black", 
      "inventory_type": "used", 
      "last_seen_at": 1553883458, 
      "last_seen_at_date": "2019-03-29T18:17:38.000Z", 
      "media": {
        "photo_links": [
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/1.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/2.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/3.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/4.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/5.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/6.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/7.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/8.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/9.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/10.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/11.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/12.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/13.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/14.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/15.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/16.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/17.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/18.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/19.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/20.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/21.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/22.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/23.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/24.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/25.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/26.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/27.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/28.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/colormatched_01/white/640/cc_2011hon003b_01_640/cc_2011hon003b_01_640_bx.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/colormatched_02/white/640/cc_2011hon003b_02_640/cc_2011hon003b_02_640_bx.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/colormatched/white/640/cc_2011hon003b_640/cc_2011hon003b_640_bx.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_11.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_12.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_13.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_18.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_20.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_25.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_28.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_32.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_43.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_44.jpg?width=480", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_45.jpg?width=480", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/1.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/2.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/3.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/4.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/5.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/6.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/7.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/8.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/9.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/10.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/11.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/12.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/13.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/14.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/15.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/16.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/17.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/18.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/19.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/20.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/21.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/22.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/23.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/24.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/25.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/26.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/27.jpg", 
          "https://www.autoeasternnissan.com/inventoryphotos/1241/1hgcp3f89ba002416/ip/28.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/colormatched_01/white/640/cc_2011hon003b_01_640/cc_2011hon003b_01_640_bx.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/colormatched_02/white/640/cc_2011hon003b_02_640/cc_2011hon003b_02_640_bx.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/colormatched/white/640/cc_2011hon003b_640/cc_2011hon003b_640_bx.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_11.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_12.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_13.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_18.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_20.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_25.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_28.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_32.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_43.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_44.jpg", 
          "https://www.autoeasternnissan.com/assets/stock/expanded/white/640/2011hon003b_640/2011hon003b_640_45.jpg"
        ]
      }, 
      "miles": 80009, 
      "msrp": 13987, 
      "price": 10884, 
      "ref_miles": 80009, 
      "ref_miles_dt": 1553808557, 
      "ref_price": 10884, 
      "ref_price_dt": 1553808557, 
      "scraped_at": 1533042683, 
      "scraped_at_date": "2018-07-31T13:11:23.000Z", 
      "seller_type": "dealer", 
      "source": "www.autoeasternnissan.com", 
      "stock_no": "PU474", 
      "vdp_url": "https://www.autoeasternnissan.com/used-Hackensack-2011-Honda-Accord+Sdn-EX+L-1HGCP3F89BA002416", 
      "vin": "1HGCP3F89BA002416"
    }, 
    {
      "build": {
        "antibrake_sys": "4-Wheel ABS", 
        "body_type": "Sedan", 
        "city_miles": "23 miles/gallon", 
        "cylinders": 4, 
        "doors": 4, 
        "drivetrain": "FWD", 
        "engine": "2.4L L4 DOHC 16V", 
        "engine_block": "I", 
        "engine_size": 2.4, 
        "fuel_type": "Regular Unleaded", 
        "highway_miles": "34 miles/gallon", 
        "made_in": "United States", 
        "make": "Honda", 
        "model": "Accord", 
        "overall_height": "58.10 Inches", 
        "overall_length": "194.90 Inches", 
        "overall_width": "72.70 Inches", 
        "std_seating": "5", 
        "steering_type": "R&P", 
        "tank_size": "18.5 gallon", 
        "transmission": "Automatic", 
        "trim": "LX", 
        "trim_r": "LX Sedan AT", 
        "vehicle_type": "Car", 
        "year": 2011
      }, 
      "carfax_1_owner": false, 
      "carfax_clean_title": false, 
      "data_source": "mc", 
      "dealer": {
        "city": "Hasbrouck Heights", 
        "country": "US", 
        "dealer_type": "independent", 
        "id": 1088186, 
        "latitude": "40.8554", 
        "longitude": "-74.0696", 
        "name": "Yes You Drive", 
        "phone": "(973) 419-2929", 
        "state": "NJ", 
        "street": "60 Railroad Ave, Unit 202", 
        "website": "iautomallnj.com", 
        "zip": "7604"
      }, 
      "dist": 7.57, 
      "dom": 172, 
      "dom_180": 65, 
      "dom_active": 65, 
      "exterior_color": "Black", 
      "first_seen_at": 1553100334, 
      "first_seen_at_date": "2019-03-20T16:45:34.000Z", 
      "heading": "2011 Honda Accord LX sedan AT", 
      "id": "1HGCP2F37BA043240-7116a287-e438-4cb0-bd0a-4d0d1982e649", 
      "interior_color": "Cloth", 
      "inventory_type": "used", 
      "last_seen_at": 1553881436, 
      "last_seen_at_date": "2019-03-29T17:43:56.000Z", 
      "media": {
        "photo_links": [
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997417805369.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997376191063.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997378375049.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997380559035.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997382587022.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997490382331.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997493346312.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997495218300.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997497090288.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997498962276.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997591781681.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997593653669.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997595681656.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/13946/12501634//636885997597865642.jpg"
        ]
      }, 
      "miles": 123239, 
      "msrp": 6900, 
      "price": 6900, 
      "ref_miles": 123239, 
      "ref_miles_dt": 1553806337, 
      "ref_price": 6900, 
      "ref_price_dt": 1553806337, 
      "scraped_at": 1553100334, 
      "scraped_at_date": "2019-03-20T16:45:34.000Z", 
      "seller_type": "dealer", 
      "source": "iautomallnj.com", 
      "stock_no": "043240", 
      "vdp_url": "https://iautomallnj.com/2011-Honda-Accord/Used-Car/HasbrouckHeights-NJ/12501634/Details.aspx", 
      "vin": "1HGCP2F37BA043240"
    }, 
    {
      "build": {
        "antibrake_sys": "4-Wheel ABS", 
        "body_type": "Sedan", 
        "city_miles": "23 miles/gallon", 
        "cylinders": 4, 
        "doors": 4, 
        "drivetrain": "FWD", 
        "engine": "2.4L L4 DOHC 16V", 
        "engine_block": "I", 
        "engine_size": 2.4, 
        "fuel_type": "Regular Unleaded", 
        "highway_miles": "34 miles/gallon", 
        "made_in": "United States", 
        "make": "Honda", 
        "model": "Accord", 
        "overall_height": "58.10 Inches", 
        "overall_length": "194.90 Inches", 
        "overall_width": "72.70 Inches", 
        "std_seating": "5", 
        "steering_type": "R&P", 
        "tank_size": "18.5 gallon", 
        "transmission": "Automatic", 
        "trim": "LX-P", 
        "trim_r": "LX-P", 
        "vehicle_type": "Car", 
        "year": 2011
      }, 
      "carfax_1_owner": false, 
      "carfax_clean_title": false, 
      "data_source": "mc", 
      "dealer": {
        "city": "Newark", 
        "country": "US", 
        "dealer_type": "independent", 
        "id": 1073398, 
        "latitude": "40.7215", 
        "longitude": "-74.1786", 
        "name": "Goble Auto Sales", 
        "state": "NJ", 
        "street": "118 Murray Street", 
        "website": "www.gobleusedautosales.com", 
        "zip": "07114"
      }, 
      "dist": 8.03, 
      "dom": 51, 
      "dom_180": 4, 
      "dom_active": 3, 
      "exterior_color": "Gray", 
      "first_seen_at": 1553726964, 
      "first_seen_at_date": "2019-03-27T22:49:24.000Z", 
      "heading": "2011 Honda Accord Sdn 4dr I4 Auto LX-P", 
      "id": "1HGCP2F43BA070749-1bb90720-a139-4502-ad6f-ec1f500056e2", 
      "interior_color": "Black", 
      "inventory_type": "used", 
      "last_seen_at": 1553885594, 
      "last_seen_at_date": "2019-03-29T18:53:14.000Z", 
      "media": {
        "photo_links": []
      }, 
      "miles": 109275, 
      "msrp": 9995, 
      "price": 9595, 
      "ref_miles": 109275, 
      "ref_miles_dt": 1553810749, 
      "ref_price": 9595, 
      "ref_price_dt": 1553810749, 
      "scraped_at": 1553726964, 
      "scraped_at_date": "2019-03-27T22:49:24.000Z", 
      "seller_type": "dealer", 
      "source": "www.gobleusedautosales.com", 
      "stock_no": "070749", 
      "vdp_url": "https://www.gobleusedautosales.com/2011-Honda-AccordSdn/Used-Car/Newark-NJ/12540200/Details.aspx", 
      "vin": "1HGCP2F43BA070749"
    }, 
    {
      "build": {
        "antibrake_sys": "4-Wheel ABS", 
        "body_type": "Coupe", 
        "city_miles": "22 miles/gallon", 
        "cylinders": 4, 
        "doors": 2, 
        "drivetrain": "FWD", 
        "engine": "2.4L L4 DOHC 16V", 
        "engine_block": "I", 
        "engine_size": 2.4, 
        "fuel_type": "Regular Unleaded", 
        "highway_miles": "33 miles/gallon", 
        "made_in": "United States", 
        "make": "Honda", 
        "model": "Accord", 
        "overall_height": "56.40 Inches", 
        "overall_length": "190.90 Inches", 
        "overall_width": "72.80 Inches", 
        "std_seating": "5", 
        "steering_type": "R&P", 
        "tank_size": "18.5 gallon", 
        "transmission": "Automatic", 
        "trim": "EX", 
        "trim_r": "EX Coupe", 
        "vehicle_type": "Car", 
        "year": 2011
      }, 
      "carfax_1_owner": false, 
      "carfax_clean_title": false, 
      "data_source": "mc", 
      "dealer": {
        "city": "Clifton", 
        "country": "US", 
        "dealer_type": "independent", 
        "id": 1035895, 
        "latitude": "40.8773", 
        "longitude": "-74.1342", 
        "name": "Lexington Auto Club", 
        "phone": "973-546-2100", 
        "state": "NJ", 
        "street": "490 Lexington Avenue", 
        "website": "www.lexautoclub.com", 
        "zip": "07011"
      }, 
      "dist": 10.35, 
      "dom": 61, 
      "dom_180": 61, 
      "dom_active": 61, 
      "exterior_color": "Silver", 
      "first_seen_at": 1548712037, 
      "first_seen_at_date": "2019-01-28T21:47:17.000Z", 
      "heading": "2011 Honda Accord EX coupe AT", 
      "id": "1HGCS1B78BA004299-a24b272a-5690-490a-921f-621725f843fe", 
      "interior_color": "Cloth", 
      "inventory_type": "used", 
      "last_seen_at": 1553821264, 
      "last_seen_at_date": "2019-03-29T01:01:04.000Z", 
      "media": {
        "photo_links": [
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842852546068115.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842852451979328.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842852454007315.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842852457595292.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842852460403274.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842852887216538.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842852889712522.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842852892208506.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842852894704490.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842852899696458.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842853227294358.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842853229634343.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842853232130327.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842853236186301.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842853240554273.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842853596387992.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842853598415979.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842853600599965.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842853602783951.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842853605747932.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854208996065.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854211492049.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854213520036.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854216328018.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854218512004.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854722544773.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854724728759.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854726912745.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854729096731.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854731436716.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854964967219.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854967151205.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854969647189.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854971831175.jpg", 
          "https://imagescdn.dealercarsearch.com/Media/2068/12263721//636842854973859162.jpg"
        ]
      }, 
      "miles": 105522, 
      "msrp": 7995, 
      "price": 7995, 
      "ref_miles": 105522, 
      "ref_miles_dt": 1553737169, 
      "ref_price": 7995, 
      "ref_price_dt": 1553737169, 
      "scraped_at": 1548712037, 
      "scraped_at_date": "2019-01-28T21:47:17.000Z", 
      "seller_type": "dealer", 
      "source": "www.lexautoclub.com", 
      "vdp_url": "https://www.lexautoclub.com/2011-Honda-Accord/Used-Car/Clifton-NJ/12263721/Details.aspx", 
      "vin": "1HGCS1B78BA004299"
    }, 
    {
      "build": {
        "antibrake_sys": "4-Wheel ABS", 
        "body_type": "Sedan", 
        "city_miles": "23 miles/gallon", 
        "cylinders": 4, 
        "doors": 4, 
        "drivetrain": "FWD", 
        "engine": "2.4L L4 DOHC 16V", 
        "engine_block": "I", 
        "engine_size": 2.4, 
        "fuel_type": "Regular Unleaded", 
        "highway_miles": "34 miles/gallon", 
        "made_in": "United States", 
        "make": "Honda", 
        "model": "Accord", 
        "overall_height": "58.10 Inches", 
        "overall_length": "194.90 Inches", 
        "overall_width": "72.70 Inches", 
        "std_seating": "5", 
        "steering_type": "R&P", 
        "tank_size": "18.5 gallon", 
        "transmission": "Automatic", 
        "trim": "SE", 
        "trim_r": "SE", 
        "vehicle_type": "Car", 
        "year": 2011
      }, 
      "carfax_1_owner": false, 
      "carfax_clean_title": false, 
      "data_source": "mc", 
      "dealer": {
        "city": "Hillside", 
        "country": "US", 
        "dealer_type": "independent", 
        "id": 1086763, 
        "latitude": "40.697", 
        "longitude": "-74.2228", 
        "name": "Car 2 Sell LLC", 
        "phone": "(347) 478-5492", 
        "state": "NJ", 
        "street": "126 US Highway 22", 
        "website": "car2sell.us", 
        "zip": "07205"
      }, 
      "dist": 10.74, 
      "dom": 22, 
      "dom_180": 7, 
      "dom_active": 7, 
      "exterior_color": "Gray", 
      "first_seen_at": 1553354400, 
      "first_seen_at_date": "2019-03-23T15:20:00.000Z", 
      "heading": "2011 Honda Accord Sdn 4dr I4 Auto SE", 
      "id": "1HGCP2F64BA090185-9fd85a83-46e4-4525-a9df-c0fbf17f7004", 
      "inventory_type": "used", 
      "last_seen_at": 1553881778, 
      "last_seen_at_date": "2019-03-29T17:49:38.000Z", 
      "media": {
        "photo_links": [
          "https://imagescdn.dealercarsearch.com/DealerImages/14449/14449_newarrivalphoto.jpg"
        ]
      }, 
      "miles": 82261, 
      "msrp": 5900, 
      "price": 5900, 
      "ref_miles": 82261, 
      "ref_miles_dt": 1553807092, 
      "ref_price": 5900, 
      "ref_price_dt": 1553807092, 
      "scraped_at": 1553354400, 
      "scraped_at_date": "2019-03-23T15:20:00.000Z", 
      "seller_type": "dealer", 
      "source": "car2sell.us", 
      "stock_no": "BA090185", 
      "vdp_url": "https://car2sell.us/2011-Honda-AccordSdn/Used-Car/Hillside-NJ/12518909/Details.aspx", 
      "vin": "1HGCP2F64BA090185"
    }, 
    {
      "build": {
        "antibrake_sys": "4-Wheel ABS", 
        "body_type": "Coupe", 
        "city_miles": "22 miles/gallon", 
        "cylinders": 4, 
        "doors": 2, 
        "drivetrain": "FWD", 
        "engine": "2.4L L4 DOHC 16V", 
        "engine_block": "I", 
        "engine_size": 2.4, 
        "fuel_type": "Regular Unleaded", 
        "highway_miles": "33 miles/gallon", 
        "made_in": "United States", 
        "make": "Honda", 
        "model": "Accord", 
        "overall_height": "56.40 Inches", 
        "overall_length": "190.90 Inches", 
        "overall_width": "72.80 Inches", 
        "std_seating": "5", 
        "steering_type": "R&P", 
        "tank_size": "18.5 gallon", 
        "transmission": "Automatic", 
        "trim": "EX-L", 
        "trim_r": "EX-L Coupe", 
        "vehicle_type": "Car", 
        "year": 2011
      }, 
      "carfax_1_owner": false, 
      "carfax_clean_title": false, 
      "data_source": "mc", 
      "dealer": {
        "city": "Bergenfield", 
        "country": "US", 
        "dealer_type": "independent", 
        "id": 1061378, 
        "latitude": "40.9161", 
        "longitude": "-73.9971", 
        "name": "Bergenfield Automall", 
        "phone": "888-307-2903", 
        "state": "NJ", 
        "street": "355 S Washington Ave", 
        "website": "bergenfieldautomall.com", 
        "zip": "07621"
      }, 
      "dist": 11.6, 
      "dom": 8, 
      "dom_180": 8, 
      "dom_active": 8, 
      "exterior_color": "White", 
      "first_seen_at": 1553190413, 
      "first_seen_at_date": "2019-03-21T17:46:53.000Z", 
      "heading": "2011 Honda Accord EX-L Coupe AT", 
      "id": "1HGCS1B83BA011377-9c7981d5-69a5-40ab-bf79-b674adac719f", 
      "interior_color": "Leather", 
      "inventory_type": "used", 
      "last_seen_at": 1553813103, 
      "last_seen_at_date": "2019-03-28T22:45:03.000Z", 
      "media": {
        "photo_links": []
      }, 
      "miles": 142535, 
      "msrp": 10400, 
      "price": 7995, 
      "ref_miles": 142535, 
      "ref_miles_dt": 1553729176, 
      "ref_price": 7995, 
      "ref_price_dt": 1553729176, 
      "scraped_at": 1553190413, 
      "scraped_at_date": "2019-03-21T17:46:53.000Z", 
      "seller_type": "dealer", 
      "source": "bergenfieldautomall.com", 
      "stock_no": "HA1377", 
      "vdp_url": "https://bergenfieldautomall.com/2011-Honda-Accord/Used-Car/Bergenfield-NJ/12513484/Details.aspx", 
      "vin": "1HGCS1B83BA011377"
    }, 
    {
      "build": {
        "antibrake_sys": "4-Wheel ABS", 
        "body_type": "Sedan", 
        "city_miles": "20 miles/gallon", 
        "cylinders": 6, 
        "doors": 4, 
        "drivetrain": "FWD", 
        "engine": "3.5L V6 SOHC 24V", 
        "engine_block": "V", 
        "engine_size": 3.5, 
        "fuel_type": "Regular Unleaded", 
        "highway_miles": "30 miles/gallon", 
        "made_in": "United States", 
        "make": "Honda", 
        "model": "Accord", 
        "overall_height": "58.10 Inches", 
        "overall_length": "194.90 Inches", 
        "overall_width": "72.70 Inches", 
        "std_seating": "5", 
        "steering_type": "R&P", 
        "tank_size": "18.5 gallon", 
        "transmission": "Automatic", 
        "trim": "EX-L V-6", 
        "trim_r": "EX-L", 
        "vehicle_type": "Car", 
        "year": 2011
      }, 
      "carfax_1_owner": false, 
      "carfax_clean_title": false, 
      "data_source": "mc", 
      "dealer": {
        "city": "Elizabeth", 
        "country": "US", 
        "dealer_type": "independent", 
        "id": 1085523, 
        "latitude": "40.6592", 
        "longitude": "-74.2237", 
        "name": "Mondino Car Sales LLC", 
        "phone": "908-242-3054", 
        "state": "NJ", 
        "street": "309 Rahway Ave", 
        "website": "mondinocarsales.com", 
        "zip": "07202"
      }, 
      "dist": 11.93, 
      "dom": 165, 
      "dom_180": 14, 
      "dom_active": 14, 
      "exterior_color": "Silver", 
      "first_seen_at": 1552750844, 
      "first_seen_at_date": "2019-03-16T15:40:44.000Z", 
      "heading": "2011 Honda Accord EX-L", 
      "id": "1HGCP3F81BA001521-041ca391-982b-4b07-9589-3f36db5ec049", 
      "interior_color": "Grey", 
      "inventory_type": "used", 
      "last_seen_at": 1553882039, 
      "last_seen_at_date": "2019-03-29T17:53:59.000Z", 
      "media": {
        "photo_links": [
          "https://mondinocarsales.com/service/picture/37321/MV521/5358e18bba15a4f935a5b4bded4b30590a22ecef", 
          "https://mondinocarsales.com/service/picture/37321/MV521/fe12a002f3beb7ec74f772676ebdeb682a5391d2", 
          "https://mondinocarsales.com/service/picture/37321/MV521/40069778dbaef68779015b06aff5b62843dc1390", 
          "https://mondinocarsales.com/service/picture/37321/MV521/d6de57dc016406bd4f67b74ce041a7e12b34a8f4", 
          "https://mondinocarsales.com/service/picture/37321/MV521/fd75958c3cee6a4f5f522d9f3970450706ee9d3d", 
          "https://mondinocarsales.com/service/picture/37321/MV521/de6335eca537d9c9a7e5bc33b032ee40d4d7c6a3", 
          "https://mondinocarsales.com/service/picture/37321/MV521/84d02184f4cbb040f3e499873064afd384fa416f", 
          "https://mondinocarsales.com/service/picture/37321/MV521/7b083410c5a229e1359dd084dc1c38bab12f8763", 
          "https://mondinocarsales.com/service/picture/37321/MV521/bd44a5aebe01ccae521d78f970fb8cedf55573ef", 
          "https://mondinocarsales.com/service/picture/37321/MV521/83794be4fd68e7c88577afb0282bb12e75044378", 
          "https://mondinocarsales.com/service/picture/37321/MV521/9cb404d02b6f59253c1809db63e16944bec2d21d", 
          "https://mondinocarsales.com/service/picture/37321/MV521/b4487bf4f79a6fb29e0375fde2505b888ebcae84", 
          "https://mondinocarsales.com/service/picture/37321/MV521/477047a25868064b1ddf191958c9a4207ba27937"
        ]
      }, 
      "miles": 103005, 
      "price": 8695, 
      "ref_miles": 103005, 
      "ref_miles_dt": 1553807160, 
      "ref_price": 8695, 
      "ref_price_dt": 1553807160, 
      "scraped_at": 1552750844, 
      "scraped_at_date": "2019-03-16T15:40:44.000Z", 
      "seller_type": "dealer", 
      "source": "mondinocarsales.com", 
      "stock_no": "MV521", 
      "vdp_url": "http://mondinocarsales.com/inventory/37321/view/MV521/", 
      "vin": "1HGCP3F81BA001521"
    }
  ], 
  "num_found": 31
}


# t=car_dict['listings'][1]['price']
# print(t)

car_price=[]
for i in range (len(car_dict['listings'])):
    try:
        list_price=car_dict['listings'][i]['price']
        car_price.append(list_price)

    except:
        continue

median_price=np.array(car_price)
mp=median_price.mean()
# print(car_price)

# print('median', round( median(car_price), 0))
# print('average' ,round ( np.average(car_price), 0))

#print(car_dict['listings'][0]['build']['make'])
# print(car_dict['listings'][0]['build']['model'])
#print(car_dict['listings'][0]['build']['year'])
# print(car_dict['listings'][0]['dealer']['zip'])


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

#     plt.plot(years_car1, prices_car1, label=make_list[0]+model_list[0])
#     plt.plot(years_car2, prices_car2, label=make_list[1]+model_list[1])
#     plt.xlabel('Year')
#     plt.ylabel('Price')
#     plt.legend()
#    # plt.show()
#     fig=plt.figure()
#     ht=mpld3.fig_to_html(fig)
#     print(ht)

    graph_dict= {'x': prices_car1, "y":years_car1}
    
    graph_data=json.dumps(graph_dict)

    return graph_data






    
print (graph_plot(['Honda', 'Audi'], ["Accord", 'A6']))

