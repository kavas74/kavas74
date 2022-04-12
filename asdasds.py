import random



def nevelo(szo):
    maganhangzok = "aáeéiíoóöőuúüű"
    if szo[0].lower() in maganhangzok:
        return("Az")
    else:
        return("A")
    
def jelzo():
    return(random.choice(["piros","nagy","könnyed"]))



for i in range(1,4):
    fonev = input(f"{i}. főnév: ")

    print(f"{nevelo(fonev)} {fonev} {jelzo()}.")
