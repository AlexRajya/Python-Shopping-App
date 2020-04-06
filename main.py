import requests
import json

def main():
    bbProducts = getBestBuy()
    print(bbProducts)
    tescoProducts = getTesco()
    print(tescoProducts)
    
def getBestBuy():
    search = input("Enter search query: ")
    bestBuy = requests.get('https://api.bestbuy.com/v1/products(search='+search+')?format=json&show=image,name,salePrice&apiKey=lfXY4GpC14duGk4N3uGvGD3d')
    print(bestBuy.status_code) #200 = OK 
    result = json.loads(bestBuy.text)
    return result['products']

def getTesco():
    search = input("Enter search query: ")
    tesco = requests.get(f"https://dev.tescolabs.com/grocery/products/?query="+search+"&offset=0&limit=13&",
        headers={
        "Ocp-Apim-Subscription-Key": 'b1ef4204177a4deb86619436f9e1e7a6'
        }
    )
    print(tesco.status_code)
    result = json.loads(tesco.text)
    return result['uk']['ghs']['products']['results']

    
main()