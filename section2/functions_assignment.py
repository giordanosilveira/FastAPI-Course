def make_dict(first_name, last_name, age):
    person = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
    }
    return person

person = make_dict("John", "Doe", 30)
print(person)