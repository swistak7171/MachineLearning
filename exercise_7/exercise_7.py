import json

data = {
    "animal": {
        "name": "cat",
        "legs": 4
    }
}

with open('data.json', 'w') as writer:
    json.dump(data, writer)

json_string = json.dumps(data)
print(json_string)
json_string = json.dumps(data, indent=4)
print(json_string)

with open('data.json', 'r') as reader:
    deserialized_data = json.load(reader)
    print(deserialized_data)

json_string = """
{
    "title": "Animals collection",
    "animals": [
        {
            "name": "cat",
            "legs": 4
        },
        {
            "name": "dog",
            "legs": 4
        },
        {
            "name": "parrot",
            "legs": 2
        }
    ],
    "number_of_animals": 3        
}
"""

data = json.loads(json_string)
print(data)


class Animal:
    def __init__(self, name: str, legs: int, is_fluffy: bool = False):
        self.name = name
        self.legs = legs
        self.is_fluffy = is_fluffy


try:
    dog = Animal("dog", 4, True)
    json.dumps(dog)
except Exception:
    print("Object is not serializable")

complex_object = 1 + 5j


def encode(object: complex):
    if isinstance(object, complex):
        return (object.real, object.imag)
    else:
        type_name = object.__class__.__name__
        print(f"Object of type {type_name} is not serializable")


complex_json = json.dumps(complex_object, default=encode)
print(complex_json)


class ComplexEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, complex):
            return (object.real, object.imag)
        else:
            return super().default(object)


complex_json = json.dumps(complex_object, cls=ComplexEncoder)
print(complex_json)


def decode(json):
    if '__complex__' in json:
        return complex(json['real'], json['imag'])
    return json

with open('complex.json', 'r') as reader:
    data = reader.read()
    complex_object = json.loads(data, object_hook=decode)
    print(complex_object)

with open('complex_numbers.json', 'r') as reader:
    data = reader.read()
    numbers = json.loads(data, object_hook=decode)
    print(numbers)