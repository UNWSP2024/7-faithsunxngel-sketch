# Program #3: US_Population
# Program #3: US_Population

def main():
    all_entered_values = []

    print("Enter population data for each state.")
    print("When you are done entering data, type 'done' for the state name.\n")

    while True:
        year = input("Enter year (e.g., 2010): ")
        if not year.isdigit():
            print("Please enter a valid year (numbers only).")
            continue
        year = int(year)

        state = input("Enter state name (or 'done' to finish): ")
        if state.lower() == 'done':
            break

        population = input(f"Enter population for {state} in {year}: ")
        if not population.isdigit():
            print("Please enter a valid population number.")
            continue
        population = int(population)

        all_entered_values.append([year, state, population])

    year_to_sum = int(input("\nEnter a year to calculate total population for: "))

    sum_population_for_year(all_entered_values, year_to_sum)


def sum_population_for_year(all_entered_values, year_to_sum):
    total_population = 0

    for record in all_entered_values:
        year, state, population = record
        if year == year_to_sum:
            total_population += population

    print(f"\nTotal population for the year {year_to_sum}: {total_population}")


if __name__ == '__main__':
    main()
