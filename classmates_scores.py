import csv

def create_scores_csv(filename="class_scores.csv"):
    # Example data for 5 classmates, each with 3 subject scores
    students = [
        ("Aadiskar", 80, 60, 55),
        ("Bipin",    50, 80, 90),
        ("Muskan",   90, 28, 63),
        ("Sita",     75, 82, 68),
        ("Ram",      64, 70, 72),
    ]
  
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "subject1", "subject2", "subject3"])
        writer.writerows(students)
    return filename

def print_averages(filename="class_scores.csv"):
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            scores = [int(row["subject1"]), int(row["subject2"]), int(row["subject3"])]
            avg = sum(scores) / len(scores)
            print(f"{name}'s average score is {avg:.2f}.")

def main():
    file = create_scores_csv()
    print_averages(file)

if _name_ == "_main_":
    main()
