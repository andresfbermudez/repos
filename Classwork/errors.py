def my_function():
    b = ['a','b']
    try:
        c = b[len(b)]
    except IndexError:
        c = b[len(b)-1]
    return c

def calc_sqrt(n):
    from calcie import sqrt
    answer = sqrt(n)        

def main():
    print(my_function())
    x = "4"
    try:
        a = calc_sqrt(x)
    except TypeError:
        new_x = int(x)
        a = calc_sqrt(new_x)
    except ValueError:
        print("You can't do negative")
        a = ""
    print(a)
if __name__ == "__main__":
    main()
