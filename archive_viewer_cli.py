import os

help_guide = print("Remember that when selected an office it will be its initials lowercase. ")

#User input for Office and year
office = input("Which paper will you like to view")
searchyear = input("Search for year in this format yyyymmdd")

#directories
dir = ("//", "//", "//", 
"//", "//", "//")



def l_view():

    lnjdirpath =(os.path.join(dir[0], searchyear))

    os.chdir(lnjdirpath)



    # Shows the pdfs of the directory the user inputed (the date)
    for dirpath, dirnames, files in os.walk(lnjdirpath):
        print(f'Found directory: {dirpath}')
        for file_name in files:
            print(file_name)


    # PDF User Input
    pdfinput = input("Which pdf will you like to open? ")

    # Opens selected pdf
    os.startfile(pdfinput)

def m_view():
    mnmdirpath =(os.path.join(dir[1], searchyear))

    os.chdir(mnmdirpath)
    


    # Shows the pdfs of the directory the user inputed (the date)
    for dirpath, dirnames, files in os.walk(mnmdirpath):
        print(f'Found directory: {dirpath}')
        for file_name in files:
            print(file_name)


    # PDF User Input
    pdfinput = input("Which pdf will you like to open? ")

    # Opens selected pdf
    os.startfile(pdfinput)

def t_view():
    tmtdirpath =(os.path.join(dir[2], searchyear))

    os.chdir(tmtdirpath)
    

    # Shows the pdfs of the directory the user inputed (the date)
    for dirpath, dirnames, files in os.walk(tmtdirpath):
        print(f'Found directory: {dirpath}')
        for file_name in files:
            print(file_name)


    # PDF User Input
    pdfinput = input("Which pdf will you like to open? ")

    # Opens selected pdf
    os.startfile(pdfinput)

def k_view():
    knhdirpath =(os.path.join(dir[3], searchyear))

    os.chdir(knhdirpath)
    


    # Shows the pdfs of the directory the user inputed (the date)
    for dirpath, dirnames, files in os.walk(knhdirpath):
        print(f'Found directory: {dirpath}')
        for file_name in files:
            print(file_name)


    # PDF User Input
    pdfinput = input("Which pdf will you like to open? ")

    # Opens selected pdf
    os.startfile(pdfinput)

def p_view():
    pwdirpath =(os.path.join(dir[4], searchyear))

    os.chdir(pwdirpath)
    


    # Shows the pdfs of the directory the user inputed (the date)
    for dirpath, dirnames, files in os.walk(pwdirpath):
        print(f'Found directory: {dirpath}')
        for file_name in files:
            print(file_name)


    # PDF User Input
    pdfinput = input("Which pdf will you like to open? ")

    # Opens selected pdf
    os.startfile(pdfinput)

def va_view():
    vadirpath =(os.path.join(dir[5], searchyear))

    os.chdir(vadirpath)
    


    # Shows the pdfs of the directory the user inputed (the date)
    for dirpath, dirnames, files in os.walk(vadirpath):
        print(f'Found directory: {dirpath}')
        for file_name in files:
            print(file_name)


    # PDF User Input
    pdfinput = input("Which pdf will you like to open? ")

    # Opens selected pdf
    os.startfile(pdfinput)


def office_search(office):
    match office:
        case "l":
            return l_view()
        case "m":
            return m_view()
        case "k":
            return k_view()
        case "t":
            return t_view()
        case "p":
            return p_view()
        case "va":
            return va_view()

office_search(office)