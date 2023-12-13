f = open("input.txt")
values = f.read().strip().splitlines()

def calculate(list):
    for income in list:
        match income:
            case <= 100000:
                return 0.044 * income
            case <= 200 000:
                return 4400 + 0.0385 * (income-100000)
            case <= 300 000:
                return 7700 + 0.0275 * (income-200000)
            case >= 300 000:
                return 8250 + 0.0165 * (income-300000)
