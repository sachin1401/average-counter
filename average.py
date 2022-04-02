term = int(input('How many number you want: '))
sum=0

for n in range(term):
    numbers=float(input("enter the number of sum you want? "))
    sum+=numbers

avg=sum/term

print(avg)