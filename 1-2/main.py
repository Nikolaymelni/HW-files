with open('recipes.txt', encoding='utf-8') as f:
    lines = f.readlines()
    recipe = [[]]
    cook_book = {}
    for string in lines:
        if string != '\n':
            if '|' in string:
                recipe[-1].append(string.strip().split('|'))
            else:
                recipe[-1].append(string.strip())
        else:
            recipe.append([])
    for dish in recipe:
        value = []
        for ingredient in dish:
            if type(ingredient) == list:
                dict_ingredient = dict(ingredient_name=ingredient[0], quantity=ingredient[1], measure=ingredient[2])
                value.append(dict_ingredient)
        cook_book[dish[0]] = value


def get_shop_list_by_dishes(dishes, persons):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for dict_ingredients in cook_book[dish]:
                if dict_ingredients['ingredient_name'] not in shop_list:
                    shop_list[dict_ingredients['ingredient_name']] = dict(measure=dict_ingredients['measure'], quantity=int(
                        dict_ingredients['quantity']) * persons)
                else:
                    shop_list[dict_ingredients['ingredient_name']] = dict(measure=dict_ingredients['measure'], quantity=int(
                        dict_ingredients['quantity']) * persons + shop_list[dict_ingredients['ingredient_name']].pop(
                        'quantity'))

        else:
            return f'Такого блюда нет, либо неверный регистр'
    return shop_list


print(cook_book)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
