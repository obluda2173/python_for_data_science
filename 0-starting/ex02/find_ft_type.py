def all_thing_is_obj(object: any) -> int:
    names = {list : "List",
             tuple : "Tuple",
             set : "Set",
             dict : "Dict"}
    obj_type = type(object)
    if (obj_type in names):
        print(f"{names[obj_type]} : {obj_type}")
    elif (obj_type == str):
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")
    return 42
