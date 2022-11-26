import string
from typing import Tuple, List


def reading_input() -> Tuple[int, List[str]]:
    count_numbers = int(input())
    result_array = []
    for i in range(count_numbers):
        string_array = list(map(str, input().split(" ")))
        result_array.append(string_array)
    return count_numbers, result_array


def string_to_hex(string_array: List[str]) -> List[str]:
    result = []
    for current_array in string_array:
        for raw_string in current_array:
            raw_list = raw_string.split(",")
            string_fullname = ""
            for row in raw_list[:3]:
                string_fullname += row
            sum_string_name = len(set(string_fullname))

            count_date = 0
            for numb in raw_list[3:5]:
                for current_numb in numb:
                    count_date += int(current_numb)

            first_symbol_numb = (
                string.ascii_letters.index(raw_string[:1].lower()) + 1
            )

            result_sum = hex(
                sum_string_name + count_date * 64 + first_symbol_numb * 256
            ).split("x")[-1]
            if len(result_sum) < 4:
                zero_string = "0" * (4 - len(result_sum))
                result_sum = zero_string + result_sum
            result.append(result_sum[1:].upper())
    return result


def print_result(array: List[str]):
    string = " ".join(map(str, array))
    print(string)


if __name__ == "__main__":
    coun_str, array_str = reading_input()
    result = string_to_hex(array_str)
    print_result(result)
