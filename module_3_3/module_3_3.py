def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params()
print_params(2)
print_params(2, "строка")
print_params(2, "строка", False)
print_params(c=False, a=2, b="строка")
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, True, "test"]

values_dict = {"a": 1, "c": True, "b": "test"}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, "test"]

print_params(*values_list_2, 42)
