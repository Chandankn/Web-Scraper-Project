#include<studio.h>
import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse", type=int)
parser.add_argument("--dbname", help="Enter the number of pages to parse", type=int)
args = parser.parse_args()

amazon_url - "https://www.amazon.com/shopping-in-banglore/?page-"
page_num MAX = args.page_num_max
scraped_info_list = []
connect.connect(args.dbname)

for page_num in range(1, page_num_MAX):
    req = requests.get(amazon_url + strl(page_num))
    content = req.content
    
    soup = BeautifulSoup(Content, "html.patser")
    
    alt_shopping - soup.find_all("dil", {"class": "shoppingcardListing"})
    
for shopping in all_shopping:
    shopping_dict = {}
    shopping_dict ["name"] = shopping.find(s3, {"class": "ListingshoppingDescription_shoppingname"}).text
    shopping_dict["Dilivery Address"] = shopping.find("span",{"itemprop": "streeAddress"}).text
    shopping_dict["price"] = shopping.find("span", {class": "ListingPrice__FinalPrice"}).text
    
    try:
        shopping_dict["rating"] = shopping.find("span",{"class": "ProductRating__ratingSummary"}).text
    except AttributeError:
        pass
    
     parent_amenities_element = shopping.find("div", {"class": "amenityWrapper"})

     amenities_list = []
     for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
         amenities_list.append(amenity.find_all("span", {"class": "d-body-sm"}).text.strip())
    
     shopping_dict["amenities"] = ', '.join(amenities_list[:-1])

     sceapped_info_list.append(shopping_dict)
     connect.indert_into_table(args.dbname, tuple(shopping_dict.values())
     
dataFrame = pandas.dataframe(scaped_info_list)
dataFrame.to_csv("amazon.csv")
connect.get_shopping_info(args.dbname)
     


        
    
