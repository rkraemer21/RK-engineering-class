target = input("""What file would you like to open?
>>""")

print(" ")

txt = open(target)
print(txt.read())

txt.close()
