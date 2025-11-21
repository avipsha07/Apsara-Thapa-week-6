from multiplication_module import multiplication_table

def ask_and_print_table():
    try:
        n = int(input("Enter the number to make multiplication table for: "))
        limit = int(input("Enter the limit (positive integer): "))
        if limit <= 0:
            print("Limit should be a positive integer.")
            return
    except ValueError:
        print("Please enter valid integers.")
        return

    table_lines = multiplication_table(n, limit)
    print(f"\nMultiplication table of {n} up to {limit}:")
    for line in table_lines:
        print(line)

def main():
    ask_and_print_table()

if _name_ == "_main_":
    main()
