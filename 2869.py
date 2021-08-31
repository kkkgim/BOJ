a,b,v=map(int,input().split())

v = v - a 
share = v//(a-b)

if v/(a-b) - share  > 0:
    print(share+2)
else:
    print(share+1)