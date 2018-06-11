import pygame
from pygame.locals import *
import sys

def main():
    pygame.init() # 初期化
    screen = pygame.display.set_mode((500, 637)) # ウィンドウサイズの指定
    """ 参考サイトのコードは以下の三行だけど上の一行でも動いた
    (w, h) = (500, 637)
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    """
    pygame.display.set_caption("Pygame Test") # ウィンドウの上の方に出てくるアレの指定
    bg = pygame.image.load("imageFolder/DotImage.png").convert_alpha() # 背景画像の指定
    rect_bg = bg.get_rect() # 画像のサイズ取得？？だと思われる

    while(True):
        screen.fill((0, 0, 0, 0)) # 背景色の指定。RGBのはず
        screen.blit(bg, rect_bg) # 背景画像の描画
        pygame.time.wait(30) # 更新間隔。多分ミリ秒
        pygame.display.update() # 画面更新

        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()