n1 = 0 
n2 = 1
nextTerm = 0
limit = 50
fibonacci_series = []
while (n1 < 50 ):
    fibonacci_series.append(n1)
    nextTerm = n1 + n2
    n1 = n2
    n2 = nextTerm
print("fibonacci_series::", fibonacci_series)
n = 50
fibonacci_series_excluded = []
for i in range(n):
    if i not in fibonacci_series:
        fibonacci_series_excluded.append(i)
print("fibonacci_series_excluded::", fibonacci_series_excluded)
