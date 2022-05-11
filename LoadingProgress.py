import math
from colorama import Fore



def loadingProgress(progress, total):

    pourcentage = progress/total * 50 #pour que le chargement reste visible dans une petite console
    barreProgression = ""
    loaded = "="*int(pourcentage)
    toDo = "-"*(50-int(pourcentage))

    barreProgression = "[" + loaded + toDo + "]"
    
    if progress!=total:
        print( Fore.YELLOW +  f"\r{barreProgression}" + Fore.RESET + f"   {pourcentage*2:.1f} %", end="")

    else:
        print( Fore.GREEN + f"\r{barreProgression}" + Fore.RESET + f"   {pourcentage*2:.1f} %")
        Fore.RESET


def main():

    L = [x for x in range(10000,12000)]
    for i,x in enumerate(L):
        ans = math.factorial(x)
        loadingProgress(i+1,len(L))


if __name__ == '__main__':
    main()