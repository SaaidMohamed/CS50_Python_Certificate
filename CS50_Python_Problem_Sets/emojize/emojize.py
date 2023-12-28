from emoji import emojize
str_inpt = input("Input: ").strip()
print(f"Output: {emojize(str_inpt, language='alias')}")