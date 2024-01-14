z,x,c,v = map(int,input().split())

if z<c :
    if x<c :
        print("nonintersecting")
    else :
        print("intersecting")
elif z==c :
    print("intersecting")
else :
    if v<z :
        print("nonintersecting")
    else :
        print("intersecting")