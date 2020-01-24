from fpdf import FPDF
from drinks import drink_list, ingredients, available_ingredients, available_drinks, alcoholic, doable

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('../images/logo_400.png', 170, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(50, 10, 'Let-Him-Mix', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 13)
        # Page number
        self.multi_cell(0, 5, 'Seite ' + str(self.page_no()) + '/{nb}' + '\nwww.let-him-mix.de', 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_auto_page_break(0)
height_of_cell = 5
page_height = 295
bottom_margin = 15
pdf.set_font('Times', '', 12)
#for i in range(1, 41):
#    pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)


for drink in available_drinks:
    pdf.set_font('Times', '', 14)
    space_left=page_height-(pdf.get_y()+bottom_margin) # space left on page
    if (height_of_cell * 2 > space_left):
        pdf.add_page() # page break
    pdf.cell(60, 5, drink["name"]  + ("" if alcoholic(drink) else " (alkoholfrei)"), 0,2)
    pdf.cell(10, 5, '         ', 0, 0)
    currentingredients=[]
    for step in drink["recipe"]:
        currentingredients.append(ingredients[step[1]][0])
    pdf.set_font('Times', '', 13)
    pdf.cell(50, 5, ', '.join(currentingredients), 0, 0)
    pdf.cell(0, 7, '', 0, 1)

pdf.output('cocktailkarte.pdf', 'F')
