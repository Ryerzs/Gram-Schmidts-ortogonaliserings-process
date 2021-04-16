
def innerProduct(u,v):
    prod = 0
    for i in range(len(v)):
        prod += u[i]*v[i]
    return prod

def scale(a,u):
    return [a*v for v in u]

def subtract(u,v):
    return [u[i]-v[i] for i in range(len(u))]

def round_vector(u,p):
    return [round(v,p) for v in u]

def linearlyDependant(V):
    r = range(len(V))
    for i in r:
        length = innerProduct(V[i],V[i])
        for j in r:
            if i!=j and innerProduct(V[i],V[j]) == length and innerProduct(V[j],V[j]) == length:
                return True
    return False

def Gram_Schmidt(V):
    e_p = []
    for v in V:
        if len(e_p) == 0:
            e_p.append(v)
        else:
            e_ip = v
            for e in e_p:
                proj = scale(innerProduct(v, e)/innerProduct(e, e),e)
                e_ip = subtract(e_ip, proj)
            e_p.append(e_ip)
    return e_p

def loadtxt(path):
    file = open(path, mode='r', encoding='utf-8')
    return [[int(n) for n in line.split()] for line in file]

def row_echelon(m):
    newM = []
    if len(m)==0:
        return []
    elif(len(m[0])==0):
        return []
    l = len(m[0])
    rows = len(m)
    base = None
    for j in range(rows):
        if m[j][0] != 0:
            base = j
            break
    if base == None:
        return removeColumn(m,0)
    a = m[base][0]
    for j in range(rows):
        if j != base:
            factor = m[j][0]/a
            for i in range(l):
                m[j][i] -= factor*m[base][i]
    return m

def removeColumn(m, c):
    out = []
    l = len(m[0])
    rows = len(m)
    for j in range(rows):
        row = []
        for i in range(l):
            if i != c:
                row.append(m[j][i])
        out.append(row)
    return out

def combine(row, col, meat, i, j):
    out = []
    for y in range(len(meat)):
        newRow = []
        for x in range(len(meat[0])):
            if x == i:
                newRow.append(col[y])
                newRow.append(meat[x][y])
            else:
                newRow.append(meat[x][y])

def main():
    vectors = loadtxt("vectors.txt")
    if linearlyDependant(vectors):
        print("The vectors are linearly dependant")
        return
    e_p = Gram_Schmidt(vectors)
    print(row_echelon(vectors))
    for e in e_p:
        print(round_vector(e,3))
main()