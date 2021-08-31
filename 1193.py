
def findNum():
    n = int(input(""))
    count = 0
    sum = 0 
    while True:
        sum = sum + count 
        if n <= sum:
            return count, sum-n 
        count = count + 1 

def result():
    count,n = findNum()
    if count%2 == 0 :
        print(f"{count-n}/{1+n}")
    else:
        print(f"{1+n}/{count-n}")

result()



