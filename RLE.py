# 'AAABBBBCCDDD' -> 'A3B4C2D3'

# def rle(s: str):
#     def pack(s: str, cnt):
#         if cnt == 1:
#             ans.append(s)
#         else:
#             ans.append(s + f'{cnt}')
#     cnt = -1
#     ans = []
#     lassymbol = s[0]
#     for i in range(len(s)):
#         cnt += 1
#         if s[i] != lassymbol:
#             pack(lassymbol, cnt)
#             cnt = 0
#             lassymbol = s[i]
        
#     ans.append(lassymbol + f'{cnt+1}')
#     return ''.join(ans)

# print(rle('ABBBBCCDDDFFFFFFFF'))
def compress(chars: list[str]) -> int:
    write = 0  # Pointer to write the compressed string
    read = 0   # Pointer to read through the original array
        
    while read < len(chars):
        char = chars[read]
        count = 0
            
            # Count the number of occurrences of the current character
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
            
            # Write the character to the write position
        chars[write] = char
        write += 1
            
            # If the character count is more than 1, write the count as well
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
        
        return write
print(compress('AAABBBBCCDDD'))