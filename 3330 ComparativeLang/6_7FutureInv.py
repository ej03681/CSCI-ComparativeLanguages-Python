def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    monthlyInterest = monthlyInterestRate / 100 / 12
    numberOfMonths = years * 12
    futureInvestment = investmentAmount * (1 + monthlyInterest) ** numberOfMonths 

    return futureInvestment

def main():
    principle = (float(input("Enter an investment amount: ")))
    interest = (float(input("Enter interest rate: " )))
    
    for i in range(1, 31):
        print(i, " ", round(futureInvestmentValue(principle, interest, i), 2))
        
main()