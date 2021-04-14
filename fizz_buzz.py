def fizz_buzz(n):
    for i in range(1,101):
        if i % 3 == 0 and not i%5 == 0:
            print('Fizz')
        print(i)
        
        pass #end of for loop


    pass


if __name__ == "__main__":
    fizz_buzz(100)
