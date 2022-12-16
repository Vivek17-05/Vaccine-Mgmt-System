# VACCINE MANAGEMENT SYSTEM
# BINARY FILES AND UDF AND MENU DRIVEN
import pickle  # for pickle.load() , pickle.dump()
import os  # for os.remove() , os.rename()
import sys  # for sys.exit()
import csv
dict = {}

def write_data():
    file = open("Vaccine.dat", "ab")  # a-append , b-binary
    n = int(input("ENTER THE NUMBER OF PERSON TO BE VACCINATED : "))
    for i in range(n):
        print("ENTER THE DETAILS OF PERSON : ", i + 1)
        dict["AADHAR NUMBER"] = int(input("ENTER AADHAR NUMBER : "))
        dict["NAME"] = input("ENTER NAME : ")
        dict["AGE"] = int(input("ENTER AGE : "))
        dict["VACCINE TYPE"] = input("ENTER VACCINE TYPE : ")
        dict['DOSE NUMBER'] = int(input('ENTER NUMBER OF DOSES ADMINISTERED : '))
        dict['STATUS'] = input('ENTER VACCINATION STATUS : ')
        pickle.dump(dict, file)  # dump is used to write in a file
    file.close()
    d=[]
    f = open('Vaccine.dat','rb')
    try :
        while True :
            e = pickle.load(f)
            s = e.values()
            d = d + [s,]
    except EOFError :
        f.close()
    l = ['AADHAR NUMBER','NAME','AGE','VACCINE TYPE','DOSE NUMBER','STATUS']
    fl = open('Vaccine.csv','w')
    w = csv.writer(fl)
    w.writerow(l)
    w.writerows(d)
    fl.close()

def display():
    file = open("Vaccine.dat", "rb")  # r-read , b-binary
    try:
        while True:
            vac = pickle.load(file)  # load is used to read
            print(vac)
    except EOFError:
        pass
    file.close()

def search():
    file = open("Vaccine.dat", "rb")  # r-read , b-binary
    a = int(input("ENTER AADHAR NUMBER TO BE SEARCHED : "))
    found = 0
    try:
        while True:
            vac = pickle.load(file)  # load is used to read
            if vac["AADHAR NUMBER"] == a:
                found = 1
                print("RECORD FOUND.")
                print(vac)
                break
    except EOFError:
        pass
    if found == 0:
        print("RECORD NOT FOUND.")
    file.close()

def update():
    file = open("Vaccine.dat", "rb")  # r-read , b-binary
    try :
        while True :
            d = pickle.load(file)
    except EOFError :
        file.close()
    file = open("Vaccine.dat", "rb")    
    f = open("temp.dat", "ab")
    r = int(input("ENTER AADHAR NUMBER TO BE UPDATED : "))
    try:
        while True:
            vac = pickle.load(file)  # load is used to read
            if vac["AADHAR NUMBER"] == r:
                print("ENTER NEW DETAILS : ")
                vac['NAME']=input("ENTER NAME : ")
                vac['AGE']=input("ENTER AGE : ")
                vac['VACCINE TYPE']=input("ENTER VACCINE TYPE : ")
                vac["DOSE NUMBER"] = input("ENTER NUMBER OF DOSES ADMINISTERED : ")
                vac['STATUS'] = input('ENTER VACCINATION STATUS : ')
                d.update(vac)
                pickle.dump(vac, f)  # dump is used to write in a file
            else:
                pickle.dump(vac, f)
    except EOFError:
        pass
    file.close()
    f.close()
    os.remove("Vaccine.dat")
    os.rename("temp.dat", "Vaccine.dat")
    file = open("Vaccine.dat", "rb")  # r-read , b-binary
    try:
        while True:
            vac = pickle.load(file)  # load is used to read
            print(vac)
    except EOFError:
        pass
    file.close()
    x = d.items()
    f = open('Vaccine.csv','w')
    w = csv.writer(f)
    w.writerows(x)
    f.close()
    
def delete():
    file = open("Vaccine.dat", "rb")  # r-read , b-binary
    f = open("temp.dat", "ab")
    a = int(input("ENTER AADHAR NUMBER TO BE DELETED : "))
    try:
        while True:
            vac = pickle.load(file)  # load is used to read
            if vac["AADHAR NUMBER"] == a:
                pass
            else:
                pickle.dump(vac, f)
    except EOFError:
        pass
    file.close()
    f.close()
    os.remove("Vaccine.dat")
    os.rename("temp.dat", "Vaccine.dat")
    file = open("Vaccine.dat", "rb")  # r-read , b-binary
    print("RECORDS AFTER DELETION : ")
    try:
        while True:
            vac = pickle.load(file)  # load is used to read from file
            print(vac)
    except EOFError:
        pass
    file.close()
    n = open('Vaccine.dat','rb')
    try :
        while True :
            v = pickle.load(n)
    except EOFError :
        n.close()
    x = v.items()
    fl = open('Vaccine.csv','w')
    w = csv.writer(fl)
    w.writerows(x)
    fl.close()

# MAIN PROGRAM
while True:
    print("MENU \n1.WRITE IN A FILE \n2.DISPLAY \n3.SEARCH \n4.UPDATE \n5.DELETE \n6.EXIT")
    ch = int(input("ENTER YOUR CHOICE : "))
    if ch == 1:
        write_data()
    elif ch == 2:
        display()  
    elif ch == 3:
        search() 
    elif ch == 4:
        update()  
    elif ch == 5:
        delete()  
    elif ch == 6:  
        sys.exit()
        print("THANK YOU !! HAVE A NICE DAY.")
    else :
        print('INVALID INPUT !!!')
