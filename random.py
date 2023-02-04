import random

def generate_message():
    message_number = random.randint(1, 3)
    if message_number == 1:
        return "Today will be a lucky day"
    elif message_number == 2:
        return "You will meet someone new and interesting"
    else:
        return "Watch out for obstacles in your path"

print(generate_message())