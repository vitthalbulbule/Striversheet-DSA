def recursion_print(i,n):
    if i>n:

        return

    fact = 0
    fact=fact*i


    print(fact)
    recursion_print(i+1,n)

recursion_print(1,5)