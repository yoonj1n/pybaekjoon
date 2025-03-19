score = input()
scores = {'A':4.3, 'B':3.3, 'C':2.3, 'D':1.3, 'F':0.0}
pm = {'+':0, '0':0.3, '-':0.6}
print(round(scores[score[0]]-pm[score[1]],2)) if score != 'F' else print(scores[score])
