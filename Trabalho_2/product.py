from category import Category

class Product:

    def __init__(self, name, description, date_fabrication, is_active, category = Category):
        self._name = name
        self._description = description
        self._date_fabrication = date_fabrication
        self._is_active = is_active
        self._category = category

    def getProductDetails(self):
        print("------------Product details------------")
        print(f"Name: {self._name} \nCategory: {self._category.getName()}\n")

    def getProductName(self):
        return self._name