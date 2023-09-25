from pico2d import *

open_canvas(1280, 1024)
ground = load_image('TUK_GROUND.png')
character = load_image('FinnJake_SpriteSheet.png')

def handle_events():
    global running
    global x, y
    global dirX, dirY

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
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

running = True
x, y = 800 // 2, 600 // 2
dirX, dirY = 0, 0
frame = 0

while running:
    clear_canvas()
    ground.draw(1280 // 2, 1024 // 2)
    character.clip_draw(frame * 90, 0, 90, 90, x, y, 200, 200)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 14
    x += dirX * 10
    y += dirY * 10

    delay(0.05)

close_canvas()
