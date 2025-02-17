import pygame
import redis
from entity import Entity

# Initialize pygame
pygame.init()

# Set up display
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Entity Positions')

# Set up colors
background_color = (0, 0, 0)  # Black
entity_color = (0, 255, 0)    # Green

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.delete('entity_positions')

# Dictionary to store entity positions
entity_positions = {}

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    messages = r.hgetall('entity_positions')
    # Poll Redis for new entity positions
    for key, message in messages.items():
        entity_positions[key] = Entity.deserialize(message)

    # Clear the screen
    window.fill(background_color)

    # Draw entities
    for pos in entity_positions.values():
        # colour = (pos['red'], pos['green'], pos['blue'])
        # print(colour)
        pygame.draw.rect(window, pos.color, pygame.Rect(pos.x, pos.y, 2, 2))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    # time.sleep(0.03)

# Quit pygame
pygame.quit()
