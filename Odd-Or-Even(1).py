def odd_or_even():
    n = int(input("What number are you thinking? "))
    if n % 2 ==0 :
        print("That's an even number!", "Have another? ")
    else:
        print("That's an odd number!", "Have another? ")
        
print(odd_or_even())
