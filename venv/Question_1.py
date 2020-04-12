d1={"Teacher":"Shikshak", "Book":"Pustak","Friend":"Mitr"}
d2={"Shikshak":"Adhyapak","Pustak":"Kitab","Mitr":"Dost"}

# printing the dictionry as given question
for x , y in d1.items():

    print(x +  " in Hindi means " + y +" and in Urdu means " + d2.get(y))