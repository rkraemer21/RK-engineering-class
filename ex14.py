from sys import argv

script, username = argv
prompt = '>'

print(f"Hi, {username}, I'm the {script} script.\nI'd like to ask you a few questions.")
print(f"Do you like me, {username}?")
likes = input(prompt)

if(likes == 'yes'): 
    print("Yay!")
if(likes == 'no'): 
    print("Darn.")

print(f"Where do you live, {username}?")
lives = input(prompt)
print("Interesting...")

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. I will remember that.
And you have a {computer} computer. Nice.
""")


