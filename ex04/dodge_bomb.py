import pygame as pg
import random
import sys

def henka(x):
   if x > 1000:
    bomb3_sfc = pg.Surface((100, 100))
    return bomb3_sfc

def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate
def main():
    clock =pg.time.Clock()
    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1000, 600))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()
    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 



    #bomb3_sfc = pg.Surface((40, 40)) # 正方形の空のSurface
    #bomb3_sfc.set_colorkey((0, 0, 0))
    #pg.draw.circle(bomb3_sfc, (255, 0, 0), (20, 20), 10)
    #bomb3_rct = bomb3_sfc.get_rect()
    #bomb3_rct.centerx = random.randint(0, scrn_rct.width)
    #bomb3_rct.centery = random.randint(0, scrn_rct.height)
    #scrn_sfc.blit(bomb3_sfc, bomb3_rct) 
    #vx3, vy3 = +1, +1    

    bomb2_sfc = pg.Surface((100, 100)) # 正方形の空のSurface
    bomb2_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc, (255, 0, 0), (50, 50), 10)
    pg.draw.circle(bomb2_sfc, (191, 0, 0), (50,50), 20)
    pg.draw.circle(bomb2_sfc, (127, 0, 0), (50,50), 30)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = 100
    bomb2_rct.centery = 100
    scrn_sfc.blit(bomb2_sfc, bomb2_rct) 
    vx2, vy2 = 0, 0

    # 練習５
    
    bomb_sfc = pg.Surface((40, 40)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (20, 20), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 
    vx, vy = +1, +1


    # 練習２
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        # 練習4
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]:
            
            tori_rct.centery -= 1
            
        if key_dct[pg.K_DOWN]:
            
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1            
        scrn_sfc.blit(tori_sfc, tori_rct) 
        # 練習６
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        ato=tori_sfc
        ato2=tori_rct
        bomb2_rct.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb2_sfc, bomb2_rct) 
        yoko2, tate2 = check_bound(bomb2_rct, scrn_rct)
        x=pg.time.get_ticks()
        
        vx2 *= yoko2
        vy2 *= tate2

        #bomb3_rct.move_ip(vx3, vy3)
        #scrn_sfc.blit(bomb3_sfc, bomb3_rct) 
        #yoko3, tate3 = check_bound(bomb3_rct, scrn_rct)
        #vx3 *= yoko3
        #vy3 *= tate3
        

        x=pg.time.get_ticks()
        henka(x)
        #y=pg.key.name()
        #if y == "t":
         #   pg.time.wait(1000)

        # 練習８
        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(bomb2_rct):
            return


        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()