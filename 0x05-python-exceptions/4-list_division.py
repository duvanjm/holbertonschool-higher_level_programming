#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            new.append(my_list_1[i] / my_list_2[i])
            error = ""
        except TypeError:
            new.append(0)
            error = "wrong type"
        except ZeroDivisionError:
            new.append(0)
            error = "division by 0"
        except IndexError:
            new.append(0)
            error = "out of range"
        finally:
            if error == "":
                print(error, end="")
            else:
                print(error)
    return new
