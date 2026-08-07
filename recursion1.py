def recursion_print(i,n):
    if i>n:
        return


    print(i)
    recursion_print(i+1,n)

recursion_print(1,5)