class MyDict(dict):
    def get(self, key):
        return super().get(key, 0)


my_dict = MyDict(a=1, b=2)
print(my_dict)
print(my_dict.get('m'))

# зачет!