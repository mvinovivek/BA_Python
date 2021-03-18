#This code will compute the weight in different planets

planets=["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn","Neptune","Uranus","Pluto","All"]
gvals=[3.61,	8.83,	9.81,	3.75,	26.0,	11.2,	10.5,	13.3,	0.61]

def greet():
    """
    This function will greet the user!
    No inputs necessary and will not return any output
    """
    print("Hello There!")
    print("Welcome to Astro Weight Calculator!")


def get_mass():
    """
    This function will request user for the mass input
    It will also validate the input
    It Returns the mass input of the user
    """
    print("Kindly Enter Your Mass")
    mass=input()
    try:
        mass_converted=float(mass)
        return mass_converted
    
    except:
        print("{} is not a number!".format(mass))
        get_mass()

def show_choices():
    """
    This function displays the Planet List available
    No inputs required
    No output either
    """
    print("Please Select the Planet")
    for i in range(len(planets)):
        print(i+1, planets[i])
    print("Use numbers only!")


def verify_planet_selection(choice):
    """
    This function is used to verify the planet selection input
    This acts like a validator case
    """
    if choice.isdigit():
        choice=int(choice)
        if choice<=9:
            verification=True
            message="{} is an amazing Planet!".format(planets[choice-1])
            return choice, verification,message

        elif choice==10:
            verification=True
            message="Lets go all Around!".format(planets[choice-1])
            return choice, verification,message
            
        else:
            verification = False
            message="{} is not available in the list".format(choice)
            return choice,verification,message

    else:
        verification = False
        message="{} is not a valid input".format(choice)
        return choice,verification,message

def compute_all(mass_input):
    for i in range(len(gvals)):
        print("Weight in {} is {} N".format(planets[i], round(compute_planet(i,mass_input),3)))

def compute_planet(planet, mass):
    return mass*gvals[planet]


#Main function starts here
greet()
mass_input=get_mass()
print("Amazing!")

verification=False
while verification==False:
    show_choices()
    unverified_input=input()
    verified_input,verification, message =verify_planet_selection(unverified_input)
    print(message)


if verified_input==10:
    compute_all(mass_input)

else:
    weight=compute_planet(verified_input-1,mass_input)
    print("Weight in {} is {} N".format(planets[verified_input-1], round(weight,3)))

print("Thank you for using the Program!!!")