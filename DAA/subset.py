def find_subsets(S, d):
    result = []
    def backtrack(start, subset, current_sum):
        if current_sum == d:
            result.append(subset[:])
            return
        if current_sum > d:
            return
        for i in range(start, len(S)):
            subset.append(S[i])
            backtrack(i + 1, subset, current_sum + S[i])
            subset.pop()
    backtrack(0, [], 0)
    return result

S = [1, 3, 4, 5]
d = 8
solutions = find_subsets(S, d)
if solutions:
    print(f"Subsets of {S} whose sum is = {d} are: ")
    for subset in solutions:
        print(subset)
else:
    print(f"No Subsets of {S} whose sum is = {d}")
