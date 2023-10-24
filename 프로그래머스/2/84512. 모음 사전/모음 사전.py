from itertools import product
def solution(word):

    vowels = ['A', 'E', 'I', 'O', 'U']

    # 중복순열 계산
    #sorted_vowels = sorted(list(product(vowels, repeat=1)) +
     #                      list(product(vowels, repeat=2)) +
      #                     list(product(vowels, repeat=3)) +
       #                    list(product(vowels, repeat=4)) +
        #                   list(product(vowels, repeat=5)))
        
    sorted_vowels = []
    for i in range(1,6):
        sorted_vowels += list(product(vowels,repeat = i))
        
    # 정리된 값들
    cleaned_values = []
    for i in sorted_vowels:
        cleaned_values.append(''.join(i))
    # cleaned_values = [''.join(item) for item in sorted_vowels]
    cleaned_values.sort()
    
    return cleaned_values.index(word)+1