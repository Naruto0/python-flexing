from pygame import Surface, display, init, event, quit, KEYDOWN, time, font
from pygame.locals import QUIT, K_w, K_a, K_s, K_d
from pygame.draw import rect, lines
from random import randint


def modify(o, x, y):
    """Offset a line object"""
    return o[0] + x, o[1] + y


def get_random_pos(screen):
    """try to get some random position"""
    x, y = screen.get_size()
    x1 = randint(0, x//20-20) * 20
    y1 = randint(0, y//20-20) * 20
    return x1, y1


def spawn_apple(screen, snake):
    """spawn nice red apple for snake"""
    pos = get_random_pos(screen)
    while pos in snake:
        pos = get_random_pos(screen)

    return pos


def draw_appleh(origin, parent):
    """Draw an apple"""

    p1, p2 = modify(origin, 4, 4), modify(origin, 16, 4)
    p3, p4 = modify(origin, 16, 16), modify(origin, 4, 16)

    lines(parent, (255, 50, 50), False, [p1, p2, p3, p4, p1])


def draw_cell(origin, parent):
    """Snake made out of bricks is booring"""

    p1 = modify(origin, 2, 2)
    p2 = modify(origin, 18, 2)
    p3 = modify(origin, 18, 18)
    p4 = modify(origin, 2, 18)

    lines(parent, (125, 255, 125), False, [p1, p2, p3, p4, p1])


def game_loop():
    """basic game loop"""

    # now setup and initialize everything
    scr = display.set_mode(size=(800, 600))
    d = display
    d.set_caption("Pysnake")
    init()

    # make some black `background`
    bkg = Surface(scr.get_size())
    bkg = bkg.convert()

    # font to be incorporated TODO:
    fn = font.Font(None, 36)
    tex = fn.render("Hello world", 1, (255, 255, 255))
    tex_pos = tex.get_rect()
    tex_pos.centerx = bkg.get_rect().centerx
    tex.blit(bkg, tex_pos)

    # basic _not so_ `global` variables
    position = (0, 0)   # current snake position
    vector = (20, 0)    # mr. Snakes moves to right
    snakes = [(0, 0)]   # snake is array of cells
    length = 5          # initial snake's lenght
    appleh = spawn_apple(scr, snakes) # initial apple

    while 1:
        # game loop
        for e in event.get():
            if e.type == QUIT:
                quit()
            if e.type == KEYDOWN:
                if e.key == K_d:
                    vector = (20, 0)
                if e.key == K_a:
                    vector = (-20, 0)
                if e.key == K_w:
                    vector = 0, -20
                if e.key == K_s:
                    vector = 0, 20
        bkg.fill((0, 0, 0))
        position = position[0] + vector[0], position[1] + vector[1] # move the snake
        if position in snakes:   # collision detected
            vector = (0, 0)      # TODO:
        if appleh == position:   # collision with apple
            length += 1
            appleh = spawn_apple(scr, snakes)
        snakes.insert(0, position) # add current position to snake array
        if len(snakes) > length:   # if the snake is longer, than he should be
            snakes.pop()           # pop his tail
        for pos in snakes:         # for each cell in snake's list
            draw_cell(pos, bkg)    # draw the cell
        draw_appleh(appleh, bkg)    
        scr.blit(bkg, (0, 0))
        d.flip()
        # print(snakes)
        print(appleh)
        time.wait(125)              # you may set this to smaller number
        # or greater if you really are llama


if __name__ == "__main__":
    game_loop()
