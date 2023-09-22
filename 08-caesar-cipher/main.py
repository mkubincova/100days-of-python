import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, input_text, shift):
    output_text = ''

    if direction == 'd': shift *= -1
    
    for char in input_text:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_char_index = (char_index + shift) % len(alphabet)
            output_text += alphabet[new_char_index]
        else:
            output_text += char
        
    return output_text

def user_input():
    direction = ''
    while (direction != 'e') and (direction != 'd'):
        direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()

    input_text = input("Type your message:\n").lower()

    shift = ''
    while shift.isnumeric() == False:
        shift = input("Type the shift number:\n")
    shift = int(shift)

    return direction, input_text, shift

def main():
    direction, input_text, shift = user_input()

    output = caesar(direction, input_text, shift)
    phrase = 'encoded' if direction == 'e' else 'decoded'

    print(f"The {phrase} text is {output}")

    again = input("Do you want to go again? Y/n ").lower()
    if again == 'y':
        main()
    

# Start
print(art.logo)
main()

    

