import folium #We import folium which can do a graphic
from Sigma import * #We import the main file to use it
from log.log import *

def MapGeneration(log):
    Carte = folium.Map(location = [45.8, 1.2], zoom_start = 6, tiles = "cartodbpositron") # insialization of the map, location, zoom and title

    #verify log presence - not finish, still in dev
    if log == 1:
        a = LogVerif() #take the saved data
    else :
        LogClean() #clean the loge file
        a = RS()    #calculate new data
        LogSave([a[0]],[a[1]],[a[2]],[a[3]]) #save new data in log

    for Rnum in range(1,96): # Loop to permit the creation the outlines of the departments and the background

        dep= "" 
        
        if Rnum < 10 : #Condition to integrate one by one all the outlines of the departments
            dep = "departements\departement-0"+str(Rnum)+".geojson"
        else:
            dep = "departements\departement-"+str(Rnum)+".geojson"
        
        #We add the background color, the name and the code of each departements in function of the departement file in the departements folder
        if int(a[2][Rnum-1]) >= 100  and int(a[0][Rnum-1]) <= 40: #Condtion to integrate the background in function of the nuber of day in sigma 0%, 20% and 80%
            folium.GeoJson(dep , style_function=lambda feature: {"color": " darkgreen"},popup=folium.GeoJsonPopup(fields=["nom", "code"], labels=True)).add_to(Carte)  #the background is darkgreen if the number of day with 80% is really high and the number with 0% is low
        elif int(a[2][Rnum-1]) >= 60  and int(a[0][Rnum-1]) <= 40: 
            folium.GeoJson(dep , style_function=lambda feature: {"color": "greenyellow"},popup=folium.GeoJsonPopup(fields=["nom", "code"], labels=True)).add_to(Carte) #the background is greenyellow if the number of day with 80% is high and the number with 0% is low
        elif int(a[2][Rnum-1]) >= 40  and int(a[0][Rnum-1]) <= 50 : 
            folium.GeoJson(dep , style_function=lambda feature: {"color": "yellow"},popup=folium.GeoJsonPopup(fields=["nom", "code"], labels=True)).add_to(Carte) #the background is yellow if the number of day with 80% is low and the number with 0% is high
        elif int(a[3][Rnum-1]) == 0 : 
            folium.GeoJson(dep , style_function=lambda feature: {"color": "blue"},popup=folium.GeoJsonPopup(fields=["nom", "code"], labels=True)).add_to(Carte) #the background is blue if we don't have any data one the department
        elif int(a[2][Rnum-1]) <= 40  and int(a[0][Rnum-1]) <= 50 : 
            folium.GeoJson(dep , style_function=lambda feature: {"color": "orange"},popup=folium.GeoJsonPopup(fields=["nom", "code"], labels=True)).add_to(Carte) #the background is orange if the number of day with 80% is lower than 30 and the number with 0% is high
        else : 
            folium.GeoJson(dep , style_function=lambda feature: {"color": "red"},popup=folium.GeoJsonPopup(fields=["nom", "code"], labels=True)).add_to(Carte) #the background is red if the the difference between sigma 0% and 80% when the number of day with sigma 0% is higher
        
    Carte.save("map.html") #this function save the map in html in the folder you choose