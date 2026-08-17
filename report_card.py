def header(name, classe):
    print("-"*40)
    print("REPORT CARD".center(40))
    print("-"*40)
    print(f"Student: {name}".ljust(30), end= "")
    print(f"Class: {classe}º".rjust(10))
    print("-"*40)

def media(n1, n2):
    return (n1 + n2) / 2


subjects = [{"Subject":"Mathematics"}, 
            {"Subject":"English"}, 
            {"Subject":"Science"}, 
            {"Subject":"History"}, 
            {"Subject":"Geography"}, 
            {"Subject":"Arts"}, 
            {"Subject":"PE"}]

studentName = input("Student's name: ").strip().upper()
studentClass = int(input("Class: "))

for item in subjects:
    item["Grade1"] = float(input(f"Grade 1 for '{item["Subject"]}': "))
    item["Grade2"] = float(input(f"Grade 2: "))
    item["Media"] = media(item["Grade1"], item["Grade2"])
    if item["Media"] >= 6:
        item["Situation"] = "Pass"
    else:
        item["Situation"] = "Failed"

header(studentName, studentClass)

for subj in subjects:
    print(f"{subj["Subject"]}".ljust(20), end= "")
    print(f"{subj["Media"]:.1f}", end= "")
    print(f"{subj["Situation"]}".rjust(17))
print("-"*40)
