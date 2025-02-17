import pygame
import redis
import json
import time

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
        parts = message.split()
        _, entity_id, global_x, y, region, red, green, blue = parts
        entity_positions[int(entity_id)] = {"x": int(global_x), "y": int(y), "region": region,
                                            # "red": int(red), "green": int(green), "blue": int(blue)
                                            }

    # Clear the screen
    window.fill(background_color)

    # Draw entities
    for pos in entity_positions.values():
        # colour = (pos['red'], pos['green'], pos['blue'])
        # print(colour)
        pygame.draw.rect(window, entity_color, pygame.Rect(pos['x'], pos['y'], 2, 2))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    # time.sleep(0.03)

# Quit pygame
pygame.quit()
