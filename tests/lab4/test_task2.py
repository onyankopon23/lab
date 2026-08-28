import unittest

from src.lab4.task2 import Person, AgeGroup, create_groups, add_people


class AgeGroupTestCase(unittest.TestCase):
    def test_add_person(self):
        group = AgeGroup(19, 25)
        person = Person("Иванов Иван", 20)
        group.add_person(person)
        self.assertEqual(group.people[0].name, "Иванов Иван")
        self.assertEqual(group.people[0].age, 20)

    def test_group_name(self):
        group = AgeGroup(19, 25)
        self.assertEqual(group.get_group_name(), "19-25")

    def test_last_group_name(self):
        group = AgeGroup(101, 123)
        self.assertEqual(group.get_group_name(), "101+")

    def test_create_groups(self):
        borders = [18, 25, 35]
        groups = create_groups(borders)
        self.assertEqual(groups[0].min_age, 0)
        self.assertEqual(groups[0].max_age, 18)
        self.assertEqual(groups[1].min_age, 19)
        self.assertEqual(groups[1].max_age, 25)
        self.assertEqual(groups[2].min_age, 26)
        self.assertEqual(groups[2].max_age, 35)
        self.assertEqual(groups[3].min_age, 36)
        self.assertEqual(groups[3].max_age, 123)

    def test_add_people(self):
        groups = create_groups([18, 25, 35])
        people = [
            Person("Иванов Иван", 20),
            Person("Роналдова Кристина", 41),
            Person("Хушетский Хасбулла", 17)
        ]
        add_people(groups, people)
        self.assertEqual(groups[0].people[0].name, "Хушетский Хасбулла")
        self.assertEqual(groups[1].people[0].name, "Иванов Иван")
        self.assertEqual(groups[3].people[0].name, "Роналдова Кристина")

    def test_sort_age(self):
        group = AgeGroup(19, 25)
        group.add_person(Person("Иванов Иван", 20))
        group.add_person(Person("Сульянов Аркадий", 25))
        group.add_person(Person("Ламинов Ямаль", 19))
        group.sort_people()
        self.assertEqual(group.people[0].age, 25)
        self.assertEqual(group.people[1].age, 20)
        self.assertEqual(group.people[2].age, 19)

    def test_sort_name(self):
        group = AgeGroup(19, 25)
        group.add_person(Person("Иванов Иван", 20))
        group.add_person(Person("Фет Афанасий", 20))
        group.add_person(Person("Акинфеев Игорь", 20))
        group.sort_people()
        self.assertEqual(group.people[0].name, "Акинфеев Игорь")
        self.assertEqual(group.people[1].name, "Иванов Иван")
        self.assertEqual(group.people[2].name, "Фет Афанасий")

