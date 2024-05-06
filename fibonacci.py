def get_fibonacci_series(num):
    if num<=0:
        print("Invalid input number. The number must be a positive integer")
        return None
    
    fibonacci_series = [0, 1]
    for i in range(num-2):
        next_item = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_item)
    return fibonacci_series
