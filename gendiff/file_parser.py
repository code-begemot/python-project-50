import json
import yaml


def file_parser(file_path):
    if file_path.endswith('json'):
        data = json.load(open(file_path))
    elif file_path.endswith(('yaml', 'yml')):
        data = yaml.safe_load(open(file_path))
    return data
