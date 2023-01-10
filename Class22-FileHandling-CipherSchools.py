# Text files

  # Opening a file
file = open("random.txt","w")
file.write("blah blah blah")

file.write("\n new line")

file.close()

  # Writing to a file
    # write
    # writelines

file = open("random.txt","w")
file.write("jatin katyal")
a = ["jatin", "samarth", "sujith", "saranah"]
file.writelines(a)
file.close()

  # Reading from a file
    # read
    # readline
    # readlines

file = open("sample.txt","r")
file.read()
print(file.read())

# STREAMS
  # Iterables which can iterated in single direction
  # They don't have starting and ending point


  # Context Programming
with open("random.txt", "r") as file:
    print(file.read())

class A:
    def __enter__(self):
        print("Entered")
        return 1
    def __exit__(self, *args):
        print("Exitted")
        print(args)
        return True

with A() as x:
    print(x)
    print("inside context")
    raise Exception

print("outside context")

# JSON rule
  # keys can only be strings and numbers
  # values can only be array,json,strings,numbers,boolean,null

a = {
    "name": "Jatin Katiyal",
    "marks": 100,
    "languages": {
        "c++",
        "python",
        "go",
        "rust"
    }
}

import json
s = json.dumps(a)
type(a)
print(s)