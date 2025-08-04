import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

package, each = 1000, 1000
for _ in range(m):
    tmp1, tmp2 = map(int, input().strip().split())

    if package>tmp1:
        package = tmp1

    if each>tmp2:
        each = tmp2

t1 = n//6 * package + n%6 * each
t2 = ((n//6)+1) * package
t3 = n * each  

print(min(t1,t2,t3))