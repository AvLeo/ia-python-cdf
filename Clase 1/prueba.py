# laberinto=[["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#                 ["#", " ", "#", "#", "#", "#", "#", "#", " ", "#"],
#                 ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
#                 ["#", " ", "#", " ", "#", "#", "#", "#", " ", "#"],
#                 ["#", " ", "#", " ", "#", " ", " ", " ", " ", "#"],
#                 ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
#                 ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
#                 ["#", "S", " ", " ", "#", " ", " ", " ", " ", "#"],
#                 ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

# def ejercicio10(laberinto):
#     final = ()
#     #completar y borrar pass
#     for i in range(len(laberinto)):
#         print(i)
#         for j in range(i):
#             print(i, j)
#             if laberinto[i][j] == "S":
#                final.append(i)
#                final.append(j)
#                print(final)

# ejercicio10(laberinto)

estado = 5

list = [1 ,2 ,3 ,4 ,5]

print(list)

list.remove(list[0])

print(list)

print(list.count(estado))