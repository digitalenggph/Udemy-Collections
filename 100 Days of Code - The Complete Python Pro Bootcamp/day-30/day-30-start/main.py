"""
DAY-30-NOTES:

# gets traceback error "No such file or directory"
with open("a_file.txt") as file:
    file.read()

# KeyError
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

# IndexError
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

# TypeError
text = "abc"
print(text + 5)

# try-except-else-finally
    * try       - something that might cause an exception
    * except    - do this if there was an exception
    * else      - do this if there were no exceptions
    * finally   - do this no matter what happens
"""

# FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["not a key"])
except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("Something")
    print(f"generated a_file.txt")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
