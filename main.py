# /task_1///////////////////////////////////////////////////////////////////////////////////////////////////////////////
from pprint import pprint
with open('recipes.txt', 'r', encoding='utf-8') as f:
    file = f.read().split('\n')

    splitted_text = [[]]
    [splitted_text.append([]) if text == '' else splitted_text[-1].append(text) for text in file]

    cook_book = {}
    product_list = []

    for text in splitted_text:
        quantity = 2 + int(text[1])
        for number in range(2, quantity):
            quantity -= 1
            product_dict = {}

            product_dict['ingredient_name'] = text[number].split('|')[0]
            product_dict['quantity'] = text[number].split('|')[1]
            product_dict['measure'] = text[number].split('|')[2]
            product_list.append(product_dict)
            cook_book[text[0]] = product_list
        product_list = []
    pprint(cook_book)

# /task_2///////////////////////////////////////////////////////////////////////////////////////////////////////////////
def get_shop_list_by_dishes(dishes, person_count):
    must_have_products = {}
    dishes_list = cook_book.keys()
    for dish in dishes:
        if dish in dishes_list:
            products = cook_book[dish]
            for product in products:
                product_count = int(product.get('quantity')) * person_count
                must_have_products[product.get('ingredient_name')] = {'measure': product.get('measure'),
                                                                      'quantity': product_count}
    return must_have_products
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# /task_3///////////////////////////////////////////////////////////////////////////////////////////////////////////////
with (open('1.txt', 'r', encoding='utf-8') as txt_1,
      open('2.txt', 'r', encoding='utf-8') as txt_2,
      open('3.txt', 'r', encoding='utf-8') as txt_3,
      open('completed_text_for_task_3.txt', 'w', encoding='utf-8') as completed_text):

    all_text_dict = ({'1.txt': txt_1.readlines(),
                     '2.txt': txt_2.readlines(),
                     '3.txt': txt_3.readlines()})

    sorting_str = dict(sorted(all_text_dict.items(), key=lambda item: item[1], reverse=True))

    for str_ in sorting_str.items():
        completed_text.write(f'{str_[0]}\n')
        completed_text.write(f'{len(str_[1])}\n')
        completed_text.write(f'\n')
        for line in str_[1]:
            if '\n' in line:
                completed_text.write(line)
            else:
                completed_text.write(f'{line}\n\n')