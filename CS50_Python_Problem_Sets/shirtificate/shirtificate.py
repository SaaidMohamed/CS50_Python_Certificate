from fpdf import FPDF

def main():
    get_shirtificate(get_name())



def get_name():
    inpt_name = input("Name: ")
    inpt_name = inpt_name.strip().title()
    return inpt_name


def get_shirtificate(inpt_name):

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)

    pdf.add_page()

    pdf.set_font("helvetica", "B", 40)
    pdf.set_text_color(165, 28, 48)
    text_str = "CS50 Shirtificate"
    x0= (pdf.w/2 )- (pdf.get_string_width(text_str)/2)
    y0 = 30
    pdf.text(x0, y0, text_str)


    x = pdf.w/2 - 100
    y = pdf.w/4
    pdf.image("shirtificate.png", x,y,200,)

    pdf.set_font("helvetica", "B", 15)
    pdf.set_text_color(255, 255, 255)
    text = f"{inpt_name} took CS50"
    x1= (pdf.w/2 )- (pdf.get_string_width(text)/2)
    y1 = pdf.h/2.5
    pdf.text(x1, y1, text )


    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()