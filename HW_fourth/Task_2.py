def write_array(array, file_name):
    list = '/n'.join(array)
    with open("file_name", "w") as file:
        file.write(list)
    pass
