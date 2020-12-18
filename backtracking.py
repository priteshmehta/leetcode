def permute(list, s):
    if list == 1:
        return s
    else:
        return [(y,x)
                for y in permute(1, s)
                for x in permute(list - 1, s)
                ]

#print(permute(1, ["a","b","c"]))
#print(permute(2, ["a","b","c"]))

def my_permute(list, s):
    if list == 1:
        return s
    else:
        #a = [ y for y in permute(1, s)]
        a = [ (x,y,z) 
            for x in ["x1","x2","x3"]
            for y in ["y1","y2","y3"]
            for z in ["z1","z2","z3"]
        ]
        return a

def permute3(list_size, s):
    a = []
    if list_size == 1:
        return s
    else:
        for y in permute(1, s):
            for x in permute(1, s[1:]):
                for z in permute(1, s[2:]):
                    if x + y + z == 0:
                        if (x,y,z) not in a:
                            a.append((x, y, z))

        return list(set(a))


ans = permute3(3, [-1, 0, 1, 2, -1, -4])
print(ans)
#[-1, 0, 1, 2, -1, -4]
