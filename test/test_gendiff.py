from gendiff import generate_diff
import os
import pytest


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)

def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_plain_json():
    # build fixture path
    file_path_1 = get_fixture_path('plain_file_1.json')
    file_path_2 = get_fixture_path('plain_file_2.json')
    # read expended result
    expended = read(get_fixture_path('plain_diff_json.txt'))
    # generate our result
    result = generate_diff(file_path_1, file_path_2, 'stylish')
    # compare our and expended result
    assert expended == result


def test_plain_yaml():
    # build fixture path
    file_path_1 = get_fixture_path('plain_file_1.yml')
    file_path_2 = get_fixture_path('plain_file_2.yml')
    # read expended result
    expended = read(get_fixture_path('plain_diff_json.txt'))
    # generate our result
    result = generate_diff(file_path_1, file_path_2, 'stylish')
    # compare our and expended result
    assert expended == result


def test_nested_json():
    # build fixture path
    file_path_1 = get_fixture_path('nested_file_1.json')
    file_path_2 = get_fixture_path('nested_file_2.json')
    # read expended result
    expended = read(get_fixture_path('nested_diff_json.txt'))
    # generate our result
    result = generate_diff(file_path_1, file_path_2, 'stylish')
    # compare our and expended result
    assert expended == result


def test_plain_format_nested_json():
    # build fixture path
    file_path_1 = get_fixture_path('nested_file_1.json')
    file_path_2 = get_fixture_path('nested_file_2.json')
    # read expended result
    expended = read(get_fixture_path('plain_diff_nested_json.txt'))
    # generate our result
    result = generate_diff(file_path_1, file_path_2, 'plain')
    # compare our and expended result
    assert expended == result