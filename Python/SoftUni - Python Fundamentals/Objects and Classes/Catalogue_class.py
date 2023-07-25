class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product: str):
        Catalogue.products.append(product)

    def get_by_letter(self, first_letter: str):
        # filtered_products = []
        # for product in Catalogue.products:
        #     if product[0].upper() == first_letter.upper():
        #         filtered_products.append(product)
        # return filtered_products
        return [product for product in Catalogue.products if product.startswith(first_letter)]

    def __repr__(self):
        sorted_products = sorted(Catalogue.products)
        return_string = f"Items in the {self.name} catalogue:\n"
        return_string += "\n".join(sorted_products)
        return return_string

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
