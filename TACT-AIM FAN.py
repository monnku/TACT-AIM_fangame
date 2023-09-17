import pygame as pg, sys, iroiro as ir, numpy as np
pg.init()
def main():
    global myrect, stage
    screen = pg.display.set_mode((1545, 810))
    pg.display.set_caption("TACT-AIMファンゲーム")
    myrect = pg.Rect(747.5, 380, 50, 50)
    cat = pg.image.load("cat.png")
    cat = pg.transform.scale(cat, (50, 60))
    dire = 0
    
    def key(key, x_or_y, henka):
        global myrect, stage
        if key:
            if x_or_y == "x":
                myrect.x += henka
                if myrect.collidelist(stage) != -1:
                    myrect.x -= henka
            if x_or_y == "y":
                myrect.y += henka
                if myrect.collidelist(stage) != -1:
                    myrect.y -= henka
    stage = [pg.Rect(707.5, 100, 130, 130), pg.Rect(707.5, 580, 130, 130), pg.Rect(0, 0, 1545, 50), pg.Rect(1495, 0, 50, 810), pg.Rect(0, 0, 50, 810),
             pg.Rect(0, 760, 1545, 50), pg.Rect(0, 380, 200, 50), pg.Rect(1345, 380, 200, 50), pg.Rect(500, 0, 50, 300), pg.Rect(995, 0, 50, 300),
             pg.Rect(500, 510, 50, 300), pg.Rect(995, 510, 50, 300), pg.Rect(100, 100, 350, 50), pg.Rect(100, 200, 350, 50), pg.Rect(100, 660, 350, 50),
             pg.Rect(100, 560, 350, 50), pg.Rect(1095, 100, 350, 50), pg.Rect(1095, 200, 350, 50), pg.Rect(1095, 560, 350, 50), pg.Rect(1095, 660, 350, 50),
             pg.Rect(300, 300, 150, 50), pg.Rect(300, 460, 150, 50), pg.Rect(1095, 300, 150, 50), pg.Rect(1095, 460, 150, 50), pg.Rect(600, 305, 50, 200), pg.Rect(895, 305, 50, 200)]
    ballets = []
    ballets_x = []
    ballets_y = []
    reload = 0
    
    while True:
        screen.fill("grey")
        key(ir.k.right() or ir.k.d(), "x", 1)
        key(ir.k.left() or ir.k.a(), "x", -1)
        key(ir.k.up() or ir.k.w(), "y", -1)
        key(ir.k.down() or ir.k.s(), "y", 1)
        for i in stage:
            pg.draw.rect(screen, "black", i)
        msx, msy = pg.mouse.get_pos()
        delx = msx - myrect.x
        dely = msy - myrect.y
        if dely == 0:
            if delx < 0:
                dire = -90
            else:
                dire = 90
        elif dely < 0:
            dire = np.arctan(delx / dely) * 60 + 180
        else:
            dire = np.arctan(delx / dely) * 60
        rotatedcat = pg.transform.rotate(cat, dire - 90)
        drawrect = myrect
        drawrect.center = myrect.x+myrect.width/2, myrect.y+myrect.height/2
        if pg.mouse.get_pressed()[0]:
            if reload <= 0:
                ballets.append(pg.Rect(myrect.x+myrect.width/2, myrect.y+myrect.height/2, 10, 10))
                ballets_x.append(delx / 50)
                ballets_y.append(dely / 50)
                reload = 100
        reload -= 1
        b = 0
        for a in range(len(ballets)):
            i = a + b
            pg.draw.rect(screen, "black", ballets[i])
            ballets[i].x += ballets_x[i]
            ballets[i].y += ballets_y[i]
            if ballets[i].collidelist(stage) != -1:
                del ballets[i]
                del ballets_x[i]
                del ballets_y[i]
                b -= 1
        screen.blit(rotatedcat, drawrect)
        pg.display.update()
        ir.sys_exit(ir.pg_quit())

if __name__ == "__main__":
    if input("passcord:") == "TACT-AIM":
        main()
