import data

Contact=data.load_contacts() 

def get_valid_name(prompt="Enter name: "):
    while True:
        name=input(prompt).lower().strip()
        if not name:
            print("you didn't enter valid name!!")
            continue
        elif any(con['Name']==name for con in Contact):
            print("Already name is exit , try enter unique name")
            continue
        elif name.replace(" ","").isalpha():
            return name
        else:
            print(f"Invalid name:{name}.")
            continue

def get_valid_phone(prompt="Enter phone number: "):
    while True:
        phone=input(prompt)
        if phone.isdigit() and len(phone)==10 and len(set(phone))!=1:
            return phone
        else:
            print(f"Invalid phone number:{phone}.")


# adding contact
def add_contact():
    d={}
    d['Name']=get_valid_name()
    d['Phone']=get_valid_phone()
    Contact.append(d)
    data.save_contacts(Contact)
    print("Successfully Added Contact!")
    print()

# view for contact
def add_view():
    if not Contact:
        print("No Contact Found.")
    else:
        print("\n---Contact list---")
        for con in Contact:
            print(f"{con['Name']:<20} {con['Phone']}")

    
# searching Contact 
def add_search():
    while True:
        name=input("Enter name:").lower().strip()
        if not name.replace(" ","").isalpha():
            print("Invalid name, please enter valid name!!")
            continue
        else:
            break

    found=False
    for con in Contact:
        if name==con['Name']:
            print(f"{con['Name']:<15} {con['Phone']}")
            found=True
    if not found:
        print("Contact is not found!!")

# delete a Contact 
def del_contact():
    while True:
        name=input("enter a name:").lower().strip()
        if not name.replace(" ","").isalpha():
            print("Invalid name,please enter a valid name")
            continue
        break
    for con in Contact:
        if name==con['Name']:
            Contact.remove(con)
            data.save_contacts(Contact)
            print("Successfully deleted contact!!!")
            return
    print("Contact is not found!!")

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
                    print("Updated Name.")
            new_phone=input("Enter new Phone number (or press enter to skip): ")
            if new_phone:
                if new_phone.isdigit() and len(new_phone)==10 and len(set(new_phone))!=1 :
                    con['Phone']=new_phone
                    print("Updated phone number.")
            
            data.save_contacts(Contact)
            print("Successfully Updated Contact")
            return
    print("Contact Not Found.")
    return
                      
while True:
    try:
        menu=("***Contact Book***\n"
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
            print("your program is terminated!")
            break
        else:
            print("please enter valid number(1-6)")

    except ValueError:
        print("Invalid input! please enter a number !!")


