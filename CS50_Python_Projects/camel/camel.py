def main():
    camel_case_inpt = input("camelCase: ")
    camel_case_inpt = camel_case_inpt.strip()
    convert_to_camel(camel_case_inpt)



def convert_to_camel(variable_name):
    for letter in variable_name:
        if letter.isupper():
            letter_lower = "_" + letter.lower()
            new_variable_name = variable_name.replace(letter,letter_lower)
            variable_name = new_variable_name
    print(variable_name)


if __name__ == "__main__":
    main()
