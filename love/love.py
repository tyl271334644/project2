import sys
import random
import pygame
from pygame.locals import *
import tkinter.messagebox
import tkinter as tk
import random
import threading
import time

from tkinter import *


#音乐设置
pygame.mixer.init()
pygame.mixer_music.load('./music/love.mp3')
pygame.mixer_music.play(1,0.0)



# 背景大小、颜色
WIDTH, HEIGHT = 600, 400
BACKGROUND = (255, 255, 255)
button_text_list = ['不同意？',  '你点不到的', '我没骗你', '哈哈点不到','你就同意吧']




# 按钮
def button(text, x, y, w, h, color, screen):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.Font('./font/simkai.ttf', 20)
    textRender = font.render(text, True, (0, 0, 0))
    textRect = textRender.get_rect()
    textRect.center = ((x+w/2), (y+h/2))
    screen.blit(textRender, textRect)


# 标题
def title(text, screen, scale, color=(230, 80, 120)):

    font = pygame.font.Font('./font/simkai.ttf', WIDTH//(len(text)*2))
    textRender = font.render(text, True, color)
    textRect = textRender.get_rect()
    textRect.midtop = (WIDTH/scale[0], HEIGHT/scale[1])
    screen.blit(textRender, textRect)


# 生成随机的位置坐标
def get_random_pos():
    x, y = random.randint(20, WIDTH-20), random.randint(20, HEIGHT-20)
    return x, y


# 点击喜欢按钮后显示的页面
def show_like_interface(text, screen, color=(255, 0, 0)):
    screen.fill(BACKGROUND)

    def dow():
        window = tk.Tk()
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        a = random.randrange(0, width)
        b = random.randrange(0, height)
        window.title('最爱你了，嘻嘻！')
        window.geometry("200x50" + "+" + str(a) + "+" + str(b))
        tk.Label(window,
                 text='最爱你了，嘻嘻！',  # 标签的文字
                 bg='Red',  # 背景颜色
                 font=('楷体', 17),  # 字体和字体大小
                 width=20, height=4  # 标签长宽
                 ).pack()  # 固定窗口位置
        window.mainloop()

    threads = []
    for i in range(200):  # 需要的弹框数量
        t = threading.Thread(target=dow)
        threads.append(t)
        time.sleep(0.1)
        threads[i].start()


    # tkinter.messagebox.showwarning("FishC Demo","我就知道你也喜欢我")
    #
    # font = pygame.font.Font('./font/simkai.ttf', WIDTH//(len(text)))
    # textRender = font.render(text, True, color)
    # textRect = textRender.get_rect()
    # textRect.midtop = (WIDTH/2, HEIGHT/2)
    # screen.blit(textRender, textRect)
    # pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


# 主函数
def main():
    text = '我才不要'
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)  #不全屏
    pygame.display.set_caption('来自一个喜欢你很久的小哥哥')
    clock = pygame.time.Clock()

    # 不喜欢按钮的初始位置和大小
    unlike_pos_x = 330
    unlike_pos_y = 250
    unlike_pos_width = 100
    unlike_pos_height = 50

    # 喜欢按钮的初始位置和大小
    like_pos_x = 180
    like_pos_y = 250
    like_pos_width = 100
    like_pos_height = 50
    running = True

    # 按钮颜色
    like_color = (230,80,120)
    
    # 若不点击喜欢按钮，就一直运行
    while running:
        screen.fill(BACKGROUND)

        # 加载图片
        img = pygame.image.load("./imgs/1.png")
        imgRect = img.get_rect()
        # 图片位置
        imgRect.midtop = 110, 20
        screen.blit(img, imgRect)



        # 监听事件
        for event in pygame.event.get():
            # 检测到鼠标
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 获取鼠标位置
                mouse_pos = pygame.mouse.get_pos()
                # 若点击了喜欢按钮，停止 while 循环
                if mouse_pos[0] < like_pos_x+like_pos_width and mouse_pos[0] > like_pos_x and\
                        mouse_pos[1] < like_pos_y+like_pos_height and mouse_pos[1] > like_pos_y:
                    like_color = BACKGROUND
                    running = False
        # 获取鼠标位置
        # 若鼠标位置位于按钮区域内
        # 则随机生成按钮位置进行显示
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < unlike_pos_x+unlike_pos_width and mouse_pos[0] > unlike_pos_x and\
                mouse_pos[1] < unlike_pos_y+unlike_pos_height and mouse_pos[1] > unlike_pos_y:
            while True:
                unlike_pos_x, unlike_pos_y = get_random_pos()
                text = button_text_list[random.randint(0, len(button_text_list)-1)]
                if mouse_pos[0] < unlike_pos_x+unlike_pos_width and mouse_pos[0] > unlike_pos_x and\
                        mouse_pos[1] < unlike_pos_y+unlike_pos_height and mouse_pos[1] > unlike_pos_y:
                    continue
                break


        title('小姐姐，我注意你很久了', screen, scale=[1.8, 10])
        title('做我女朋友好不好呀', screen, scale=[1.8, 3])
        button('^_^好呀', like_pos_x, like_pos_y, like_pos_width,
               like_pos_height, like_color, screen)


        button(text, unlike_pos_x, unlike_pos_y, unlike_pos_width,
               unlike_pos_height, (230,80,120), screen)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
    show_like_interface('最爱你了，嘻嘻！', screen, color=(230, 80, 120))


if __name__ == '__main__':
    main()
