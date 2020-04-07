import requests
import json

class product:
    def __init__(self,productJson,vendor):
        self.vendor = vendor
        if vendor == "Tesco":
            self.image = productJson['image']
            self.price = productJson['price']
            self.desc = productJson['name']
        else:
            self.image = productJson['image']
            self.price = productJson['salePrice']
            self.desc = productJson['name']
    
class bbSearch:
    def __init__(self,query):
        bestBuy = requests.get('https://api.bestbuy.com/v1/products(search='+query+')?format=json&show=image,name,salePrice&apiKey=lfXY4GpC14duGk4N3uGvGD3d')
        self.result = json.loads(bestBuy.text)
        self.result = self.result['products']
        self.products = productList(self.result, 'BestBuy')
        self.formatted = format(self.products)
    def display(self):
        displayProducts(self.products)

class tescoSearch:
    def __init__(self,query):
        tesco = requests.get(f"https://dev.tescolabs.com/grocery/products/?query="+query+"&offset=0&limit=13&",
            headers={
            "Ocp-Apim-Subscription-Key": 'b1ef4204177a4deb86619436f9e1e7a6'
            }
        )
        self.result = json.loads(tesco.text)
        self.result = self.result['uk']['ghs']['products']['results']  
        self.products = productList(self.result, 'Tesco')
        self.formatted = format(self.products)
    def display(self):
        displayProducts(self.products)

        
def productList(productList, vendor):
    listOfProducts = []
    for i in range(len(productList)):
        listOfProducts.append(product(productList[i],vendor))
    return listOfProducts

def displayProducts(productList):
    for i in range(len(productList)):
        temp = productList[i]
        print(temp.desc+" - Price: £"+str(temp.price)+"\n")
        
def format(productList):
    formatted = ""
    for i in range(len(productList)):
        temp = productList[i]
        formatted += temp.desc+" - Price: £"+str(temp.price)+"\n"
    return formatted