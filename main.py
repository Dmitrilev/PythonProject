m,n = map(int,input().split())
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (m ==1 and n == 1) or (m==12 and m == 31):
    print("нихера")
elif n==b[0] or n==b[1] or n==b[2] or n==b[3] or n==b[4] or n==b[5] or n==b[6] or n==b[7] or n==b[8] or n==b[9] or n==b[10] or n==b[11]:
    print(f"{m:02}.{n-1} {m+1:02}.{int(n/n):02}")
elif n==1:
    print(f"{m-1:02}.{b[m - 2]} {m:02}.0{n + 1}")
else:
    print(F"{m:02}.{n - 1:02} {m:02}.{n + 1:02}")




