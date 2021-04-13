
def innerProduct(u,v):
    prod = 0
    for i in range(len(v)):
        prod += u[i]*v[i]
    return prod

def scale(a,u):
    return [a*v for v in u]

def subtract(u,v):
    u_p = []
    for i in range(len(v)):
        u_p.append(u[i]-v[i])
    return u_p

def round_vector(u,p):
    return [round(v,p) for v in u]

def linearlyDependant(V):
    l = len(V)
    for i in range(l):
        length = innerProduct(V[i],V[i])
        for j in range(l):
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

def main():
    v1 = [1,1,1,1]
    v2 = [0,1,1,1]
    v3 = [0,0,1,1]
    vectors  = [v1,v2,v3]
    if linearlyDependant(vectors):
        print("The vectors are linearly dependant")
        return
    e_p = Gram_Schmidt(vectors)
    for e in e_p:
        print(round_vector(e,3))
main()