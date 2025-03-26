import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 10000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DNA Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Different DNA Strands
human = "ATGCGTACGTTGACCTAGGCTAACCGTTCAGC"
virus = "TTAAGCGGCTGACCGAATTCCGGTAGCTTAGG"
bacteria = "GCTTAGGCCAATCGTTAAGGCCGATCCTAGGT"
strawberry = "ATGGTGAGCTCAGTTGGTGACCTGAGGCTTCA"

# DNA colors
Cytosine  = (255, 255, 0)
Thymine  = (0, 100, 255)
Guanine  = (255, 0, 0)
Adenine = (0, 255, 0)

# DNA parameters
num_base_pairs = 16
base_spacing = 40
amplitude = 100
speed = 0.05
angle_offset = 0

# Function to generate random base pairs
def generate_base_pair():
    return random.choice(["A", "T", "C", "G"])

# Function to get the color for a base
def get_base_color(base):
    if base == "A":
        return Adenine
    elif base == "T":
        return Thymine
    elif base == "C":
        return Cytosine
    elif base == "G":
        return Guanine

# Function to interpolate between two colors
def interpolate_color(color1, color2, t):
    return tuple(int(c1 + (c2 - c1) * t) for c1, c2 in zip(color1, color2))

# Function to handle click events on buttons
def handle_click(pos, button_rects):
    for idx, rect in enumerate(button_rects):
        if rect.collidepoint(pos):
            return idx  # Return the index of the clicked button
    return None

# Game loop
running = True
clock = pygame.time.Clock()

# Default DNA sequence (human)
current_sequence = human

# List to store the sequence of bases for the current DNA strand
dna_sequence = [base for base in current_sequence]

# Keep track of the colors of each base pair
base_colors = [get_base_color(base) for base in dna_sequence]

# Buttons for selecting DNA sequence
button_font = pygame.font.SysFont("Arial", 24)
buttons = [
    ("Human", human),
    ("Virus", virus),
    ("Bacteria", bacteria),
    ("Strawberry", strawberry),
]

# Rectangles for buttons
button_rects = []
for i, (label, sequence) in enumerate(buttons):
    text_surface = button_font.render(label, True, BLACK)
    button_rect = pygame.Rect(50, 50 + i * 50, 150, 40)
    button_rects.append(button_rect)

while running:
    screen.fill(WHITE)

    # Draw buttons for DNA sequence selection
    for i, (label, _) in enumerate(buttons):
        pygame.draw.rect(screen, (200, 200, 200), button_rects[i])  # Draw button
        text_surface = button_font.render(label, True, BLACK)
        screen.blit(text_surface, (button_rects[i].x + 10, button_rects[i].y + 10))

    # Draw DNA strands with the selected sequence
    for i in range(len(dna_sequence)):
        angle = i * 0.4 + angle_offset  # Add rotation to the angle
        x1 = WIDTH // 2 + amplitude * math.sin(angle)
        y = 100 + i * base_spacing
        x2 = WIDTH // 2 - amplitude * math.sin(angle)

        # Get base and complementary base
        base1 = dna_sequence[i]
        base2 = "T" if base1 == "A" else "A" if base1 == "T" else "C" if base1 == "G" else "G"
        
        # Get color for the bases
        color1 = base_colors[i]
        color2 = get_base_color(base2)

        # Smooth transition of colors (interpolation)
        transition_progress = 0.0  # Color transition
        interpolated_color1 = interpolate_color(color1, color2, transition_progress)
        interpolated_color2 = interpolate_color(color2, color1, transition_progress)

        # Draw the base pairs (split the bars in half)
        pygame.draw.line(screen, BLACK, (x1, y), (x2, y), 2)
        
        # Half bar colored with the interpolated color1 (skinnier)
        pygame.draw.rect(screen, interpolated_color1, (min(x1, x2), y - 2, abs(x1 - x2) / 2, 4))
        
        # Half bar colored with the interpolated color2 (skinnier)
        pygame.draw.rect(screen, interpolated_color2, (min(x1, x2) + abs(x1 - x2) / 2, y - 2, abs(x1 - x2) / 2, 4))
        
        # Draw larger black dot at the end of the bar (bigger than before)
        pygame.draw.circle(screen, BLACK, (x1, y), 8)  # Left end dot
        pygame.draw.circle(screen, BLACK, (x2, y), 8)  # Right end dot

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a button was clicked
            clicked_button = handle_click(event.pos, button_rects)
            if clicked_button is not None:
                # Update the DNA sequence based on the clicked button
                current_sequence = buttons[clicked_button][1]
                dna_sequence = [base for base in current_sequence]
                base_colors = [get_base_color(base) for base in dna_sequence]
    
    # Update rotation angle to make the strands rotate
    angle_offset += speed

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
