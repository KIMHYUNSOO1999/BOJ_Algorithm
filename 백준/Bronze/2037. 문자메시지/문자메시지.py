N, M = map(int, input().split())
S = input()

pad = {
    1: [' '],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z']
}

result = 0
prev_key = -1

for ch in S:
    for key, chars in pad.items():
        if ch in chars:
            press_count = chars.index(ch) + 1
            if key == prev_key and ch != ' ':
                result += M
            result += N * press_count
            prev_key = key
            break

print(result)
