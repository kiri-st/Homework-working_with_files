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

    print(cook_book)