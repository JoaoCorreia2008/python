def new_product(product , prico, iva):
    return {
        'produtos' : product,
        'price' : prico,
        'tax' : iva
   }
def update_final_price(dicion):
    dicion['final_price'] = round(dicion['price'] * (1 + dicion['tax']),2)

def print_product(p):
    print(f'{p['product']}; Preço: {p['price']};',sep='\n')
    print(f'iva: {p['tax']* 100}%, preço final: {p['final_price']}')
