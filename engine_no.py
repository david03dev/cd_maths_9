"""In XYZ country there is rule that car’s engine no. depends upon car’ number plate. 
Engine no is sum of all the integers present on car’s Number plate.
The issuing authority has hired you in order to provide engine no. to the cars.
Your task is to develop an algorithm which takes input as in form of string(Number plate) and gives back"""


def calculate_engine_number(plate):
    # Initialize sum to zero
    engine_number = 0
    # Iterate over each character in the string
    for char in plate:
        if char.isdigit():
            # Add the integer value of the digit to the engine number
            engine_number += int(char)
    return engine_number


if __name__ == "__main__":
    
    ip_num = input().strip()
    print(calculate_engine_number(ip_num))
