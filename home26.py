import json
import requests

def get_definitions(word):
    definitions = ""
    counter = 1
    url = f"http://api.urbandictionary.com/v0/define?term={word}"
    result = requests.get(url).json()
    for i in result["list"]:
        data = i["definition"].replace("[", "").replace("]", "")\
            .replace("\n", "").title()
        definitions = f'{definitions}\n{counter}. {data}'
        counter += 1
    return definitions.strip()

print(get_definitions("spare parts"))


#Hash function

class Hashing:
    def __init__(self, table_length=10):
        self.hash_table = [[] for _ in range(table_length)]

    def hash_function(self, key):
        if isinstance(key, int):
            return key % len(self.hash_table)
        else:
            return len(key) % len(self.hash_table)

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        is_in_table = False
        bucket = self.hash_table[hash_key]
        for a, b in enumerate(bucket):
            c, d = b
            if key == c:
                is_in_table = True
                break
        if is_in_table:
            bucket[a] = ((key, value))
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = self.hash_function(key)
        bucket = self.hash_table[hash_key]
        for a, b in enumerate(bucket):
            c, d = b
            if key == c:
                return d
        return "Not found"

    def delete(self, key):
        hash_key = self.hash_function(key)
        bucket = self.hash_table[hash_key]
        for a, b in enumerate(bucket):
            c, d = b
            if key == c:
                print(f"{bucket[a][1]} deleted")
                del bucket[a]
                return
        return "Not found"


table1 = Hashing()
table1.insert(10, "Steve")
table1.insert(20, "Mike")
table1.insert("40", "Peter")
print(table1.hash_table)

print(table1.search(20))
print(table1.search("40"))
table1.delete("40")
print(table1.hash_table)
