import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DNA Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYTOSINE = (255, 255, 153)  # Pastel Yellow
THYMINE = (102, 178, 255)  # Pastel Blue
GUANINE = (255, 102, 102)  # Pastel Red
ADENINE = (153, 255, 153)  # Pastel Green

# Different DNA Strands
human = "ATGCGTACGTTGACCTAGGCTAACCGTTCAGC"
virus = "TTAAGCGGCTGACCGAATTCCGGTAGCTTAGG"
bacteria = "GCTTAGGCCAATCGTTAAGGCCGATCCTAGGT"
strawberry = "ATGGTGAGCTCAGTTGGTGACCTGAGGCTTCA"

# Base pair mapping
complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
base_colors = {"A": ADENINE, "T": THYMINE, "C": CYTOSINE, "G": GUANINE}

# DNA parameters
num_base_pairs = 16
base_spacing = 40
amplitude = 100
speed = 0.02  # Slow down the speed for smoother rotation
angle_offset = 0
helix_turns = 6  # Number of turns of the helix

# Default DNA sequence
current_sequence = human
is_frozen = False  # Track if the DNA animation is frozen

# Define button fonts and rects
button_font = pygame.font.SysFont("Arial", 24)
freeze_button_rect = pygame.Rect(50, 50, 150, 40)
buttons = [
    ("Human", human),
    ("Virus", virus),
    ("Bacteria", bacteria),
    ("Strawberry", strawberry),
]
button_rects = []
for i, (label, sequence) in enumerate(buttons):
    button_rect = pygame.Rect(50, 100 + i * 50, 150, 40)
    button_rects.append(button_rect)

def handle_click(pos, button_rects):
    for idx, rect in enumerate(button_rects):
        if rect.collidepoint(pos):
            return idx  # Return index of clicked button
    return None

# Function to draw the base pair rungs with a glow effect
def draw_rung(x1, y, x2, color1, color2):
    # Horizontal rectangle dimensions
    rect_height = 8
    rect_width = abs(x1 - x2)

    # Draw the left and right bars (rectangles) with a glow effect
    for i in range(3):  # Add a subtle glow effect by drawing multiple rectangles with increasing transparency
        pygame.draw.rect(screen, (color1[0], color1[1], color1[2], 255 - i * 80),
                         (min(x1, x2) - i, y - rect_height / 2 - i, rect_width / 2 + 2 * i, rect_height + 2 * i))  # Left bar with glow
        pygame.draw.rect(screen, (color2[0], color2[1], color2[2], 255 - i * 80),
                         (min(x1, x2) + rect_width / 2 - i, y - rect_height / 2 - i, rect_width / 2 + 2 * i, rect_height + 2 * i))  # Right bar with glow

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)  # Set the background to black
    
    # Draw the Freeze button
    pygame.draw.rect(screen, (200, 200, 200), freeze_button_rect)
    text_surface = button_font.render("Freeze", True, BLACK)
    screen.blit(text_surface, (freeze_button_rect.x + 10, freeze_button_rect.y + 10))
    
    # Draw DNA selection buttons
    for i, (label, _) in enumerate(buttons):
        pygame.draw.rect(screen, (200, 200, 200), button_rects[i])
        text_surface = button_font.render(label, True, BLACK)
        screen.blit(text_surface, (button_rects[i].x + 10, button_rects[i].y + 10))
    
    if not is_frozen:  # Normal animated helix
        for i in range(len(current_sequence)):
            # Calculate angle and vertical offset to simulate helical rotation
            angle = i * 0.4 + angle_offset  # Horizontal movement (wave)
            y = 100 + i * base_spacing  # Constant height for base pairs

            # Calculate horizontal positions using sine and cosine for the helix effect
            x1 = WIDTH // 2 + amplitude * math.sin(angle)
            x2 = WIDTH // 2 - amplitude * math.sin(angle)

            base1 = current_sequence[i]
            base2 = complements[base1]
            color1 = base_colors[base1]
            color2 = base_colors[base2]

            # Switch the colors if the black balls are close enough
            if abs(x1 - x2) < 15:  # Threshold for when the black balls are "touching"
                color1, color2 = color2, color1  # Swap the colors

            # Constant bar height
            bar_height = 8
            bar_width = 4

            # Ensure bars connect the two black circles
            pygame.draw.line(screen, WHITE, (x1, y), (x2, y), bar_width)  # Draw the horizontal line between the balls

            # Draw the base pair rungs (rectangles + glow effect)
            draw_rung(x1, y, x2, color1, color2)

            # Draw the white balls (nucleotides)
            pygame.draw.circle(screen, WHITE, (x1, y), 8)
            pygame.draw.circle(screen, WHITE, (x2, y), 8)
    else:  # When DNA is frozen, display as a ladder
        ladder_x = WIDTH // 2  # Central position for the ladder
        for i in range(len(current_sequence)):
            y = 100 + i * base_spacing  # Constant vertical spacing for ladder bars
            base1 = current_sequence[i]
            base2 = complements[base1]
            color1 = base_colors[base1]
            color2 = base_colors[base2]

            # Draw vertical bars representing the base pairs with glow effect
            pygame.draw.rect(screen, (color1[0], color1[1], color1[2], 255), (ladder_x - 50, y - 10, 100, 20))  # Left side base (longer horizontally)
            pygame.draw.rect(screen, (color2[0], color2[1], color2[2], 255), (ladder_x - 50 + 110, y - 10, 100, 20))  # Right side base (longer horizontally)

            # Draw connecting lines between base pairs (like the ladder rungs)
            pygame.draw.line(screen, WHITE, (ladder_x - 50, y), (ladder_x + 50 + 110, y), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_button = handle_click(event.pos, button_rects)
            if clicked_button is not None:
                current_sequence = buttons[clicked_button][1]
            # Handle Freeze Button click
            if freeze_button_rect.collidepoint(event.pos):
                is_frozen = not is_frozen  # Toggle the freeze state
    
    angle_offset += speed  # Update wave movement more smoothly
    pygame.display.flip()
    clock.tick(60)  # Increased frame rate for smoother animation

pygame.quit()
