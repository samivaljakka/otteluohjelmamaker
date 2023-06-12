import string
import ottelu

def creatematchlist(ottelulista, joukkuelista):
    jklm = 0
    jklm = int(input("Anna joukkueiden lukumäärä: "))
    joukkueet = [chr(chNum) for chNum in list(range(ord('A'),ord('z')+1))]
    for i in range(jklm):
        joukkuelista.append(joukkueet[i])
    print(joukkuelista)

    otlm=0
    a=0
    b=a+1
    while (a < jklm ):
        while (b < jklm ):
            otlm=otlm+1
            print(joukkuelista[a], joukkuelista[b])
            newmatch = ottelu.Ottelu("a", "B", otlm)
            ottelulista.append(newmatch)
            print(newmatch.joukkue1, newmatch.joukkue2, newmatch.joukkue2)
            b=b+1
            print(otlm)
        a=a+1
        b=a+1
    print(ottelulista)


    


    return None
