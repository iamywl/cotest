T = int(input())
def A(arg_W, P):
    return arg_W*P
def B(arg_W, Q, R, S):
    if W <= R:
        return Q
    else:
        return Q + S * (arg_W - R)

for tc in range(1,T+1):
    P, Q, R, S, W = map(int, input().split())
    a = A(W,P)
    b = B(W,Q,R,S)
    res = min(a, b)

    print(f'#{tc} {res}')