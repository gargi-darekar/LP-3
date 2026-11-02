import heapq
from collections import Counter

def huffman_encoding(text):
    freq = Counter(text)
    heap = [[frequency, [char, ""]] 
            for char, frequency in freq.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        char = heap[0][1][0]
        return {char: "0"}

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for pair in left[1:]:
            pair[1] = "0" + pair[1]

        for pair in right[1:]:
            pair[1] = "1" + pair[1]

        heapq.heappush(heap, [
            left[0] + right[0]
        ] + left[1:] + right[1:])

    return dict(heap[0][1:])

text = input("Enter a string: ")
codes = huffman_encoding(text)

print("\nHuffman Codes:")
for char, code in sorted(codes.items()):
    print(char, ":", code)

encoded = "".join(codes[char] for char in text)
print("\nEncoded String:", encoded)

