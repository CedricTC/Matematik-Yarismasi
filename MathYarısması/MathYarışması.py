import turtle
import random
import time

def draw_border():
    border_pen = turtle.Turtle()
    border_pen.penup()
    border_pen.speed(0)
    border_pen.goto(-250, 250)
    border_pen.pendown()
    border_pen.hideturtle()
    border_pen.color("red")
    border_pen.width(5)
    for _ in range(4):
        border_pen.forward(500)
        border_pen.right(90)

def main():
    win = turtle.Screen()
    win.bgcolor("black")
    win.title("Matematik Soruları")
    win.screensize(700, 700)

    draw_border()

    question_turtle = turtle.Turtle()
    question_turtle.penup()
    question_turtle.speed(1)
    question_turtle.goto(0, 100)
    question_turtle.penup()
    question_turtle.hideturtle()
    question_turtle.color("red")

    result_turtle = turtle.Turtle()
    result_turtle.penup()
    result_turtle.speed(0)
    result_turtle.goto(0, -100)
    result_turtle.penup()
    result_turtle.hideturtle()
    result_turtle.color("red")

    dogrusayisi_turtle = turtle.Turtle()
    dogrusayisi_turtle.penup()
    dogrusayisi_turtle.speed(0)
    dogrusayisi_turtle.goto(0,0)
    dogrusayisi_turtle.penup()
    dogrusayisi_turtle.hideturtle()
    dogrusayisi_turtle.color("red")

    toplamsüre_turtle = turtle.Turtle()
    toplamsüre_turtle.penup()
    toplamsüre_turtle.speed(0)
    toplamsüre_turtle.goto(0,-200)
    toplamsüre_turtle.penup()
    toplamsüre_turtle.hideturtle()
    toplamsüre_turtle.color("red")    

    i = 0
    correct_count = 0
    toplam_sure = 0
   

    while i < 5:
        start_time = time.time()  # Soru başlangıç zamanı

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*", "/"])
        question = f"{num1} {operator} {num2}"
        answer = eval(question)

        question_turtle.write(question, align="center", font=("Courier", 30, "normal"))
        user_answer = turtle.textinput("Cevap", "Sonucu Yazın")

        end_time = time.time()  # Soru cevaplama bitiş zamanı
        soru_suresi = end_time - start_time  # Soru çözme süresi
        toplam_sure += soru_suresi  # Toplam süreyi güncelle

        result_turtle.clear()

        if user_answer and float(user_answer) == answer:
            correct_count += 1
            result_turtle.write("Aferin", align="center", font=("Courier", 30, "normal"))
        else:
            result_turtle.write("Yanlış", align="center", font=("Courier", 30, "normal"))

        question_turtle.clear()
        result_turtle.clear()
        i += 1

    question_turtle.write("Doğru Sayınız", align="center", font=("Courier", 30, "normal"))
    dogrusayisi_turtle.write(f"{correct_count}", align="center", font=("Courier", 30, "normal"))

    toplamsüre_turtle.write(f"Süre: {toplam_sure:.2f} saniye", align="center", font=("Courier", 30, "normal"))

    time.sleep(3)
    win.mainloop()

main()
