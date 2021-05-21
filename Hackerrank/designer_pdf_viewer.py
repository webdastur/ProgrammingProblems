def designerPdfViewer(h: list[int], word: str):
    higher_letter = 0
    for i in word.strip():
        higher_letter = max(higher_letter, h[ord(i) - 97])
    return higher_letter * len(word.strip())


print(designerPdfViewer(
    [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    'abc'
))
