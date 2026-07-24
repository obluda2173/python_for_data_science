ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# list
ft_list[1] = "World!"

# tuple
ft_tuple_list = list(ft_tuple)
ft_tuple_list[1] = "Austria!"
ft_tuple = tuple(ft_tuple_list)

# set
ft_set.discard("tutu!")
ft_set.add("Vienna!")

# dictionary
ft_dict["Hello"] = "42Vienna!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
