from pico2d import *
import random

open_canvas(1280, 1024)
ground = load_image('TUK_GROUND.png')
character = load_image('FinnJake_SpriteSheet.png')


def handle_events():
    global running, reverse, idle
    global x, y, dirX, dirY
    global line

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            line=0
            if event.key == SDLK_RIGHT:
                dirX += 1
                line, reverse = 2, False
            elif event.key == SDLK_LEFT:
                dirX -= 1
                line, reverse = 2, True
            elif event.key == SDLK_UP:
                dirY += 1
                line = 3
            elif event.key == SDLK_DOWN:
                dirY -= 1
                line = 4
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
            elif event.key == SDLK_LEFT:
                dirX += 1
            elif event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1


def set_idle_state():
    global line, idle

    if dirX == 0 and dirY == 0:
        if curframe+1 >= total_frames[line]:
            line = 1

        idle = True
    else:
        if dirX > 0:
            line = 2
            reverse = False
        elif dirX < 0:
            line = 2
            reverse = True
        elif dirY > 0:
            line = 3
        elif dirY < 0:
            line = 4
        idle = False

# def isEnd(x, y):
#     if x < 0 or x > 1280:
#         return True
#     if y < 0 or y > 1024:
#         return True
#
#     return False


running, reverse, idle = True, False, True
x, y = 800 // 2, 600 // 2
dirX, dirY, speed = 0, 0, 10
curframe, line = 0, 0

frame_column = [360, 270, 180, 90, 0]
total_frames = [20, 12, 16, 11, 12]

while running:
    clear_canvas()
    ground.draw(1280 // 2, 1024 // 2)

    # if isEnd(x, y):
    #     speed = 0
    # else:
    #     speed =10

    if reverse:
        character.clip_composite_draw(curframe * 90, frame_column[line], 90, 90, 0, 'h', x, y, 250, 250)
    else:
        character.clip_draw(curframe * 90, frame_column[line], 90, 90, x, y, 250, 250)

    update_canvas()
    handle_events()
    set_idle_state()  # 대기모션 상태 판단

    curframe = (curframe + 1) % total_frames[line]
    x += dirX * speed
    y += dirY * speed

    delay(0.05)

close_canvas()
