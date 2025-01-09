from string import ascii_lowercase, ascii_uppercase, digits

username = ascii_lowercase+ascii_uppercase+digits+'_-'
website = username[:-2]
extension = website[:-10]

def filtering(valid_chars: str, unexamined_string: str) -> str:
    return ''.join(list(filter(lambda x: x in valid_chars, unexamined_string)))

def fun(s: str) -> bool:
    if s.count('@') != 1 or s[0] == '@':
        return False
    user, rest = s.split('@')
    if '.' not in rest[-4:]:
        return False
    web, ext = rest.split('.')
    return filtering(username, user) == user and filtering(website, web) == web and filtering(extension, ext) == ext and len(ext) <= 3
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = [input() for _ in range(n)]

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)