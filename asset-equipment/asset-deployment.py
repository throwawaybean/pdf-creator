import PySimpleGUI as sg
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import date
import sys

# CALL THE PDF CREATOR

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)


#FORM HERE


layout = [

 	[sg.Text('I T  A L L O C A T I O N  F O R M', size=(50, 1), justification='center', font=("Calibri", 25), relief=sg.RELIEF_FLAT)],
    [sg.Text('Name:'), sg.InputText('',key='Name'), sg.Text('Office Location:'), sg.InputText('',key='Office')],

    [sg.Frame('Contract Type',[
    [sg.Radio('Permanent', "RADIO1", key='Contract', default=True, size=(10,1,)), sg.Radio('Non-permanent', "RADIO1", key='Contract2')]])],

    [sg.Frame('Asset Type',[
    [sg.Radio('Desktop', "RADIO2", key='Desktop',), sg.Radio('Laptop', "RADIO2", key='Laptop', default=True, size=(10,1,)), sg.Radio('iPad', "RADIO2", key='iPad')]])],

    [sg.Frame('C O M P U T E R',[
    [sg.Text('Brand:',), sg.InputText('', key='CBrand')],
    [sg.Text('Model:'), sg.InputText('', key='CModel')],
    [sg.Text('Serial:'), sg.InputText('', key='CSerial')],
    [sg.Text('Tag:   '), sg.InputText('', key='CTag')],
    [sg.Text('Computer Name:'), sg.InputText('', key='CName')]]),

    sg.Frame('M O N I T O R',[
    [sg.Text('Brand:'), sg.InputText('', key='MBrand')],
    [sg.Text('Model:'), sg.InputText('', key='MModel')],
    [sg.Text('Serial:'), sg.InputText('', key='MSerial')],
    [sg.Text('Tag:   '), sg.InputText('', key='MTag')],])],

    [sg.Frame('Accesories',[
    [sg.Checkbox('Docking station', key='Dock'), sg.Checkbox('Keyboard', key='Keyboard'), sg.Checkbox('Mouse', key='Mouse')]])],

 #   [sg.Text('_' * 80)],
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

pdf = '.pdf'
path = values['path']
today = date.today()
date = today.strftime("%d/%m/%Y")
text_input1 = values['Name']
text_input2 = values['Office']
text_input12 = values['Contract']
text_input3 = values['CBrand']
text_input4 = values['CModel']
text_input5 = values['CSerial']
text_input6 = values['CTag']
text_input7 = values['CName']
text_input8 = values['MBrand']
text_input9 = values['MModel']
text_input10 = values['MSerial']
text_input11 = values['MTag']
text_input13 = values['Dock']
text_input14 = values['Keyboard']
text_input15 = values['Mouse']
text_input16 = values['Laptop']
text_input17 = values['Desktop']
text_input18 = values['iPad']

filename = path + '/' + text_input1 + ' (' + text_input7 + ')' + ".pdf"


#INPUT THE THE VALUES IN THE PDF

can.drawString(109, 678, text_input1)
can.drawString(309, 678, text_input2)
can.drawString(120, 380, text_input3)
can.drawString(120, 360, text_input4)
can.drawString(120, 340, text_input5)
can.drawString(120, 320, text_input6)
can.drawString(135, 295, text_input7)
can.drawString(250, 385, text_input8)
can.drawString(250, 365, text_input9)
can.drawString(250, 345, text_input10)
can.drawString(250, 325, text_input11)
can.drawString(105, 220, date),


if text_input12 == True : 
    can.drawString(96,653, 'x'),

if text_input13 == True :
    can.drawString(343, 384, 'Docking station'),
    can.drawString(150, 273, 'x'),
    can.drawString(411, 535, 'x'),

if text_input14 == True :
    can.drawString(343, 364, 'Keyboard'),
    can.drawString(276, 524, 'x'),

if text_input15 == True :
    can.drawString(343, 344, 'Mouse'),
    can.drawString(410, 547, 'x'),

if text_input16 == True :
	can.drawString(321, 547, 'x'),
	can.drawString(87, 547, 'x'),
	can.drawString(128, 400,'x'),

if text_input17 == True :
	can.drawString(88, 558, 'x')
	can.drawString(87, 400, 'x')

if text_input18 == True :
	can.drawString(169, 400, 'x')

can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("asset.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)    
# finally, write "output" to a real file

outputStream = open(filename, "wb")
output.write(outputStream)
outputStream.close()

sg.Popup('Done', no_titlebar=True, grab_anywhere=True, keep_on_top=True)
