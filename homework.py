import openpyxl

dictionary = {}
collection = []
fileInput = "students.txt"
fileOutput_without_scholarship = "without_scholarship.txt"
fileOutput_up_scholarship = "up_scholarship.txt"
fileOutput_Csv = "students.csv"

with open(fileInput, "r", encoding="utf8") as file:
    for line in file:
        a = line.split("-")
        a[1] = a[1][1]
        dictionary[a[0]] = a[1]


def solve_txt():
    with open(fileOutput_without_scholarship, "w") as file:
        for key in dictionary:
            if int(dictionary[key]) <= 3:
                file.write(key + "\n")

    with open(fileOutput_up_scholarship, "w") as file:
        for key in dictionary:
            if int(dictionary[key]) == 5:
                file.write(key + "\n")


def solve_csv():
    for key in dictionary:
        a = key.split(" ")
        localColl = [a[0], a[1], dictionary[key]]
        collection.append(localColl)

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["Фамилия", "Имя", "Оценка"])
    for elem in collection:
        sheet.append([elem[0], elem[1], elem[2]])
    workbook.save(fileOutput_Csv)
    workbook.close()


solve_txt()
solve_csv()

