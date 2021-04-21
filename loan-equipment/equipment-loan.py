import PySimpleGUI as sg
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import date
import sys
import os

# CALL THE PDF CREATOR

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)


#FORM HERE

layout = [

 	[sg.Text('EQUIPMENT LOAN FORM', size=(50, 1), justification='center', font=("Calibri", 25), relief=sg.RELIEF_FLAT)],
    [sg.Text('Name:'), sg.InputText('',key='Name'), sg.Text('Office Location:'), sg.InputText('',key='Office')], 
    
    [sg.Radio('Staff', "RADIO1", key='Staff', default=True), 
    sg.Radio('Faculty', "RADIO1", key='Faculty'), 
    sg.Radio('PHD', "RADIO1", key='PHD'), 
    sg.Radio('MBA', "RADIO1", key='MBA'), 
    sg.Radio('Other', "RADIO1", key='Other')],
#   [sg.Frame('Classification',[
#   [sg.Radio('Staff', "RADIO1", key='Contract', default=True), sg.Radio('Faculty', "RADIO1", key='Contract2'), sg.Radio('PHD', "RADIO1"), sg.Radio('MBA', "RADIO1"), sg.Radio('Other', "RADIO1")]])],
    [sg.Frame('IT equipment',[
    [sg.Checkbox('Standard Desktop', key='Desktop')], 
    [sg.Checkbox('Standard laptop', key='Laptop')], 
    [sg.Checkbox('External keyboard', key='Keyboard')], 
    [sg.Checkbox('Network cable', key='Network')], 
    [sg.Checkbox('Docking station', key='Dock')], 
    [sg.Checkbox('Monitor', key='Monitor')], 
    [sg.Checkbox('Printer', key='Printer')]]),


    
    sg.Frame('AV equipment',[
    [sg.Checkbox('Mobile sound station', key='SoundStation')], 
    [sg.Checkbox('Webcam', key='Webcam')], 
    [sg.Checkbox('Camcorder', key='Camcorder')],
    [sg.Checkbox('Projector', key='Projector')],
    [sg.Checkbox('Other', key='Other1')]]),

    sg.Frame('Accesories',[
    [sg.Checkbox('Clicker', key='Clicker')],
    [sg.Checkbox('Multimedia card reader', key='CardReader')],
    [sg.Checkbox('Audio cable/Video cable', key='Cable')],
    [sg.Checkbox('Power supply', key='Powersupply')], 
    [sg.Checkbox('Mouse', key='Mouse')], 
    [sg.Checkbox('Other', key='Other2')]])],


    [sg.Frame('Equipment 1',[
    [sg.Text('Model:',), sg.InputText('', key='Model')],
    [sg.Text('Serial:'), sg.InputText('', key='Serial')],
    [sg.Text('Tag:   '), sg.InputText('', key='Tag')],]),

    sg.Frame('Equipment 2',[
    [sg.Text('Model:'), sg.InputText('', key='Model1')],
    [sg.Text('Serial:'), sg.InputText('', key='Serial1')],
    [sg.Text('Tag:   '), sg.InputText('', key='Tag1')],])],

   [sg.Text('  ' )],
   [sg.In(key='Calendar', visible=False), sg.CalendarButton('Return date', target='Calendar', format=('%d/%m/%Y'))],


   [sg.Text('Choose A Folder', size=(35, 1))],

    [sg.InputText(os.path.join(os.path.expanduser("~\Desktop")), key='path'), sg.FolderBrowse()],
    [sg.Button('Submit'), sg.Button('Cancel')]]


#create the Window
window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=True, no_titlebar=True, keep_on_top=True)

#button, values = window.read()
event, values = window.read()

if event == 'Cancel':
	sys.exit()

window.close()

# INPUT DEFINED VALUE HERE

calendar = values['Calendar']
pdf = '.pdf'
path = values['path']
today = date.today()
date = today.strftime("%d/%m/%Y")
text_input1 = values['Name']
text_input2 = values['Office']
text_input3 = values['Staff']
text_input4 = values['Faculty']
text_input5 = values['PHD']
text_input6 = values['MBA']
text_input7 = values['Other']
text_input8 = values['Desktop']
text_input9 = values['Laptop']
text_input10 = values['Keyboard']
text_input11 = values['Network']
text_input12 = values['Dock']
text_input13 = values['Monitor']
text_input14 = values['Printer']
text_input15 = values['SoundStation']
text_input16 = values['Webcam']
text_input17 = values['Camcorder']
text_input18 = values['Projector']
text_input19 = values['Other1']
text_input20 = values['Clicker']
text_input21 = values['CardReader']
text_input22 = values['Cable']
text_input23 = values['Powersupply']
text_input24 = values['Mouse']
text_input25 = values['Other2']

text_input26 = values['Model']
text_input27 = values['Serial']
text_input28 = values['Tag']
text_input29 = values['Model1']
text_input30 = values['Serial1']
text_input31 = values['Tag1']


#filename = path + '/' + text_input1 + ' (' + text_input7 + ')' + ".pdf"

filename = path + '/' + text_input1 + ".pdf"

#INPUT THE THE VALUES IN THE PDF

can.drawString(126, 743, text_input1)
can.drawString(355, 730, text_input2)

if text_input3 == True:
    can.drawString(351, 744, 'x'),
if text_input4 == True:
    can.drawString(381, 744, 'x'),
if text_input5 == True:
    can.drawString(422, 744, 'x'),
if text_input6 == True:
    can.drawString(448, 744, 'x'),
if text_input7 == True:
    can.drawString(479, 744, 'x'),

if text_input8 == True:
    can.drawString(103, 663, 'x'),
if text_input9 == True:
    can.drawString(103, 650, 'x'),
if text_input10 == True:
    can.drawString(103, 639, 'x'),
if text_input11 == True:
    can.drawString(103, 627, 'x'),
if text_input12 == True:
    can.drawString(103, 614, 'x'),
if text_input13 == True:
    can.drawString(103, 602, 'x'),
if text_input14 == True:
    can.drawString(103, 590, 'x'),

if text_input15 == True:
    can.drawString(267, 662, 'x'),
if text_input16 == True:
    can.drawString(267, 650, 'x'),
if text_input17 == True:
    can.drawString(267, 639, 'x'),
if text_input18 == True:
    can.drawString(267, 627, 'x'),
if text_input19 == True:
    can.drawString(267, 614, 'x'),

if text_input20 == True:
    can.drawString(401, 660 , 'x'),
if text_input21 == True:
    can.drawString(401, 650, 'x'),
if text_input22 == True:
    can.drawString(401, 640, 'x'),

if text_input23 == True:
    can.drawString(401, 627, 'x'),
if text_input24 == True:
    can.drawString(443, 614, 'x'),
if text_input25 == True:
    can.drawString(401, 602, 'x'),


can.drawString(277, 549, text_input26)
can.drawString(281, 533, text_input27)
can.drawString(297, 518, text_input28)
can.drawString(282, 484, text_input29)
can.drawString(280, 469, text_input30)
can.drawString(297, 453, text_input31)

can.drawString(103, 532, date)
can.drawString(103, 321, date)
can.drawString(69, 99, text_input1)
can.drawString(103, 468, calendar)




can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("loan.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(1)

page.mergePage(new_pdf.getPage(0))
#add page number 1
output.addPage(existing_pdf.getPage(0))
#add edited page
output.addPage(page)

# finally, write "output" to a real file

outputStream = open(filename, "wb")
output.write(outputStream)
outputStream.close()

sg.Popup('Done', no_titlebar=True, grab_anywhere=True, keep_on_top=True)

