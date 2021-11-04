from typing import List


def cheapest_flight(costs: List, a: str, b: str) -> int:
    # your code here
    q = []
    k = 0
    c = [list(j) for j in costs]
    for i in costs:
        i[0],i[1] = i[1],i[0]
        c.append(i)
    for i in c:
        if a in i[0] and b in i[1]:
            q.append(i[2])
        elif a in i[0]:
            k += i[2]
            for j in c:
                if i[1] in j[0] and b in j[1]:
                    k += j[2]
                    q.append(k)
                    return min(q)
    return 0


