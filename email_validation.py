from string import ascii_lowercase, ascii_uppercase

username = list(ascii_lowercase+ascii_uppercase) + [str(value) for value in range(10)] + ['_', '-']
website = username[:-2]
extension = website[:-10]

def filtering(some_string: str, some_list: list) -> str:
    return ''.join(list(filter(lambda x: x in some_string, some_list)))

def fun(s):
    if list(s).count('@') != 1 or s[0] == '@':
        return False
    user, rest = s.split('@')
    if '.' not in rest[-4:]:
        return False
    web, ext = rest.split('.')
    f_user, f_web, f_ext = filtering(username, user), filtering(website, web), filtering(extension, ext)
    return True if f_user == user and f_web == web and f_ext == ext and len(ext) <= 3 else False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)