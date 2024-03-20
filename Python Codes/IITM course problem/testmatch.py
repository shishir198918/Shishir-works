def userinput():
    d={"A1":0,"AW1":0,"A2":0,"AW2":0,"B1":0,"BW1":0,"B2":0,"BW2":0}
    for i in d:
        while(d[i]<=0):
            d[i]=int(input())
    return d

def main():
    score=userinput()
    teamA=score["A1"]+score["A2"]
    teamWA=score["AW1"]+score["AW2"]
    teamB=score["B1"]+score["B2"]
    teamWB=score["BW1"]+score["BW2"]
    if teamA>teamB:
        if teamWB==20:
            print("Team A")
        else:
            print("DRAW")
    elif teamA==teamB:
        print("TIE")

    else:
        if teamWA==20:
            print("Team B")
        else:
            print("Draw")
        
        
main()        
