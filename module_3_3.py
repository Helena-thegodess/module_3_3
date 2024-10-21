def print_params(a = 1, b = "строка", c = True):
    print(a, b, c)
values_list = [52, "Python", False]
values_dict = {"a": 69, "b": "World", "c": [2, 7]}
values_list_2 = ["Lesson", 89]
print_params(b=25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
























