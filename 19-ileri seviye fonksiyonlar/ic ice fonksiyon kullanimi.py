# encapsulation islemi => 
def outer(num1):
    print("outer")
    def innerIncrement(num1):
        print("inner")
        return num1 + 1
    num2=innerIncrement(num1)
    print(num1,num2)

outer(10)


print("--------------------------------------------")

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("Number must be integer.")
    
    if not number>=0:
        raise ValueError("Number must be zero or positive.")
    
    def innerFactorial(number):
        if(number<=1):
            return 1
        return number*innerFactorial(number-1)
    return innerFactorial(number)

try:
    sayi = int(input("Bir sayi giriniz: "))
    result = factorial(sayi)
    print("Islem sonucu: ", result)
except Exception as e:
    print(f"Invalid input: {e}")

print("--------------------------------------------")