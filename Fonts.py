import pygame
my_name = "Isaac Furches"
pygame.init()
my_font = pygame.font.SysFont("arial", 64, bold=True, italic=True)
name_surface = my_font.render(my_name, True, (0,0,0), (255, 255, 255))
pygame.image.save(name_surface, "name.png")
