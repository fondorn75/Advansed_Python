import time


class MyString:
    def __new__(cls, value, author):
        instance = super().__new__(cls)
        instance.value = value
        instance.author = author
        instance.time = time.time()
        return instance


if __name__ == '__main__':
    s = MyString('kvskvs', 'Ru')
    print(s.time)
    print(s.value)
    print(s.author)
