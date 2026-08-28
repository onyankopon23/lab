import sys


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class AgeGroup:
    def __init__(self, min_age, max_age):
        self.min_age = min_age
        self.max_age = max_age
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def sort_people(self):
        self.people.sort(key=lambda person: person.name)
        self.people.sort(key=lambda person: person.age, reverse=True)

    def get_group_name(self):
        if self.max_age == 123:
            return str(self.min_age) + "+"
        return str(self.min_age) + "-" + str(self.max_age)


def create_groups(borders):
    groups = []
    first_group = AgeGroup(0, borders[0])
    groups.append(first_group)

    for i in range(1, len(borders)):
        min_age = borders[i - 1] + 1
        max_age = borders[i]
        group = AgeGroup(min_age, max_age)
        groups.append(group)

    last_group = AgeGroup(borders[-1] + 1, 123)
    groups.append(last_group)

    return groups


def read_people():
    people = []
    while True:
        line = input()
        if line == "END":
            break

        parts = line.split(",")
        name = parts[0]
        age = int(parts[1])
        person = Person(name, age)
        people.append(person)

    return people


def add_people(groups, people):
    for person in people:
        for group in groups:
            if group.min_age <= person.age <= group.max_age:
                group.add_person(person)
                break


def print_groups(groups):
    for group in reversed(groups):
        if len(group.people) == 0:
            continue

        group.sort_people()

        print(group.get_group_name() + ":")
        for person in group.people:
            print(person.name + "," + str(person.age))


def main():
    borders = []
    for arg in sys.argv[1:]:
        borders.append(int(arg))

    groups = create_groups(borders)
    people = read_people()
    add_people(groups, people)
    print_groups(groups)


if __name__ == "__main__":
    main()

