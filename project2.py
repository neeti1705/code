
import requests
import csv  
import os

 # Function to create folder
def createFolder(directory):                 
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
createFolder('./data2/')

links = []
cells = []

with open("Animals.csv", 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        #adding all links in an array 
        links.append(line[1])      
        #adding all names in an array 
        cells.append(line[0])  
        
    i=0;
    for address in links :
        #except 1st row 
        if address !="Links" :    
            i=i+1;
            #fetching data from link
            r = requests.get(address)   
            #creating our file to copy the data in our folder
            with open('data2/'+cells[i]+'.jpg','wb') as f:
                 # writing data into our file
                f.write(r.content)    
            print(cells[i]+'.jpg file downloaded')
           


"""
Output :
       
Lion.jpg file downloaded
Tiger.jpg file downloaded
Elephant.jpg file downloaded
Zebra.jpg file downloaded
Cat.jpg file downloaded
Dog.jpg file downloaded
Monkey.jpg file downloaded

"""
    
    