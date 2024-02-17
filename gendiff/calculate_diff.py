def check_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def added(key, value):
    return {
        'key': key,
        'type': 'added',
        'new_value': value
    }


def deleted(key, value):
    return {
        'key': key,
        'type': 'deleted',
        'old_value': value
    }


def changed(key, old_value, new_value):
    return {
        'key': key,
        'type': 'changed',
        'old_value': old_value,
        'new_value': new_value
    }


def unchanged(key, value):
    return {
        'key': key,
        'type': 'unchanged',
        'value': value
    }


def nested(key, value_1, value_2):
    return {
        'key': key,
        'type': 'nested',
        'children': calculate_diff(value_1, value_2)
    }


def calculate_diff(file_data1, file_data2):
    diff_list = []
    all_keys = file_data1.keys() | file_data2.keys()
    added_keys = file_data2.keys() - file_data1.keys()
    deleted_keys = file_data1.keys() - file_data2.keys()
    list_keys = sorted(list(all_keys))
    for k in list_keys:
        value_1 = check_value(file_data1.get(k))
        value_2 = check_value(file_data2.get(k))
        if k in added_keys:
            diff_list.append(added(k, value_2))
        elif k in deleted_keys:
            diff_list.append(deleted(k, value_1))
        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            diff_list.append(nested(k, value_1, value_2))
        elif value_1 == value_2:
            diff_list.append(unchanged(k, value_1))
        else:
            diff_list.append(changed(k, value_1, value_2))
    return diff_list
