input_string = str(input("Enter a sentence: "))

def get_dog(input_string):
    
    words = input_string.split(" ")

    for i in words:
        i = i.capitalize()
        if i == "Dog":
            print("Yes")
            return True
        else:
            continue
        
get_dog(input_string)
