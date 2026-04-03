import data
from colorama import Fore, Style

Contact=data.load_contacts() 

def get_valid_name(prompt="Enter name: "):
    while True:
        name=input(prompt).lower().strip()
        if not name:
            print(Fore.Red+"you didn't enter valid name!!"+Style.RESET_ALL)
            continue
        elif any(con['Name']==name for con in Contact):
            print(Fore.YELLOW+"Already name is exit , try enter unique name"+Style.RESET_ALL)
            continue
        elif name.replace(" ","").isalpha():
            return name
        else:
            print(Fore.RED +f"Invalid name:{name}."+Style.RESET_ALL)
            continue

def get_valid_phone(prompt="Enter phone number: "):
    while True:
        phone=input(prompt)
        if phone.isdigit() and len(phone)==10 and len(set(phone))!=1:
            return phone
        else:
            print(Fore.RED+f"Invalid phone number:{phone}."+Style.RESET_ALL)


# adding contact
def add_contact():
    d={}
    d['Name']=get_valid_name()
    d['Phone']=get_valid_phone()
    Contact.append(d)
    data.save_contacts(Contact)
    print(Fore.GREEN+"Successfully Added Contact!"+Style.RESET_ALL)
    print()

# view for contact
def add_view():
    if not Contact:
        print(Fore.YELLOW+"No Contact Found.")
    else:
        print("\n---Contact list---")
        for con in Contact:
            print(Fore.CYAN+f"{con['Name']:<20}"+ Style.RESET_ALL +
                   Fore.LIGHTMAGENTA_EX + f"{con['Phone']}"+Style.RESET_ALL)

    
# searching Contact 
def add_search():
    while True:
        name=input("Enter name:").lower().strip()
        if not name.replace(" ","").isalpha():
            print(Fore.RED+"Invalid name, please enter valid name!!"+Style.RESET_ALL)
            continue
        else:
            break

    found=False
    for con in Contact:
        if name==con['Name']:
            print(f"{con['Name']:<15} {con['Phone']}")
            found=True
    if not found:
        print(Fore.YELLOW+"Contact is not found!!"+Style.RESET_ALL)

# delete a Contact 
def del_contact():
    while True:
        name=input("enter a name:").lower().strip()
        if not name.replace(" ","").isalpha():
            print(Fore.RED+"Invalid name,please enter a valid name"+Style.RESET_ALL)
            continue
        break
    for con in Contact:
        if name==con['Name']:
            Contact.remove(con)
            data.save_contacts(Contact)
            print(Fore.GREEN+"Successfully deleted contact!!!"+Style.RESET_ALL)
            return
    print(Fore.YELLOW+"Contact is not found!!"+Style.RESET_ALL)

# modify contact 
def edit_contact():
    name=input("Enter name:").lower().strip()
    for con in Contact:
        if name==con['Name']:
            print(f"Contact found : {con['Name']:<15} {con['Phone']}")
            new_name=input("Enter new name (or press enter to skip): ").strip().lower()
            if new_name:
                if new_name.replace(" ","").isalpha():
                    con['Name']=new_name
                    print(Fore.GREEN+"Updated Name."+Style.RESET_ALL)
            new_phone=input("Enter new Phone number (or press enter to skip): ")
            if new_phone:
                if new_phone.isdigit() and len(new_phone)==10 and len(set(new_phone))!=1 :
                    con['Phone']=new_phone
                    print(Fore.GREEN+"Updated phone number."+Style.RESET_ALL)
            
            data.save_contacts(Contact)
            print(Fore.GREEN+"Successfully Updated Contact"+Style.RESET_ALL)
            return
    print(Fore.YELLOW+"Contact Not Found."+Style.RESET_ALL)
    return
                      
while True:
    try:
        menu=(Fore.LIGHTWHITE_EX+"***Contact Book***\n"+Style.RESET_ALL+
            "1.Add Contact\n"
            "2.View Contact\n"
            "3.Search Contact\n"
            "4.Delete Contact\n"
            "5.Edit Contact\n"
            "6.Exit\n")
        
        choice=int(input(menu+"Enter your choice:"))
        if choice==1:
            add_contact()
        elif choice==2:
            add_view()
        elif choice==3:
            add_search()
        elif choice==4:
            del_contact()
        elif choice==5:
            edit_contact()
        elif choice==6:
            print(Fore.YELLOW+"your program is terminated!"+Style.RESET_ALL)
            break
        else:
            print(Fore.YELLOW+"please enter valid number(1-6)"+Style.RESET_ALL)

    except ValueError:
        print(Fore.RED+"Invalid input! please enter a number !!"+Style.RESET_ALL)


