import random

print('VÍTEJ VE HŘE SIRKY')
print()
print('Hra pro 2 hráče...zadej 0')
print('Lehká obtížnost...zadej 1')
print('Střední obtížnost...zadej 2')
print('Těžká obtížnost...zadej 3')
x=24
obtiznost=int(input('Vyber obtížnost:'))

while obtiznost<0 or obtiznost>3:             
    obtiznost=int(input('Vyber obtížnost):'))
hrac=1
if obtiznost==0:    #hra pro 2 hráče
    print()
    print('Vybral sis hru pro 2 hráče')
    while x>0:      #hra končí na 0
        if hrac==1:    #hraje hráč 1
            print('Počet sirek je', x,'hraje hráč 1:')
            a=int(input('Odeber 1,2 nebo 3 sirky:'))
            while a<1 or a>3:   #číslo nesmí být menší než 1 a větší než 3
                print()
                print('Špatný počet')
                print('Počet sirek je', x,'hraje hráč 1:')
                a=int(input('Odeber 1,2 nebo 3 sirky:'))
                
        else :       #hraje druhý hráč
            print('Počet sirek je', x,'hraje hráč 2:')
            a=int(input('Odeber 1,2 nebo 3 sirky:'))
            while a<1 or a>3:
                print('Špatný počet')
                print('Počet sirek je', x,'hraje hráč 2:')
                a=int(input('Odeber 1,2 nebo 3 sirky:'))
        print()
        x=x-a     #vypíše se počet sirek
        
        if hrac==1:
            hrac=2        #střídání hráčů
        else:
            hrac=1

    if hrac==1:
        print('Poček sirek je 0')
        print('Hráč 2 prohrál')
    else :                           #vypíše se kdo prohrál
        print('Počet sirek je 0')
        print('Hráč 1 prohrál')




if obtiznost==1:        #lehká obtížnost
    print()
    print('Vybral sis lehkou obtížnost')
    while x>0:      #hra končí na 0
        if hrac==1:    #hraje hráč 1
            print('Počet sirek je', x,'jseš na řadě:')
            a=int(input('Odeber 1,2 nebo 3 sirky:'))
            while a<1 or a>3:   #číslo nesmí být menší než 1 a větší než 3
                print()
                print('Špatný počet')
                print('Počet sirek je', x,'jseš na řadě:')
                a=int(input('Odeber 1,2 nebo 3 sirky:'))
                
        else :       #hraje počítač
            print('Počet sirek je', x,'hraje počítač:') 
            if x==1 or x==2:
                a=1
            elif x==3:
                a=2
            elif x==4:
                a=3
            else:
                a=random.randint (1,3)
            print('Počítač odebral', a,)
        print()
        x=x-a     #vypíše se počet sirek
        
        if hrac==1:
            hrac=2       #střídání
        else:
            hrac=1

    if hrac==1:
        print('Poček sirek je 0')
        print('Počítač prohrál')
    else :                           #vypíše se kdo prohrál
        print('Počet sirek je 0')
        print('Prohrál jsi')




if obtiznost==2:    #střední obtížnost
    print()
    print('Vybral sis střední obtížnost')
    while x>0:      #hra končí na 0
        if hrac==1:    #hraje hráč 1
            print('Počet sirek je', x,'jseš na řadě:')
            a=int(input('Odeber 1,2 nebo 3 sirky:'))
            while a<1 or a>3:   #číslo nesmí být menší než 1 a větší než 3
                print()
                print('Špatný počet')
                print('Počet sirek je', x,'jseš na řadě:')
                a=int(input('Odeber 1,2 nebo 3 sirky:'))
                
        else :       #hraje počítač
            print('Počet sirek je', x,'hraje počítač:') 
            if x==1 or x==2 or x==6 or x==10:     #počítač hraje chytře
                a=1
            elif x==3 or x==7 or x==11:
                a=2
            elif x==4 or x==8 or x==12:
                a=3
            else:
                a=random.randint (1,3)
            print('Počítač odebral', a,)
        print()
        x=x-a     #vypíše se počet sirek
        
        if hrac==1:
            hrac=2       #střídání
        else:
            hrac=1

    if hrac==1:
        print('Poček sirek je 0')
        print('Počítač prohrál')
    else :                           #vypíše se kdo prohrál
        print('Počet sirek je 0')
        print('Prohrál jsi')




if obtiznost==3:    #těžká obtížnost
    print()
    print('Vybral sis těžkou obtížnost')
    while x>0:      #hra končí na 0
        if hrac==1:    #hraje hráč 1
            print('Počet sirek je', x,'jseš na řadě:')
            a=int(input('Odeber 1,2 nebo 3 sirky:'))
            while a<1 or a>3:   #číslo nesmí být menší než 1 a větší než 3
                print()
                print('Špatný počet')
                print('Počet sirek je', x,'jseš na řadě:')
                a=int(input('Odeber 1,2 nebo 3 sirky:'))
                
        else :       #hraje počítač
            print('Počet sirek je', x,'hraje počítač:') 
            if x==1 or x==2 or x==6 or x==10 or x==14 or x==18:     #počítač hraje chytře
                a=1
            elif x==3 or x==7 or x==11 or x==15 or x==19:
                a=2
            elif x==4 or x==8 or x==12 or x==16 or x==20:
                a=3
            else:
                a=random.randint (1,3)
            print('Počítač odebral', a,)
        print()
        x=x-a     #vypíše se počet sirek
        
        if hrac==1:
            hrac=2       #střídání
        else:
            hrac=1

    if hrac==1:
        print('Poček sirek je 0')
        print('Počítač prohrál')
    else :                           #vypíše se kdo prohrál
        print('Počet sirek je 0')
        print('Prohrál jsi')