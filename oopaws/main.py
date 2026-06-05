from pet import Pet

def display_pet_info(pet):

    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    
    print("\nPet Information")
    print("Name:", pet.get_name())
    print("Animal Type:", pet.get_animal_type())
    print("Age:", pet.get_age())

def main():
    my_pet = Pet()
    name = input("Enter your pet's name: ")
    animal_type = input("Enter the type of animal: ")
    age = int(input("Enter the pet's age in months: "))

    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)

    display_pet_info(my_pet)

main()