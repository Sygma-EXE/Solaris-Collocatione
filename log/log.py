import csv

def LogSave(S0,S20,S80,Date):
    with open("log\\log.csv","w") as csvfile:
        writer = csv.writer(csvfile, delimiter ="," , quoting = csv.QUOTE_MINIMAL)
        writer.writerow(S0+S20+S80+Date)

def LogVerif():
    with open("log\\log.csv","r") as csvfile:
        reader = csv.reader(csvfile,delimiter=",")
        for row in reader:
            if row != []:
                S0 = row[0]
                S20 = row[1]
                S80 = row[2]
                return (S0,S20,S80)
            else:
                return("Empty")

def LogClean():
    open("log\\log.csv", 'w').close()

