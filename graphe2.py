import networkx as nx 
from math import sqrt
import csv

#defining a graph 
G = nx.DiGraph()
#pas 
def get_time_path(fichier, fichier2):
    n = 0 
    maxi = 0.0
    mini = 0.0
    with open(fichier, "r+") as f1, open(fichier2,"w+") as f2:
        file_content = csv.DictReader(f1)
        
        headers = file_content.fieldnames
        headers.append("time_order")    
        writer = csv.DictWriter(f2, fieldnames = headers)
        writer.writeheader()
        time_list = []
        new_rows = []
        for row in file_content:
            time_list.append(row["time"])
            n+=1
            if float(row["time"])> maxi:
                maxi = float(row["time"])
            if float(row["time"])< mini:
                mini = float(row["time"])
            new_rows.append(row)
        time_list.sort()
        for row in new_rows:
            row.update({"time_order" : time_list.index(row["time"]) })
            writer.writerow(row)
        
        
        return ((maxi +mini)/n, mini)   

pas = get_time_path("fichier_filtre3.csv", "Fichie_filtre3.csv")


with open("Fichie_filtre3.csv") as f:
    file_content = csv.DictReader(f)
    for row in file_content:
        position = int(row["time_order"])
        tweet_id = row["id"]
        author = row["from__user_name"]
        text_tweet = row["text"]
        total_followers = row["sum_Rtfollowers"]
        G.add_node(tweet_id) #, author = author, text = text_tweet, nb_of_followers = total_followers)
        G.nodes[tweet_id]["viz"] = {"size":1.0 +float(sqrt(float(total_followers)))/(float(sqrt(float(total_followers)))-1)}   #FLOAT
        G.nodes[tweet_id]["viz"]["color"] = {"r": 200, "g": 0, "b" : 0, "a" : 1.0} #INT BUT FLOAT FOR A
        
        if position % 2 == 0:
            G.nodes[tweet_id]["viz"]["position"] = {"x": -(position//2)*pas[0] , "y": pas[1] + pas[0]*position , "z" : 0.0} 
        else:
            G.nodes[tweet_id]["viz"]["position"] = {"x": (position//2 + 1)*pas[0] , "y": pas[1] + pas[0]*position, "z" : 0.0}
        
        '''
        x += pas[0]
        if alter:
           #probleme coresspondance de temps entre le tweet et la 
            
            alter = False
        else :
            G.nodes[tweet_id]["viz"]["position"] = {"x": -x , "y" : pas[1] + pas[0]*n, "z" : 0.0}
            alter = True
        n +=1'''

nx.write_gexf(G, "graphe.gexf")