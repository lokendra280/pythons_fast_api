my_dict = {"name": "Lokendra", "age": 20, "address": "Kathmandu"}
# print(my_dict)

my_dict_2 = dict({"name": "Dick", "age": 25})
# print(my_dict["address"])

my_dict["address"]= "india"
my_dict.update({"gender": "Male"})
# 

for key, value  in my_dict.items():
    print(key, value)