



def findMatchTrue(nombre1,nombre2):
    
    tv=0
    rv = 0
    uv = 0
    ev = 0

    totalTrue=0

    name1List = list(nombre1)
    name2List = list(nombre2)


    for i in range(len(name1List)):
         if name1List[i] == 't':
              tv=tv+1
         if name1List[i] == 'r':
              rv=rv+1
         if name1List[i] == 'u':
              uv=uv+1
         if name1List[i] == 'e':
              ev=ev+1
    
    for i in range(len(name2List)):
         if name2List[i] == 't':
              tv=tv+1
         if name2List[i] == 'r':
              rv=rv+1
         if name2List[i] == 'u':
              uv=uv+1
         if name2List[i] == 'e':
              ev=ev+1

    totalTrue=tv+rv+uv+ev


    
    lv=0
    ov = 0
    vv = 0
    ev = 0

    totalLove=0


    for i in range(len(name1List)):
         if name1List[i] == 'l':
              lv=lv+1
         if name1List[i] == 'o':
              ov=ov+1
         if name1List[i] == 'v':
              vv=vv+1
         if name1List[i] == 'e':
              ev=ev+1
    
    for i in range(len(name2List)):
         if name2List[i] == 'l':
              lv=lv+1
         if name2List[i] == 'o':
              ov=ov+1
         if name2List[i] == 'v':
              vv=vv+1
         if name2List[i] == 'e':
              ev=ev+1

    totalLove= lv+ov+vv+ev


    print("TotalLove",str(totalTrue)+str(totalLove))
        

findMatchTrue("Angela Yu","Jack Bauer")