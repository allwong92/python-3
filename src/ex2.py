
def find_total_visits():
    count = 0
    with open("./files/week-1.csv", "r") as week1_file:
        next(week1_file)
        for row in week1_file:
            line = row.strip().split(",")
            for day in line:
                if day.strip().isdigit():
                    count += int(day.strip())
        
    with open("./files/week-2.csv", "r") as week2_file:
        next(week2_file)
        for row in week2_file:
            line = row.strip().split(",")
            for day in line:
                if day.strip().isdigit():
                    count += int(day.strip())

    with open("./files/week-3.csv", "r") as week3_file:
        next(week3_file)
        for row in week3_file:
            line = row.strip().split(",")
            for day in line:
                if day.strip().isdigit():
                    count += int(day.strip())

    return count

def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()