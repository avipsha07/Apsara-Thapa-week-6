import csv

def collect_employees(filename="employees.csv"):
    fieldnames = ["Name", "Department", "Salary"]
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            name = input("Enter employee Name (or type 'stop' to finish): ").strip()
            if name.lower() == "stop":
                break
            dept = input("Enter Department: ").strip()
            salary_input = input("Enter Salary: ").strip()
            try:
                salary = float(salary_input)  # allow decimals
            except ValueError:
                print("Invalid salary. Please enter a number. Try again for this employee.")
                continue

            employee = {"Name": name, "Department": dept, "Salary": salary}
            writer.writerow(employee)
            print(f"Saved {name}.\n")

    print(f"All entries saved to {filename}.")

def main():
    collect_employees()

if _name_ == "_main_":
    main()
