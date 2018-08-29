from Population import *

test = Population()


def evolve():
    test.compute_total_fitness()
    test.natural_selection()
    test.all_dead = False
    test.generation += 1


def update():
    test.update()
    pygame.display.update()
    pygame.event.clear()
    clock.tick(frame_per_second)
    if test.all_dead:
        evolve()
        # pygame.time.wait(1000)


while not simulation_over:
    text_surface = data_font.render('Generation: {}'.format(test.generation), False, YELLOW)
    game_display.fill(WHITE)
    game_display.blit(text_surface, (600, 0))
    pygame.draw.rect(game_display, GREEN, goal)
    if test.generation <= 5:
        update()
    elif test.generation <= 15:
        pygame.draw.rect(game_display, GREY, obs_a)
        pygame.draw.rect(game_display, GREY, obs_b)
        update()
    else:
        pygame.draw.rect(game_display, GREY, obs_a)
        pygame.draw.rect(game_display, GREY, obs_b)
        pygame.draw.rect(game_display, GREY, obs_c)
        pygame.draw.rect(game_display, GREY, obs_d)
        update()
pygame.quit()
quit(0)
