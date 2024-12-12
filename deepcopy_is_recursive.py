from simple_deepcopy import my_deepcopy
import copy

original = {
    "David" : ["Beckham", ["Former footballer", "Ambassador"]],
    "Ete" : ["Birtalan", ["Programmer", "Courier"]]
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["David"].append("Miami")
original["Ete"].append("Sepsi")

original["David"][1].append("Boss")
ete_list = original["Ete"]
ete_list[1].append("Mountain lover")

print(original)
print(copy_1)
print(copy_2)