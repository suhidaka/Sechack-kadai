身長 = float(input("身長をメートル単位で入力してください（例: 1.68）: "))
体重 = float(input("体重をkg単位で入力してください（例: 67）: "))
print('BMIが22になる体重は以下になります。')
while True:
    BMI=体重/(身長*身長)
    print(f'{体重}kg' , f'BMI:{BMI:.2f}')
    if BMI<22:
        break
    体重=体重-1
print(f'あなたの現在のBMIは{BMI:.2f}です！')
if BMI < 18.5:
    print("やせすぎです 健康に注意しましょう！")
elif BMI < 25:
    print("標準体重です 維持していきましょう")
else:
    print("肥満の可能性があります 運動をして健康に行きましょう")
