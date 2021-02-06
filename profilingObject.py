import profiling

print("This program profiles 3 people by asking the user information of those 3 people." +
      "After the information is entered the user can lookup people based on attributes."+
      "This can help organizations/police department look up people just by entering one"+
      "attribute of the person (address, height, name, weight, phone number, etc)\n")


# info about person1
name1 = input("Enter Name: ")
address1 = input("Enter Address: ")
phone1 = input("Enter Phone Number: ")
gender1 = input("Enter Gender: ")
height1 = input("Enter Height: ")
weight1 = input("Enter Weight: ")

person1 = profiling.Profiling(name1)
person1.addAddress(address1)
person1.addPhone(phone1)
person1.addGender(gender1)
person1.addHeight(height1)
person1.addWeight(weight1)

#info about person2
name2 = input("\nEnter Name: ")
address2 = input("Enter Address: ")
phone2 = input("Enter Phone Number: ")
gender2 = input("Enter Gender: ")
height2 = input("Enter Height: ")
weight2 = input("Enter Weight: ")

person2 = profiling.Profiling(name2)
person2.addAddress(address2)
person2.addPhone(phone2)
person2.addGender(gender2)
person2.addHeight(height2)
person2.addWeight(weight2)

#info about person3
name3 = input("\nEnter Name: ")
address3 = input("Enter Address: ")
phone3 = input("Enter Phone Number: ")
gender3 = input("Enter Gender: ")
height3 = input("Enter Height: ")
weight3 = input("Enter Weight: ")

person3 = profiling.Profiling(name3)
person3.addAddress(address3)
person3.addPhone(phone3)
person3.addGender(gender3)
person3.addHeight(height3)
person3.addWeight(weight3)

'''_____________________________________________________________________________'''

#LOOK UP A PERSON BASED ON ATTRIBUTES
lookUp = input("Look up a person?: ")
while lookUp == "Y" or lookUp == "y" or lookUp == "yes" or lookUp == "Yes" or lookUp == "YES":
    method = input("Method of looking up (name, address, phone, gender, height, weight): ")

    #lookup using name
    if method.lower() == "name":
        name_lookUp = input("Name lookup: ")
        print("\n")
        if name_lookUp.lower() == name1.lower():
            person1.profile()
            print("\n")
        if name_lookUp.lower() == name2.lower():
            person2.profile()
            print("\n")
        if name_lookUp.lower() == name3.lower():
            person3.profile()
            print("\n")

    #lookup using address
    elif method.lower() == "address":
        add_lookUp = input("Address lookup: ")
        print("\n")
        if add_lookUp.lower() == address1.lower():
            person1.profile()
            print("\n")
        if add_lookUp.lower() == address2.lower():
            person2.profile()
            print("\n")
        if add_lookUp.lower() == address3.lower():
            person3.profile()
            print("\n")

    #lookup using phone number        
    elif method.lower() == "phone":
        phone_lookUp = input("Phone Number lookup: ")
        print("\n")
        if phone_lookUp.lower() == phone1.lower():
            person1.profile()
            print("\n")
        if phone_lookUp.lower() == phone2.lower():
            person2.profile()
            print("\n")
        if phone_lookUp.lower() == phone3.lower():
            person3.profile()
            print("\n")

    #lookup using gender
    elif method.lower() == "gender":
        gender_lookUp = input("Gender lookup: ")
        print("\n")
        if gender_lookUp.lower() == gender1.lower():
            person1.profile()
            print("\n")
        if gender_lookUp.lower() == gender2.lower():
            person2.profile()
            print("\n")
        if gender_lookUp.lower() == gender3.lower():
            person3.profile()
            print("\n")

    #lookup using height
    elif method.lower() == "height":
        height_lookUp = input("Height lookup: ")
        print("\n")
        if height_lookUp.lower() == height1.lower():
            person1.profile()
            print("\n")
        if height_lookUp.lower() == height2.lower():
            person2.profile()
            print("\n")
        if height_lookUp.lower() == height3.lower():
            person3.profile()
            print("\n")

    #lookup using weight
    elif method.lower() == "weight":
        weight_lookUp = input("Weighe lookup: ")
        print("\n")
        if weight_lookUp.lower() == weight1.lower():
            person1.profile()
            print("\n")
        if weight_lookUp.lower() == weight2.lower():
            person2.profile()
            print("\n")
        if weight_lookUp.lower() == weight3.lower():
            person3.profile()
            print("\n")

    else:
        print("You did not chose the method from the given list")
    lookUp = input("Look up a person?: ")
        
