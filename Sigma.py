import csv


#Sigma insolation value reading

def RS():
    Ftr = "" #File to Read

    RS0 = []    #readed Sigma = 0%
    RS20 = []   #readed Sigma < 20%
    RS80 = []   #readed Sigma > 80%
    count = [] #count number of usefull station

    for Rnum in range(0,95): #creating empty value for each region for an easier add during the file reading
        RS0.append(0)
        RS20.append(0)
        RS80.append(0)
        count.append(0)

    numpcom = 0 #save the station id to don't count it twice

    for Rnum in range(0,95): #for in range nb of region - 1 - add the Rnum for the FiletoRead str
        if Rnum < 9 : Ftr = "data\MENSQ_0"+str(Rnum+1)+"_latest-2024-2025.csv"  #if Rnum is one character int, add a "0" before for the FiletoRead value
        else:Ftr = "data\MENSQ_"+str(Rnum+1)+"_latest-2024-2025.csv"

        with open(Ftr, encoding='utf-8',newline='') as csvfile: #open the region csv file
            reader=csv.reader(csvfile,delimiter=";")

            a=0 #to skip the first line - maybe changing the value name

            for row in reader:

                if a == 0:  #if first line not skiped
                    a = 1   #SKIP DA LINE
                
                elif row[128] == '' or row[129] == '' or row[130] == '': #if the value we want are empty 
                    print(end="")   #SKIP DA LINE
                
                else :  #if that not the first line and there is the value we want

                    e = int(row[0]) #we take the station post n° - maybe changing the value name
                    if e != numpcom: #if the station post n° is different for the saved one
                        numpcom = e #save the new one
                        count[Rnum]+=1 #add 1 to the count of usefull station
                    
                    RS0[Rnum]+=int(row[128])    #add the number of Sigma = 0 at the exact region place in the list
                    RS20[Rnum]+=int(row[129])   #add the number of Sigma < 20 at the exact region place in the list
                    RS80[Rnum]+=int(row[130])   #add the number of Sigma > 80 at the exact region place in the list

    #some debug
    #print (RS0)
    #print (RS20)
    #print (RS80)
    #print (count)

    #divide every Sigma value by the nb of usefull station
    for Rnum in range(0,95):
        if count[Rnum] == 0:    #we can't divide 0... i think...
            print(end="")
        else:
            RS0[Rnum] = int(RS0[Rnum]/count[Rnum])
            RS20[Rnum] = int(RS20[Rnum]/count[Rnum])
            RS80[Rnum] = int(RS80[Rnum]/count[Rnum])
    
    return(RS0,RS20,RS80,count)   #return all usefull list

    