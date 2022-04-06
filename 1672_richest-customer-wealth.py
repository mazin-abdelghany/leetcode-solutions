def maximumWealth(accounts):
    wealth = []
    for i in range(len(accounts)):
        wealth.append(sum(accounts[i]))
    return max(wealth)

print(maximumWealth([[1,5],[7,3],[3,5]]))