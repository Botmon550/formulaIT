# TODO Напишите функцию для поиска индекса товара
def get_first_index(goods: list[str], item: str) -> int | None:
    index = None
    n = len(goods)

    for i in range(n):
        cur_item = goods[i]
        if cur_item == item:
            index = i
            break

    return index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    # TODO Вызовите функцию, что получить индекс товара
    index_item = get_first_index(goods=items_list, item=find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
