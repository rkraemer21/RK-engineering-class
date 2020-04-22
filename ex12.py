age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} years old, {height} tall, and {weight} heavy.")

formatter = "So, you're {} years old, {} tall, and {} heavy."
print(formatter.format(age, height, weight))
