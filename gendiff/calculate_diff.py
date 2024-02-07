def check_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def calculate_diff(file_data1, file_data2):
    def inner(current_data1, current_data2):
        new_dict = {}
        all_keys = set(current_data1.keys() | current_data2.keys())
        list_keys = sorted(list(all_keys))
        for k in list_keys:
            value_1 = check_value(current_data1.get(k, 'absent'))
            value_2 = check_value(current_data2.get(k, 'absent'))
            if value_2 == 'absent':
                new_dict[f'- {k}'] = value_1
            elif value_1 == 'absent':
                new_dict[f'+ {k}'] = value_2
            elif value_1 == value_2:
                new_dict[f'  {k}'] = value_1
            elif value_1 != value_2 and isinstance(value_1, dict) \
                    and isinstance(value_2, dict):
                new_dict[f'  {k}'] = inner(value_1, value_2)
            else:
                new_dict[f'- {k}'] = value_1
                new_dict[f'+ {k}'] = value_2
        return new_dict
    return inner(file_data1, file_data2)
