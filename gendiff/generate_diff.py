from gendiff.calculate_diff import calculate_diff
from gendiff.file_parser import file_parser
from gendiff.file_formatter import file_formatter


def generate_diff(file_path_1, file_path_2, format):
    # parsing files
    file_data_1 = file_parser(file_path_1)
    file_data_2 = file_parser(file_path_2)
    # building
    diff = calculate_diff(file_data_1, file_data_2)
    # format output
    result = file_formatter(diff, format)
    return result
