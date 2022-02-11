from django.shortcuts import render

# Create your views here.

import pyfiglet

def index(request):

    if request.method=='POST':
        text=request.POST.get('txt')
        text_font=request.POST.get('font')
        print(text)
        print(text_font)

        #1. converting text to ASCII using pyfiglet third-pary library
        txt=pyfiglet.figlet_format(text, font=text_font) #create ASCII-text in 'txt' string
        print(txt)
        # print(type(txt))

        #2. ASCII-text to txt using python inbuilt file operation libraries
        file = open('static/output.txt','w') #reading file in writing mode
        file.write(str(txt)) #writiing method to write that text
        file.close() #close method to save and close



        return render(request,'output.html',{'result':txt})
 
    return render(request,'index.html',{})


# Tutorial
    # text to docx coverting library - python-docx third-pary library
    # import docx /////////////////////////////////////////////////

    # doc=docx.Document() #creating empty document
    # print(type(doc))
    # doc.add_paragraph('Hai Iam Abhijith') #adding string paragraph
    # paraObject=doc.add_paragraph('Moncy') #adding string paragraph with other object
    # paraObject.add_run('continuing') # continue the editing
    # doc.save('output.docx') # saving the document
    # //////////////////////////////////////////////////////////////////

