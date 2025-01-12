from string import ascii_lowercase as chars

def is_pangram_one(string_: str) -> bool:
    return ''.join(sorted(set(filter(lambda x: x in chars, string_.lower())))) == chars

def is_pangram_two(string_: str) -> bool:
    return ''.join(sorted({c for c in string_ if c in chars})) == chars

def is_pangram_three(string_: str) -> bool:
    return set(chars).issubset(set(string_.lower()))

def is_pangram_four(st: str) -> bool:  # sourcery skip: invert-any-all, use-any, use-next
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if not st.lower().count(char):
            return False
    return True

test = 'The quick brown fox jumps over the lazy dog.'
print(is_pangram_one(test)) # True
print(is_pangram_two(test)) # True
print(is_pangram_three(test)) # True
print(is_pangram_four(test)) # True


