#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        if (result):
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: None".format(result))
            return None
    return result
