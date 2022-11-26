from typing import List
from collections import defaultdict


def reading_input() -> List[str]:
    count_numbers = int(input())
    result_array = []
    for i in range(count_numbers):
        string_array = input()
        result_array.append(string_array)
    return result_array


def sum_clien_time_in_log(raw_string: List[str]) -> List[int]:
    dict_client = defaultdict(list)
    for raw in raw_string:
        row = raw.split(" ")
        all_minutes = int(row[0]) * 1440 + int(row[1]) * 60 + int(row[2])
        dict_client[int(row[3])].append([all_minutes, row[4]])
    sorted_dict = dict(sorted(dict_client.items(), key=lambda x: x[0]))
    result = []
    start_point, end_point = 0, 0
    for key, value in sorted_dict.items():
        key_results = []
        sorted_lists = sorted(value, key=lambda student: student[0])
        for row in sorted_lists:
            if row[1] == "A":
                start_point = row[0]
            if row[1] == "C" or row[1] == "S":
                end_point = row[0] - start_point
                key_results.append(end_point)
        result.append(sum(key_results))
    return result


def print_result(array: List[int]):
    string = " ".join(map(str, array))
    print(string)


if __name__ == "__main__":
    lists_client_log = reading_input()
    result = sum_clien_time_in_log(lists_client_log)
    print_result(result)
