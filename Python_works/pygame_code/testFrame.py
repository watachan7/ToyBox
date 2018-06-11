import pygame
from pygame.locals import *
import sys

def main():

    # 初期化
    pygame.init()

    # ウィンドウサイズの指定
    screen = pygame.display.set_mode((540, 490))

    # ウィンドウの上の方に出てくるアレの指定
    pygame.display.set_caption("Pygame Test")

    # 背景画像の指定
    bg = pygame.image.load("imageFolder/DotImage.png").convert_alpha()

    # 画像のサイズ取得
    rect_bg = bg.get_rect() 

    while(True):
        # 背景色の指定(RGB)
        screen.fill((0, 0, 0, 0))
        # 背景画像の描画
        screen.blit(bg, rect_bg)
        # 更新間隔(ミリ秒)
        pygame.time.wait(30)
        # 画面更新
        pygame.display.update()

        # 終了処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()