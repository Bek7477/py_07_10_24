def full_list(n, lst):

    for i in range(n):
        qiymat = int(input(">>> "))
        lst.append(qiymat)
    return lst

def eng_katta_farq_topish(lst):
    max_diff = 0
    max_pair = 0

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] - lst[i] > max_diff:
                max_diff = lst[j] - lst[i]
                max_pair = (lst[i], lst[j])

    return f"{max_diff} ({max_pair[0]} va {max_pair[1]})"
    

lst = []
n = int(input("n = "))

full_list(n, lst)

print(eng_katta_farq_topish(lst))

