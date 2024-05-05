def calculate_average(*args):
    if not args:
        return None
    total = sum(args)
    count = len(args)
    average = total / count
    return average

if __name__ == "__main__":
    print("Среднее арифметическое:", calculate_average(40, 20, 30))