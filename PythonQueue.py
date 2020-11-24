
#list of names
names = []

#loop to enter 10 names into queue
for x in range(10):
    n = input("Please enter a name: ")
    names.append(n)
    print(n, "has been entered into the queue.\n")

#loop to remove names from queue
for x in range(10):
    n = names[0]
    print(n, "has exited the queue.")
    names.pop(0)
