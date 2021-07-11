from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

textlower2=""
subscription_key = ""
endpoint = ""

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))



images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")

read_image_path = os.path.join (images_folder, "sample response sheet .png")   
read_image = open(read_image_path, "rb")
read_response = computervision_client.read_in_stream(read_image, raw=True)
read_operation_location = read_response.headers["Operation-Location"]
operation_id = read_operation_location.split("/")[-1]
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status.lower () not in ['notstarted', 'running']:
        break


if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            # print(line.text.lower())  
           
            textlower2+=(line.text.lower())


#converting all text into lower case to avoid case mistakes in detection


#forming list for keywords and marks 
list1=[["honest","responsible","xyz","abc"],["encourage people","support","positive image","pqr"],["listening to others","maintaining positive attitude"]]
list2=[5,5,5]

print(textlower2)

#actual working starts...
#step1: finding the index of q.1 , q.2...
listindex=[]

print(textlower2.index("q.2"))

for i in range(1,51):
    try:
        x="q."
        b=x+str(i)
        listindex.append(textlower2.index(b))
        
    except:
         pass
       
l=len(listindex)

# step2: selecting the answer which is in between q.i and q.i+1
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
