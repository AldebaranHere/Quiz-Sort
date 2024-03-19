quiz_list = [
        ["quiz_name_1", number_of_questions_1],
        ["quiz_name_2", number_of_questions_2],
        ["quiz_name_3", number_of_questions_3],
        ["quiz_name_4", number_of_questions_4],
        ["quiz_name_5", number_of_questions_5]
    ]
    
sorted_list=sorted(quiz_list, key=lambda a: a[1])  

for a in range(len(sorted_list)):
    print(str(a+1)+". " + sorted_list[a][0]+", "+str(sorted_list[a][1]))
