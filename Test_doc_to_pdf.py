from mailmerge import MailMerge # This is the import needed for the doc method
from PyPDF2 import PdfFileReader, PdfFileWriter # This is the import needed for the pdf method
 

#Start of code to output data into PDF
#PDF input works, cant see data in PDF unless I click on it. Very weird...
input = PdfFileReader("Character Sheet - Form Fillable.pdf")
output = PdfFileWriter()

first_page = input.getPage(0)


field = PdfFileReader.getFields(input) #Gets names of fields specified in PDF
#print(field)

field2 = {'ClassLevel': 7}
field.update(field2) #This would be the method to put data into the fields
#print(field)


output.addPage(first_page)

with open("newfile.pdf", "wb") as new: #Exports PDF
    PdfFileWriter.updatePageFormFieldValues(page = first_page, fields = field, self = new)
    output.write(new)

#End of code to output data into PDF

#Start of code to output data into doc
template = "Character Sheet Python.docx"
document = MailMerge(template)
#print(document.get_merge_fields())

document.merge( # Puts data into respective field specified in document. This just uses placeholder values for now.
                # Eventually this would be equal to the values the user would put in.
Initiative = "3",
Armor_Class = "12",
Inspiration = "4",
Equipment = "Short Sword, 15 Arrows, 25 Gold",
Player = "Ish Soni",
Dexterity = "16",
Dexterity_Mod = "+3",
Wisdom = "10",
Wisdom_Mod = "0",
Strength = "12",
Strength_Mod = "+1",
Constitution = "8",
Constitution_Mod = "-1",
Charisma = "14",
Charisma_Mod = "+2",
Intelligence = "12",
Intelligence_Mod = "+1",
Speed = "30ft",
Temp_HP = "10",
Background = "Hermit",
Current_HP = "15",
Class_and_Level = "Wizard LVL 5",
Race = "Human",
Proficiencies_Languages = "Stick, Common, Elvish, Dwarvish",
Flaws = "Just not a good person",
Allignment = "Chaotic Good",
EXP = "150",
Character_Name = "Zeth",
Proficiency_Bonus = "4",
Attacks_Spells = "Fire Ball, 2d6 \n Stick Wack, 1d4",
Bonds = "Jesus")

document.write('test_output.docx') #Exports Doc
#End of code to output data into doc