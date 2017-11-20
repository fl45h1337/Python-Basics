with open("txt_files/countries-raw.txt","r") as file:
    content = file.readlines()

    content = [i.strip("\n") for i in content if "\n" in i]
    content = [i for i in content if i != ""]
    content = [i for i in content if i != "Top of Page"]
    content = [i for i in content if len(i) != 1]
    print(''.join(content))

with open("txt_files/countries-raw.txt","w") as file:
    for i in content:
        file.write(i+"\n")

# Checking if checklist items are in the file!

checklist = ["Portugal", "Germany", "Not This One", "Spain"]

with open("txt_files/countries-clean.txt", "r") as file:
    content = file.readlines()

content = [i.rstrip('\n') for i in content]
checked = [i for i in content if i in checklist]

country_names = ', '.join(checked)

print("The countries matched are : ", country_names)