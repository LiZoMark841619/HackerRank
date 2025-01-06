from string import ascii_lowercase as chars

def is_pangram(string_: str) -> bool:
    return ''.join(sorted(set(filter(lambda x: x in chars, string_.lower())))) == chars
print(is_pangram('The quick brown fox jumps over the lazy dog.'))