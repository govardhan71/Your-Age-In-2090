while True:
    print("enter your age or year of birth")
    age=int(input())
    if 1<age<100:
        year_to_beome_100=2020+100-age
        print("you will get 100 years old in ",year_to_beome_100)
    elif 1920<age<=2020:
        year_to_beome_100 = 100+age
        print("you will get 100 years old in ", year_to_beome_100)
    elif 100<=age<=1920:
        print("your tooo old ")
        continue

    elif age>2020:
        print("your not born yet")
        continue
    else:
        print("invalid age")
        continue
    print("do you want to find your age in any particuler year yes or no")
    q=input()
    if q=="yes":
        year=int(input("enter in which year you want your age"))
        if 1 < age < 100:
            age_new = age+2020-year
            print("your age will become  ", age_new)
        elif 1920 < age <= 2020:
            age_new = year-age
            print("your age will become  ", age_new )
    else:
        print("thank you")