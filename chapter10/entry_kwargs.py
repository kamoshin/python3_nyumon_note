def entry(name, gender, **kwargs):
    data = {"name" : name, "gender" : gender}
    data.update(kwargs)
    print(data)

entry(name = "大阪坂道", gender = "男性", age = 27, course = "E")