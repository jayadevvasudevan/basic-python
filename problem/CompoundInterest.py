# Function to calculate Compound Interest
def CI(principle, rate, time):
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    format_CI = "{:.2f}".format(CI)
    print("Compound interest is", format_CI)
    

# main() Function 
if __name__ == "__main__":
    CI(1000, 10, 3)