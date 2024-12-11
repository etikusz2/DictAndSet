animals = {
    "lion" : ["scary", "big", "cat"],
    "elephant" : ["big", "gray", "wrinkled"],
    "teddy" : ["cuddly", "stuffed"]
}

# things = animals
things = animals.copy()
animals["teddy"] = "toy"
print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])