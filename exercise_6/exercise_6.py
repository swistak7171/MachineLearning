def separate(number: int):
    print(f"------------------------ {number} ------------------------ ")


readonly_file = open('szustak_21172.txt')
print(type(readonly_file))
readonly_file.close()

readwrite_file = open('szustak_21172.txt', 'rb')
print(type(readwrite_file))
readwrite_file.close()

separate(1)
with open('szustak_21172.txt') as reader:
    print(reader.read())

separate(2)
with open('szustak_21172.txt') as reader:
    print(reader.readline(7))

separate(3)
with open('szustak_21172.txt') as reader:
    print(reader.readlines())
file_3 = open('szustak_21172.txt')
print(list(file_3))
file_3.close()

separate(4)
with open('szustak_21172.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        print(line, end='')
        line = reader.readline()

print()

with open('szustak_21172.txt') as reader:
    for line in reader.readlines():
        print(line, end='')

print()

with open('szustak_21172.txt', 'r') as reader:
    for line in reader:
        print(line, end='')

print()

separate(5)
with open('szustak_21172.txt', 'r') as reader:
    lines = reader.readlines()

with open('szustak_21172_reversed.txt', 'w') as writer:
    for line in reversed(lines):
        writer.write(line)

separate(6)
with open('szustak_21172_corgies.jpg', 'rb') as reader:
    print(reader.read(1))
    print(reader.read(3))
    print(reader.read(2))
    print(reader.read(1))
    print(reader.read(1))

separate(7)
print(__file__)

separate(8)
with open('szustak_21172_append.txt', 'a') as writer:
    writer.write('Appended new line\n')

separate(9)
with open('szustak_21172_corgies.jpg', 'rb') as reader, open('szustak_21172_corgies_copy.jpg', 'wb') as writer:
    lines = reader.readlines()
    writer.writelines(lines)


class FileReader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        print('ENTER')
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT')
        self.__file_object.close()


separate(10)
with FileReader('szustak_21172.txt') as reader:
    pass


class PngReader():
    _expected_magic = b'\x89PNG\r\n\x1a\n'

    def __init__(self, file_path):
        if not file_path.endswith('.png'):
            raise NameError("File must be a '.png' extension")
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path, 'rb')

        magic = self.__file_object.read(8)
        if magic != self._expected_magic:
            raise TypeError("The File is not a properly formatted .png file!")

        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    def __iter__(self):
        return self

    def __next__(self):
        initial_data = self.__file_object.read(4)

        if self.__file_object is None or initial_data == b'':
            raise StopIteration
        else:
            chunk_len = int.from_bytes(initial_data, byteorder='big')
            chunk_type = self.__file_object.read(4)
            chunk_data = self.__file_object.read(chunk_len)
            chunk_crc = self.__file_object.read(4)
            return chunk_len, chunk_type, chunk_data, chunk_crc


separate(11)
with PngReader('szustak_21172_corgies.png') as reader:
    for l, t, d, c in reader:
        print(f"{l:05}, {t}, {c}")