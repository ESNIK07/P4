import math
FLAG = 1
LIMIT_P = 1000000
LIMIT_K = 1000000000

def verification(X, LIMIT_X):
    while X > LIMIT_X:
        print("The limit was exceeded")
        X = int(input("Enter a smaller value:"))
        if X < LIMIT_X:
            print("Thanks")
            break
    return X

def prime_numb(K):
    end = int(math.sqrt(K))
    start = int(math.sqrt(end))
    for n in range(start, end):
        if K % n == 0:
            A = n
            B = int(K/n)
            print(f"values {A} {B}")



if __name__ == "__main__":
    while FLAG == 1:
        P = int(input("Enter the value of P:"))
        P = verification(P,LIMIT_P)
        for x in range(P):
            K = int(input("Enter the value of K:"))
            K = verification(K, LIMIT_K)
            prime_numb(K)
        break


