def stockSpan(price,stock):
    n = len(price)
    l = []
    l.append(0)
    stock[0] = "null"
    for i in range(1 , n):
        while len(l) > 0 and price[l[-1]] <= price[i]:
            l.pop()
        
        stock[i] = i + 1 if len(l) <= 0 else (i - l[-1]) 
        l.append(i)

def display(arr,n):
    for i in range(n):
        print(arr[i],end=' ')

daily_price = []
l=int(input("Enter number of days : "))
for i in range(l):
    ele=int(input("Enter daily stock value : "))
    daily_price.append(ele)
stock = [0 for i in range(len(daily_price)+1)] 
  
stockSpan(daily_price, stock) 
display(stock, len(daily_price))