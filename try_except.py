def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError as zde: # Exceptions are classes
        print("Division failed: " + str(zde))
        # print(zde.__str__()) # str(zde) is equivalent to zde.__str__() 
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2))
print(reciprocal(0))
