RT1_SAE105

                                                                                             @@@   
                                                                                         @@@@@     
                                                                                    @@@@@@@@       
                                                                                @@@@@@@@@@         
                                                                            @@@@@@ @@@@@           
                                @@@@@@@@@@@@@@@@@                      @@@@@@@   @@@@              
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@     @@@                
                         @@@@@@@@@@@@@             @@@@@       @@@@@@@       @@@@                  
                      @@@@@@@@@@@@                     @@@@  @@@@@         @@@@                    
   @@@@@@@@@@@@@@@   @@@@@@@@@@@                         @@@@  @@@@      @@@                       
     @@@     @@@   @@@@@@@@@@@                             @@@   @@@   @@@@                        
       @@@  @@@   @@@@@@@@@@@    @@@@@@@@@@                 @@@@  @@@@@@                           
        @@@@@@   @@@@@@@@@@@    @@@@@@@@@@                   @@@@ @@@@                             
          @@@@  @@@@@@@@@@@     @@@@                          @@@  @                               
            @  @@@@@@@@@@@      @@@@                           @@@@                                
              @@@@@@@@@@@       @@@@@@@@@@@                    @@@@                                
              @@@@@@@@@@@        @@@@@@@@@@    @@@@@@           @@@                                
             @@@@@@@@@@@@              @@@@  @@@@@@@@@          @@@@                               
             @@@@@@@@@@@@              @@@@  @@@@               @@@@                               
             @@@@@@@@@@@@        @@@@@@@@@@  @@@@               @@@@                               
             @@@@@@@@@@@@@       @@@@@@@@    @@@@              @@@@@                               
             @@@@@@@@@@@@@@                  @@@@             @@@@@@                               
              @@@@@@@@@@@@@                  @@@@             @@@@@                                
              @@@@@@@@@@@@@@                 @@@@            @@@@@@                                
               @@@@@@@@@@@@@@@               @@@@@@@@@     @@@@@@@@                                
                @@@@@@@@@@@@@@@                @@@@@@     @@@@@@@                                  
                 @@@@@@@@@@@@@@@@@                     @@@@@@@@@@                                  
                  @@@@@@@@@@@@@@@@@@@               @@@@@@@@@@@@                                   
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                     
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                      
                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@                                     
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                                    
                            @@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@                                    
                                @@@@@@@@@@@@@@@@@    @@@@@   @@@                                   
                                                      @@@@    @@@                                  
                                                        @@@@   @@@                                 
                                                          @@@@  @@@                                
                                                            @@@@@@@                                
                                                               @@@@@@                              
                                                                 @@@@                              
                                                                   @@@                             
                                                                      @                            


Vous trouverez ici un petit programme d'analyse de fichier CSV, un par département, concernant la fraction d'insolation par rapport à la durée du jour dit SIGMA depuis 2024.

L’objectif de ce projet est de déterminer les zones géographiques optimales pour l’implantation de panneaux solaires. On prendra en compte la nébulosité, l’inclinaison du soleil en fonction des coordonnées GPS, etc. On pourra compléter avec un fichier .csv contenant les horaires du lever et coucher du soleil.

Utilisation : pour une utilisation optimal, utilisé le fichier "Gui.py", il intérragira avec les autres sans problème.

Attention: les librairies doivent être téléchargés afin d'assurer le bon fonctionnement du programme:
            - PySide6 (et ses add-ons si ne fonctionne toujours pas)
            - folium

Pour la lecture de la carte:
>rouge: extrêmement déconseillé
>orange: déconseillé
>jaune: acceptable
>vert clair: favorable
>vert foncé: très favorable
>bleu: asbence de donnée(s) utile(s)