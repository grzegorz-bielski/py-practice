import re

string_to_match = "'I said' - that's what she said."
some_string = re.sub('[A-Z]', '', string_to_match)
print(some_string)

ayy = "Hello:World"
world = ayy.split(":")[1]
print(world)


def bubble_sort(old_list):
    nlist = list(old_list)
    for numbers in range(len(nlist)-1, 0, -1):
        for i in range(numbers):
            if nlist[i] > nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    return nlist


sorted = bubble_sort([23, 34, 645, 3, 3, 22, 243, 11, 23, 53453])
print(sorted)


def map_to_dict(people, things):
    mapped = {}
    for index, person in enumerate(people):
        mapped[person] = things[index]
    return mapped


print(map_to_dict(["John", "Mary"], [34, 23]))


def make_comparisment(n): return lambda x: x == n


isFive = make_comparisment(5)
isSix = make_comparisment(6)

print(isFive(5), isFive(6), isSix(6))


def print_names(name="Someone", age=0):
    print("Name: ", name, "Age: ", age)


def greet_all(*people):
    for person in people:
        print("Hello ", person)


print_names()
print_names(age=27)
greet_all("Ayy", "Lmao", "The Third")

isChecked = 'yes' if True else 'true'

print(isChecked)
