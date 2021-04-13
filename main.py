
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

def main():
    vectors = loadtxt("vectors.txt")
    if linearlyDependant(vectors):
        print("The vectors are linearly dependant")
        return
    e_p = Gram_Schmidt(vectors)
    for e in e_p:
        print(round_vector(e,3))
main()