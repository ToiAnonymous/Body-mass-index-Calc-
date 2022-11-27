def main():
    import math
    print("-----------------Body Mass Index Calculator----------------")
    name = input("\nName of body : ")
    weight = int(input("\nWeight of body(km) : "))
    height = int(input("\nHeight of body(cm) : "))
    height/=100
    height_1 = height**2
    BMI = weight/height_1
    if BMI < 18.5:
        category = ("Underweight")
    elif ((BMI >= 18.5) and (BMI < 25.0)):
        category = ("Healthy")
    elif ((BMI >= 25.0) and (BMI < 30.0)):
        category = ("Overweight")
    elif ((BMI >= 30.0)):
        category = ("Obese")
    import csv
    fields = ["Name","Height(m)","Weight","BMI","Categorisation"]
    BMI = round(BMI , 2)
    rows = [[name,height,weight,BMI,category]]
    filename = "bmi.csv"
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerow(rows)  

main()    