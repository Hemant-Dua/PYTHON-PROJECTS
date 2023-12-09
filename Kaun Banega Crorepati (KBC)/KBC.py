print("------------------WELCOME TO KAUN BANEGA CROREPATI---------------------")

#list of questions
questions=["What is our National Fruit?\nA) Mango \nB) Apple \nC) Banana \nD) Strawberry","How many Wonders are there in the World? \nA) 5 \nB) 6 \nC) 7 \nD) 69","What is the formula of Salt? \nA) CuSO4 \nB) NaCl \nC) NH3 \nD) HCl","Seismometer is used to measure? \nA) Earthquakes \nB) Rainfall \nC) Ocean depth \nD) Sound intensity","Which one of following is flightless bird? \nA) Swan \nB) Duck \nC) Hen \nD) Emu","Which country is the largest producer of platinum? \nA) America \nB) Italy \nC) Canada \nD) China","Honey has large percentage of? \nA) Water \nB) Glucose \nC) Starch \nD) Sucrose","Allergy is treated by? \nA) Antibiotic \nB) Surgery \nC) Antihistamine \nD) None of the Above","Biological system that removes unnecessary materials from the body is known as? \nA) Circulatory System \nB) Excretory System \nC) Respiratory System \nD) Muscular System","Camel uses its hump for? \nA) Temperature Regulation \nB) Storing Water \nC) Storing Fat \nD) None of the Above"]

#prize amounts
prizes=["0","10,00,000","20,00,000","30,00,000","40,00,000","50,00,000","60,00,000","70,00,000","80,00,000","90,00,000","1,00,00,000"]

#correct answers respective to their questions
answers=["a","c","b","a","d","c","b","c","b","c"]

for i in range(len(questions)):

    print("Q",i+1,questions[i])                             #Question no.=(i+1) Questions=Questions[i]
    x=str(input())                                          #taking input in x

    if x.lower()==answers[i]:
        print(f"It's Correct... You won {prizes[i+1]} Ruppees...")

    else:
        print(f"ALAS!!! It's Wrong... you end up with {prizes[i]} Ruppees...")
        break