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
    