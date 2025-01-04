def count_substring(str: str, sub_str: str) -> int:
    return sum(1 for i in range(len(str)-len(sub_str)+1) if str[i:len(sub_str)+i] == sub_str)

if __name__ == '__main__':
    string, sub_string = input('String substring:').split()
    count = count_substring(string, sub_string)
    print(f'The "{sub_string}" substring in "{string}" string appears "{count}" time(s)')