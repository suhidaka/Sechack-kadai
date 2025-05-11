身長 = float(input("身長をメートル単位で入力してください（例: 1.68）: "))
体重 = float(input("\n体重をkg単位で入力してください（例: 67）: "))
元の体重 = 体重

現在のBMI = 元の体重 / (身長 * 身長)
print(f'\nあなたの現在のBMIは {現在のBMI:.2f} です！')


print('\nBMIが22になる体重は以下になります。')
while True:
    BMI=体重/(身長*身長)
    print(f'{体重}kg' , f'BMI:{BMI:.2f}')
    if BMI<22:
        break
    体重=体重-1


if BMI < 18.5:
    print("やせすぎです 健康に注意しましょう！")
elif BMI < 25:
    print("\n標準体重です 維持していきましょう！")
else:
    print("肥満の可能性があります 運動をして健康に行きましょう！")
