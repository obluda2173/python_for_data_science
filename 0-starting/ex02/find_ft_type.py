def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    obj_type_str = ""
    if (obj_type == list):
        obj_type_str = "List"
    elif (obj_type == tuple):
        obj_type_str = "Tuple"
    elif (obj_type == set):
        obj_type_str = "Set"
    elif (obj_type == dict):
        obj_type_str = "Dict"
    elif (obj_type == str):
         obj_type_str = f"{object} is in the kitchen"
    else:
        print("Type not found")
    if obj_type_str:
        print(f"{obj_type_str} : {type(object)}")
    return 42
