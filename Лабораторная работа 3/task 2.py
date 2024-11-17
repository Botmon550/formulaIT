# TODO Напишите функцию find_common_participants
def find_common_participants(first_group: str, second_group: str, separator: str = ",") -> list[str]:
    first_group_set = set(first_group.split(separator))
    second_group_list = second_group.split(separator)

    group_intersections = first_group_set.intersection(second_group_list)
    res = sorted(group_intersections)

    return res


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
