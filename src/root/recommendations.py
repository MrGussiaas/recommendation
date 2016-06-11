from math import sqrt
def sim_distance(prefs, person1, person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    if len(si)==0:return 0    

    sum_of_squares = sum([pow(prefs[person1][item2]-prefs[person2][item2], 2)
                        for item2 in si])
    return 1/(1 + sqrt(sum_of_squares));
                             
    
critics={
         
         'Lisa Rose'       :{'Lady in the Water':2.5,'Snakes on a Plane':3.5,'Just My Luck':3.0,'Superman Returns':3.5,'You, Me and Dupree':2.5,'The Night Listener':3.0},
         'Gene Seymour'    :{'Lady in the Water':3.0,'Snakes on a Plane':3.5,'Just My Luck':1.5,'Superman Returns':5.0,'The Night Listener':3.0,'You, Me and Dupree':3.5,},
         'Michael Phillips':{'Lady in the Water':2.5,'Snakes on a Plane':3.0,'Superman Returns':3.5,'The Night Listener':4.0},
         'Claudia Puig'    :{'Snakes on a Plane':3.5,'Just My Luck':3.0,'The Night Listener':4.5,'Superman Returns':4.0,'You, Me and Dupree':2.0},
         'Mick LaSalle'    :{'Lady in the Water':3.0, 'Snakes on a Plane':4.0,'Just My Luck':2.0,'Superman Returns':3.0,'The Night Listener':3.0,'You, Me and Dupree':3.5},
         'Jack Matthews'   :{'Lady in the Water':3.0,'Snakes on a Plane':4.0,'The Night Listener':3.0,'Superman Returns':5.0,'You, Me and Dupree':3.5},
         'Toby'            :{'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0},
         'Gussiaas'        :{'Superman Returns':5.0},
         'Brian'           :{'Superman Returns':5.0}
}

#Use Euclidean Distance to compute a similarity score
#     calculate by 
#      _________________________________
#    \/((y1 - y2) ^ 2) + ((x1 - x2) ^ 2)
#      
#     


#lrWater = critics['Lisa Rose']['Lady in the Water']
#lrSnakes = critics['Lisa Rose']['Snakes on a Plane']
#gsWater = critics['Gene Seymour']['Lady in the Water']
#gsSnakes =  critics ['Gene Seymour']['Snakes on a Plane']

#print 'Lisa Rose Lady In The Water Rating ' + str(lrWater)
#print 'Lisa Rose Snakes on a Plane Rating ' + str(lrSnakes)
#print 'Gene Seymour Lady In The Water Rating '+ str(gsWater)
#print 'Gene Seymour Snakes on a Plane Rating ' + str(gsSnakes)

#euclideanDistance = 1 / (1 + sqrt(pow((lrWater - gsWater), 2) + pow((lrSnakes - gsSnakes), 2)))
#print 'The Euclidean Distance is : ' + str(euclideanDistance) 