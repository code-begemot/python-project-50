import itertools
import json

def file_formatter(value, format):
    output = eval(f'{format}_format')(value)
    return output


def stylish_format(value, replacer=' ', spacesCount=4):
    def iter_(current_value, depth):
        lines = []
        current_indent = depth * replacer
        if not isinstance(current_value, dict):
            return str(current_value)
        deep_indent_size = depth + spacesCount
        deep_indent = deep_indent_size * replacer
        for i in current_value.items():
            key, val = i
            if key[1] == ' ':
                lines.append(f'{deep_indent[:-2]}{key}: {iter_(val, deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        return '\n'.join(itertools.chain("{", lines, [current_indent + "}"]))
    return iter_(value, 0)


def plain_format(value, replacer=' ', spacesCount=4):
    new_lines = []

    def iter_(current_value, path):
        current_path = path
        if not isinstance(current_value, dict):
            return str(current_value)
        for i in current_value.items():
            key, val = i
            temp_val = current_value.get(f'+ {key[2:]}')
            temp_key = key.split(' ')[-1]
            if current_path != '':
                deep_path = f'{current_path}.{temp_key}'
            else:
                deep_path = temp_key
            temp_value_before = '[complex value]' if isinstance(val, dict) else (val if val in ('true', 'false', 'null', '0') or isinstance(val, int) or isinstance(val, float) else f"'{val}'")
            temp_value_after = '[complex value]' if isinstance(temp_val, dict) else (temp_val if temp_val in ('true', 'false', 'null', '0') or isinstance(val, int) or isinstance(val, float) else f"'{temp_val}'")
            if key[0] == '-' and f'+ {key[2:]}' in current_value:
                new_lines.append(f"Property '{deep_path}' was updated. From {temp_value_before} to {temp_value_after}")
            elif key[0] == '-' and not f'+ {key[2:]}' in current_value:
                new_lines.append(f"Property '{deep_path}' was removed")
            if key[0] == '+' and not f'- {key[2:]}' in current_value:
                new_lines.append(f"Property '{deep_path}' was added with value: {temp_value_before}")
            else:
                iter_(val, deep_path)
        return '\n'.join(new_lines)
    return iter_(value, '')


def json_format(value, replacer = ' ', spacesCount = 4):
    result = json.dumps(value)
    print(result)
    return result