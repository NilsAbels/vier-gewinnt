import tkinter as tk

def create_circle(x, y, r,canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill='red')




def Grid():



    root = tk.Tk()

    root.title("4 gewinnt")
    root.geometry("400x400")
    cv = tk.Canvas(root)
    cv.pack()
    allovals = [[0 for x in range(8)] for y in range(8)]
    x = 10
    y = 10
    for i in range(8):
        y = y + 25
        x = 10
        for j in range(8):
            x = x + 25
            allovals[i][j] = create_circle(x, y, 10, cv)
    cv.itemconfig(allovals[0][0], fill='black')
    print(allovals)

    root.mainloop()