from operator import itemgetter

def person_lister(f):
    def inner(people):
        for person in sorted(people, key=itemgetter(2)):
            yield f(person)
    return inner


def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for _ in range(int(input()))]
    print(*person_lister(name_format)(people), sep='\n')