import os
import gzip
import requests
import csv
import maj.majurl as majurl

#channge months initial in month n°
def monthconv(month): #"month" is at the intial 3 letters format "Jan"
    ref = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    return ref[month]

#take the last update date save in "majdate.csv"
def datecatch():
    with open("maj\majdate.csv", encoding='utf-8') as csvfile:
            reader=csv.reader(csvfile,delimiter=",")
            for row in reader:
                  return int(row[0]),int(row[1]),int(row[2]) #return every information into int

#write the new update date in "majdate.csv"
def datenew(newdate): #"newdate" is at the format (year,month,day)
    with open("maj\majdate.csv", "w" , encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter ="," , quoting = csv.QUOTE_MINIMAL)
        writer.writerow(newdate) #write above the old line

#separate the date of the http header we have wut the request in order to be usable with "datetime" and other function
def dateseparator(date):    #"date" in the header is an str and is in the format "day_month_year" (_ is space)
    d = int(date[:2])
    m = monthconv(date[3:6])
    y = int(date[7:11])
    return (y,m,d)  #return the date with day, month and year separated

#check if there is a difference between 2 date
def compa (dateA,dateB): #dateA and dateB are at the format (year,month,day)
    if dateA[0] != dateB[0] or dateA[1] != dateB[1] or dateA[2] != dateB[2]:    #check if every date part are different
        return 1    #1 mean "that different" and an update start
    else :
        return 0    #0 mean "that the same" and the update is canceled


def DoMaj():
    result = 0 #used for the loop
    nbregion = 0    #used with the list "fileid" and "regionfile"
    maj = 0 #used to check if the update is needed

    while result == 0:  #loop since not everyfile was checked/updated

        infocatching = majurl.nameandurl(nbregion)  #take the file url and file name of the specified region
        
        filename = infocatching[0]  #save the file name
        url = infocatching[1]   #save the file url
        
        response = requests.get(url)    #register the respond of the url into the variable "response"
        localfiledate = datecatch()     #take the last update date
        
        if response.status_code == 200: #code 200 mean that there is no problem during the communication
        
            servfiledate = dateseparator(response.headers["Last-Modified"][5:16])   #save date of last modification of the file situated in the header
            maj = compa (localfiledate, servfiledate)   #define if the maj is needed by comparing last local file update date and last server file update date
        
            if maj == 1:    #if the date are different - - note for later: maybe changing it later for "if localfiledate is older than servfiledate"
        
                with open((filename+".gz"), "wb") as file:  #open the file received with the "os" lib
                    file.write(response.content)    #saving the file in the main folder
        
                with gzip.open((filename+".gz"),"rb") as f: #open the saved file with the "gzip" lib to be able to unzip the compressed file
                    file_content = f.read() #read the compressed file
                    with open(filename, "wb") as file:  #create a new file
                        file.write(file_content)    #save the readed compressed file into the created one

                os.remove((filename+".gz")) #delete the unecessary compressed file

                if os.path.exists("data\\"+filename):   #if an older version of the csv exite

                    os.remove("data\\"+filename)    #delet it

                os.replace(filename,("data\\"+filename))    #move the new file into the data folder

            else:   #if the date are the same - - note for later : maybe changing it in case of the file is different than the other
                maj = 0 #reset maj by security
                nbregion = 0    #reset nbregion by security
                return(0)

        else :  #if an error occured
            maj = 0 #reset maj by security
            nbregion = 0    #reset nbregion by security
            return(3)
        
        if nbregion == 94: #if last region file updated
            maj = 0 #reset maj for next time
            nbregion = 0    #reset nbregion for next time
            datenew(servfiledate)   #update the date of majdate
            return(1)

        else:   #if not all region file updated
            nbregion += 1   #incrase nbregion by one