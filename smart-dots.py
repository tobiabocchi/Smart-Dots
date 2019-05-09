from Goal import *
from Population import *
from Obstacle import *

goal = Goal()
all_sprites.add(goal)
population = Population()


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def handle_obstacles():
    global lvl_up
    global obs_index
    if lvl_up and obs_index < len(obs_topleft_list):
        Obstacle(obs_topleft_list[obs_index])
        lvl_up = False
        obs_index += 1


def evolve():
    population.compute_total_fitness()
    if population.generation % 2 == 1:
        population.boost_fitness()
    else:
        population.natural_selection()


def update():
    global lvl_up
    if not pop_sprites.sprites():  # if all dead:
        handle_obstacles()
        evolve()
        return
    winners = pygame.sprite.spritecollide(goal, pop_sprites, False)
    for winner in winners:
        winner.winner()
        lvl_up = True
    sprite_map = pygame.sprite.groupcollide(pop_sprites, obs_sprites, False, False)
    for loser in sprite_map:
        loser.die()
    pop_sprites.update()


def events():
    global simulation_over
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulation_over = True


def draw():
    clock.tick(frame_per_second)
    game_display.fill(WHITE)
    #  obs_sprites.draw(game_display)
    all_sprites.draw(game_display)
    draw_text(game_display, "GENERATION: " + str(population.generation) +
              " SCORE: " + str(population.total_fitness), 30,
              resolution[0] / 2, 10)
    pygame.display.flip()


while not simulation_over:
    draw()
    events()
    update()
