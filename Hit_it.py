import requests
import json
from pandas import json_normalize

# set up the request parameters
params = {
  'api_key': '',    								#Enter your Rainforest API_Key
  'type': 'search',
  'amazon_domain': 'amazon.de',
  # 'asin' : 'B000M00404',
  'search_term':'lotion'
  
}

# make the http GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)

# print the JSON response from Rainforest API
response = api_result.json()
# print(json.dumps(response))

#  Working code
response_string = {'product_name':response['product']['title'],
'category': response['product']['categories'][5]['name'],
'unit': response['product']['specifications'][1]['value'],
'product_brand': response['product']['brand'],
'imageURL': response['product']['main_image']['link']}

#Search
response_string = {'search_results':response['search_results']}
#works 
with open('product_info.json', 'w') as fp:
     json.dump(response_string, fp,indent=4)


for i in data['product_name'][]: 
  print(i)
    product_info = {'product_name':product['position']} 
with open('productinfo.json', 'a') as fp:
     json.dump(product_info, fp,indent=4)

f = open('product.json','r')     
data = json.load(f)
print(json_normalize(data))     
