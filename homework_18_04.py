def z_func(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

curr_ind = 0
indexes = []
s = ""
for word in input().split():
    if curr_ind > 0:
        indexes.append(curr_ind)
    s = s + word + '#'
    curr_ind += len(word) + 1
end_index = min([z_func(s)[i] for i in indexes])
print(s[:end_index:])
      
