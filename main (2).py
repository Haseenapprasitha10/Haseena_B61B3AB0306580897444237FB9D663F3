def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices

# Example usage:
products_list = ["product1", "product2", "product3", "product2", "product4", "product2"]
target_product = "product2"
result = linear_search_product(products_list, target_product)
print("Indices of occurrences:", result)