'''
Created on Jun 13, 2016

@author: bgussiaas
'''
from math import sqrt
# first find items common between two sets S1 and S2
#    sum items and the square of the sums of each item from the two sets
#    sum the products of the items 


# S1 = {i0 + i1 + i2 + . . . + in}}
# S1SQ = {i0 ^ 2 + i1 ^ 2 + . . . + in ^2}
# S2 = {j0 + j1 + j2 + . . . + jn}
# S2Sq = {j0 ^ 2 + j1 ^ 2 + . . . + jn ^2}
# S1S2 = {i0 * j0 + i1 * j1 + . . . + in * jn}
#
#Pearson score 
#
#                        (S1 * S2)
#               (S1S2) - ---------
# ___________________________n__________________
#     _________________________________________ 
#    /(           S1 ^ 2    )    (         S2 ^ 2 )
#   / ( S1SQ - ___________  )  * ( S2SQ -  ______ )
# \/  (             n       )    (           n    )
#                                   

def pearson (prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item]=1
        
    n = len(si);
    
    if(n==0):return 0
    
    s1 = sum(prefs[person1][it1] for it1 in si)
    s1sq = sum(pow(prefs[person1][itsq1], 2) for itsq1 in si)
    
    s2 = sum(prefs[person2][it2] for it2 in si)
    s2sq = sum(pow(prefs[person2][itsq2], 2) for itsq2 in si)
    
    s1s2 = sum(prefs[person1][itp] * prefs[person2][itp] for itp in si)
    
    numerator = s1s2 - ((s1 * s2) / n);
    denominator = sqrt((s1sq - pow(s1, 2) / n) * (s2sq - pow(s2, 2) / n))
    
    if denominator == 0: return 0
    
    return numerator / denominator;
 