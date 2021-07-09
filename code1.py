# method 1 by using pytesseract
from re import I
import pytesseract as pbl
pbl.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

# converting image into text
img = Image.open("sample response sheet .png")
text = pbl.image_to_string(img)

#converting all text into lower case to avoid case mistakes in detection
textlower2=text.lower()

#forming list for keywords and marks 
list1=[["honest","responsible","xyz","abc"],["encourage people","support","positive image","pqr"],["listening to others","maintaining positive attitude"]]
list2=[5,5,5]



#actual working starts...
#step1: finding the index of q.1 , q.2...
listindex=[]
for i in range(1,51):
    try:
        x="q."
        b=x+str(i)
        listindex.append(textlower2.index(b))
        
    except:
         pass
       
l=len(listindex)

#step2: selecting the answer which is in between q.i and q.i+1
responsemain=[]
for i in range(0,l+1) :
   try:
      responsemain.append(textlower2[listindex[i]:listindex[i+1]])
   except:
      pass

n1=len(list1)

#step3: finding keywords in the answer
for i in range(0, n1):
        r=0
        listb=list1[i]

        n=len(listb)
        for j in range(0,n):
            index = (responsemain[i]).find(listb[j])
            if (index>0):
                    count = 1
            else :
                    count = 0
            r = r + count
            om =r*list2[i]/n
            #step4: displaying marks question wise
        print("obtained marks for question no.",i+1,"=",om)