import csv


def is_text_unique(tweets):
    unique = set()
    for tweet in tweets:
        if tweet['text'] not in unique:
            unique.add(tweet['text'])
        else:
            print("not unique")
            return False
    return True


def filtrage_text(tweet):
    c=0
    for x in tweet:
        if x != "#":
            c +=1
        else:
            return tweet[c:]
            break

def process_and_write_tweets(fichier):
    tweets_o = []
    rt_o = []
    with open(fichier) as file, open("fichier_filtre.csv", "w") as filtrated_file:
        file_content = csv.DictReader(file)
        field = file_content.fieldnames
        field.append("sum_followers_of_retweeters")
        writer = csv.DictWriter(filtrated_file, fieldnames = field)
        writer.writeheader()
        for row in file_content:
            if row["retweeted_user_name"]:
                rt_o.append(row)
            else:
                tweets_o.append(row)
                
        for tweet in tweets_o:
            S = 0
            for rt in rt_o:
                if filtrage_text(rt["text"]) == tweet["text"]:
                    print("ok")
                    S += int(rt["from__user_followercount"])
            tweet.update({"sum_followers_of_retweeters" : S})
            writer.writerow(tweet)
    return (tweets_o,rt_o)

distinction_rt_tweets("lancet_smallfile.csv")






    
    