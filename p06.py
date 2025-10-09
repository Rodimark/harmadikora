import turtle
import p05Pont

ablak = turtle.Screen()
ablak.title("Pontverseny")
ablak.bgcolor("black")

def kilepes():
    ablak.bye()

pont1 = p05Pont.MozgoPont("cyan", -200,23,15)
pont2 = p05Pont.MozgoPont("magenta", 150, 23, 19)
pont3 = p05Pont.MozgoPont("mustard", 200, 150, 15)

ablak.listen()

ablak.onkey(kilepes, "Escape")
ablak.onkey(pont1.inditas, "d")
ablak.onkey(pont2.inditas, "k")
ablak.onkey(pont3.inditas, "l")