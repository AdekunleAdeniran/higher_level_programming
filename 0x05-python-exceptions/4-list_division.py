#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for items in range(list_length):
        try:
            new_list.append(my_l_1[items] / my_l_2[items])
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass
        return new_list
