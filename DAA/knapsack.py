#program related to index:
def knapsack(wt, profit, cap):
    items=[(i, wt[i], profit[i], wt[i]/profit[i] )for i in range(len(wt))]
    items.sort(key=lambda x:x[0], reverse =True)
    # items.sort(key=lambda x:x[1]) for smallest weight
    # items.sort(key=lambda x:x[2], reverse =True ) for largest profit
    # items.sort(key=lambda x:x[2], reverse =True ) for largest wt/profit ratio

    total_profit =0
    include_items = []

    for i, wt, profit, ratio in items:
        if cap>=wt:
            include_items.append((i, 1))
            total_profit = total_profit + profit
            cap = cap - wt

        else:
            frac = cap/wt
            total_profit = total_profit + (frac*profit)
            include_items.append((i, frac))
        
    return total_profit , include_items

wt = [30,20,10]
profit = [60, 50,40]
cap = 50

total_profit, include_items = knapsack(wt, profit, cap)

print("\t\ntotal profit is: " , total_profit)
print("include items are : " , include_items)