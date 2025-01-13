from string import ascii_lowercase as lowers,  ascii_uppercase as uppers, digits

username_chars, website_chars, extension_chars  = lowers+uppers+digits+'_-', lowers+uppers+digits, lowers+uppers

def validate(valid_chars: str, unexamined_string: str) -> str:
    return ''.join(list(filter(lambda x: x in valid_chars, unexamined_string)))

def fun(s: str) -> bool:
    if s.count('@') != 1 or s[0] == '@':
        return False
    user, rest = s.split('@')
    if '.' not in rest[-4:]:
        return False
    web, ext = rest.split('.')
    conds = validate(username_chars, user) == user, validate(website_chars, web) == web, validate(extension_chars, ext) == ext
    return len(ext) <= 3 and all(conds)

def filter_mail(emails: list) -> list:
    return list(filter(fun, emails))

if __name__ == '__main__':
    emails = [input() for _ in range(int(input()))]
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)