score = 0  

print(' هل الأرض كروية؟')

user_answer = input(' enter : tru  /  fls')

if user_answer == 'tru':


    print('correct')

    score += 5

    print('your score is:', score)

else:

    print('false')

print(' هل 5 أكبر من 10؟')

user_answer = input(' enter : tru  /  fls')

if user_answer == 'fls':


    print('correct')

    score += 5

    print('your score is:', score)

else:
    print('false')
    score -= 5
    print('your score is:', score)


print(' هل الجمل يُطلق عليه سفينة الصحراء')

user_answer = input(' enter : tru  /  fls')

if user_answer == 'tru':


    print('correct')

    score += 5

    print('your score is:', score)

else:

    print('false')
    score -= 5
    print('your score is:' , score)
if score >= 10:
    print('congratulation you won your score is:',score)
else:
    print('you lose!')

exit()
