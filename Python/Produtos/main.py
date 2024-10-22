import products as p
produtos = []


produtos.append(p.new_product ('Calça',12.93,0.06))
produtos.append(p.new_product ('Camisola',15,0.25))
produtos.append(p.new_product ('pisantes',190,0.13))



for product in produtos:
    p.update_final_price(product)
    p.print_product(product)

# print(*produtos, sep='\n')