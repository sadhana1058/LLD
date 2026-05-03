def flag_t(transactions):
    h = {}
    res = []
    for t in transactions:
        t = t.split(",")
        flag = False
        if t[0] in h:
            print(h)
            pass
            for ttt in h[t[0]]:
                time,city=ttt[0],ttt[1]
                print(time,city,type(ttt))
                if city!=t[2] and int(t[1])-time<=50:
                    res.append(t[0]+","+str(time)+","+city)
            flag=True
                    
        else:
            h[t[0]]=[]
            h[t[0]].append([int(t[1]),t[2]])
        if flag:
            res.append(t[0]+","+str(t[1])+","+t[2])
    print(res)
ts = ['Alice,50,sf','George,50,sf','Alice,60,ny']
flag_t(ts)