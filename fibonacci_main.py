import fibonacci

def main():
    number = int(input("Enter the length of the series 0-x: "))
    series = fibonacci.get_fibonacci_series(number)
    print(series)

main()