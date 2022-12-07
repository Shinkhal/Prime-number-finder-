x=eval(input("enter a number : "))
prime=True
for i in range(2,x):
    if x%i==0:
        prime=False
if prime ==True:
    print("prime")
else:
    print("not a prime")
