def main():
    inpt_text = input()
    convert(inpt_text)
    print(convert(inpt_text))

def convert(strText):
    SSF = "🙂"
    SFF = "🙁"
    strText = strText.replace(':)',SSF)
    strText = strText.replace(':(',SFF)
    return strText

main()