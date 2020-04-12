states={"Rajasthan":101,"Haryana":102}

# Adding element to predefined dictionary =>>

states["Assam"] = 103

# Printing dictionary
print(states)

# printing non existing states code

print(states.get("UP"))
# adding another element
states["Goa"] = 104

# printing the dic....
print(states)

#  use of setDefault to dictionary =>>
x = states.setdefault("Goa","104")
print(x)

