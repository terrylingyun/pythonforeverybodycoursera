score = input('What is your score? (Ranging from 0.0 to 1.0)')
score = float(score)
if score > 1.0 :
    newscore = 'Error'
elif score < 0.0 :
    newscore = 'Error'
elif score >= 0.9 :
    newscore = 'A'
elif score >= 0.8 :
    newscore = 'B'
elif score >= 0.7 :
    newscore = 'C'
elif score >= 0.6 :
    newscore = 'D'
else :
    newscore = 'F'
print(newscore)
