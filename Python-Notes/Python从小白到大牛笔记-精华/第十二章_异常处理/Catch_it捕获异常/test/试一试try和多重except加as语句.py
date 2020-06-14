n = 100
try:
    print(100 / 'QQQ')
except TypeError as te:
    print("TypeError!")
    print(te)
except ValueError as ve:
    print("ValueError!")
    print(ve)
