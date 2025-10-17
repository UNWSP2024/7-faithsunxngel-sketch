# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

def main():
    rainfall_list = []
    for month in range(1, 12 + 1):
     rainfall = float(input(f"enter the rainfall (in inches) for month {month}: "))
    rainfall_list.append(rainfall)
    total_rainfall = sum(rainfall_list)
    average_rainfall = total_rainfall / 12
    highest_rainfall = max(rainfall_list)
    lowest_rainfall = min(rainfall_list)
    month_of_the_highest = rainfall_list.index(highest_rainfall) + 1
    month_of_the_lowest = rainfall_list.index(lowest_rainfall) + 1

    print("\n--- Rainfall Report ---")
    print(f"Total rainfall for the year: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Highest rainfall in month {month_of_the_highest}: {highest_rainfall:.2f} inches")
    print(f"Lowest rainfall in month {month_of_the_lowest}: {lowest_rainfall:.2f} inches")
 
if __name__ == '__main__':
    main() 