def rightAnswer(Ans_Den,Ans_Ira):
    if (Ans_Den==1 and Ans_Den==Ans_Ira) or (Ans_Den!=1 and Ans_Ira!=1):
        return 'YES'
    else:
        return 'NO'

Ans_Den = int(input())
Ans_Ira = int(input())
print(rightAnswer(Ans_Den,Ans_Ira))