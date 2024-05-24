#Procedure de la sign :
def Sign(N):
    if N > 0:
        print("Strictement Positive!")
    elif N < 0:
        print("Strictement Negetive!")
    elif N == 0:
        print("Null!")
#Demande:     
N = float(input("Entrer un Nombre : "))
#Declaration de prodcedure:
Sign(N)