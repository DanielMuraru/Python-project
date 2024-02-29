
def cmp(a, b, reverse):
    if reverse == False:
        return a>b
    if reverse == True:
        return a<b


def cmpnou21 (v,a,b,reverse):
    if v[a].get_nume()==v[b].get_nume():
            if reverse==False:
                return v[a].get_media()>v[b].get_media()
            if reverse==True:
                return v[a].get_media() < v[b].get_media()

    if reverse == False:
        return v[a].get_nume()>v[b].get_nume()
    if reverse == True:
        return v[a].get_nume()<v[b].get_nume()


def cmpnou (v,key,li,ls,reverse):
    if key[0][v[li]]==v[ls].get_nume():
            if reverse==False:
                return v[a].get_media()>v[b].get_media()
            if reverse==True:
                return v[a].get_media() < v[b].get_media()

    if reverse == False:
        return v[a].get_nume()>v[b].get_nume()
    if reverse == True:
        return v[a].get_nume()<v[b].get_nume()

def poz(v, li, ls, comparator, key, reverse):
    ok = 0
    while li < ls:
        # if v[li].get_nume() > v[ls].get_nume():
        #if comparator(v[li].get_nume(),v[ls].get_nume(), reverse) == True:
        #if comparator(getattr(v[li],key[0])(),v[ls].get_nume(), reverse) == True:
        if comparator(v,key,li,ls,reverse) == True:
            v[li], v[ls] = v[ls], v[li]
            if ok != 0:
                ok = 0
            else:
                ok = 1

        if ok == 0:
            li = li + 1
        else:
            ls = ls - 1
    return li


def quicksort(v, li, ls, comparator,key, reverse):
    if li < ls:
        p = poz(v, li, ls, comparator,key, reverse)
        quicksort(v, li, p - 1, comparator,key, reverse)
        quicksort(v, p + 1, ls, comparator,key,reverse)


def gnomesort(lista, comparator,key,reverse):
    poz = 0
    while poz < len(lista):
        # if poz==0 or lista[poz].get_nume()>lista[poz-1].get_nume()
        if poz == 0 or cmp(getattr(lista[poz],key[0])(), getattr(lista[poz - 1],key[0])(),reverse) == True:
            poz = poz + 1
        elif cmp(getattr(lista[poz],key[0])(), getattr(lista[poz - 1],key[0])(),not(reverse)):
            lista[poz], lista[poz - 1] = lista[poz - 1], lista[poz]
            poz = poz - 1

        # if lista[poz].get_nume()==lista[poz-1].get_nume()
        # if lista[poz].get_media()<lista[poz-1].get_media()
        elif comparator(getattr(lista[poz],key[0])(), getattr(lista[poz - 1],key[0])(),reverse) == False:
            if comparator(getattr(lista[poz],key[1])(), getattr(lista[poz - 1],key[1])(),not (reverse)) :
                lista[poz], lista[poz - 1] = lista[poz - 1], lista[poz]
                poz = poz - 1
            else:
                poz = poz + 1

def sortare(rez, metoda,comparator, key, reverse):
    if metoda == "quick_sort":
        quicksort(rez, 0, len(rez) - 1,comparator ,key, reverse)
    elif metoda == "gnome_sort":
        gnomesort(rez, comparator,key,reverse)
