tuition = 10000
yearlyIncrease = .05
fourYearCost = 0

for i in range(10):
    tuition += (tuition * yearlyIncrease) 

print("Tuition in 10 years: $", tuition)

for i in range(1, 5):
    fourYearCost += tuition
    tuition += (tuition * yearlyIncrease)

print("Total tuition : $", fourYearCost)