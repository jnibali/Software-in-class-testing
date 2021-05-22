val = int(input("Input - "))
if (val % 4) == 0:
    if (val % 100) == 0:
        if(val % 400) == 0:
            print("Output - ", val, "is a leap year")
        else:
             print("Output - ", val, "is not a leap year")
    else:
        print("Output - ", val, "is a leap year")
else:
    print("Output - ", val, "is not a leap year")