kaufpreis = int(input("Was ist der Kaufpreis?"))
groschen = int(input("Wie viel haben Sie dem Kassierer gegeben?"))
restgeld = groschen - kaufpreis

if restgeld > 0:
    print(restgeld, " € müssen Sie zurückbekommen.")
elif restgeld == 0:
    print("Sie haben passend bezahlt und erhalten kein Restgeld")
else:
    print("Sie haben zu wenig bezahlt und müssen noch ", restgeld*-1, " € bezahlen")