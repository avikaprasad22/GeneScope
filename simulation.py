import pygame 
import math
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 800
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

# Game loop
running = True
clock = pygame.time.Clock()

# Generate random DNA sequence
dna_sequence = [generate_base_pair() for _ in range(num_base_pairs)]
color_transition_progress = [0.0] * num_base_pairs  # Progress of color transition (0.0 to 1.0)

while running:
    screen.fill(WHITE)
    
    # Draw DNA strands with random base pairs
    for i in range(num_base_pairs):
        angle = i * 0.4 + angle_offset
        x1 = WIDTH // 2 + amplitude * math.sin(angle)
        y = 100 + i * base_spacing
        x2 = WIDTH // 2 - amplitude * math.sin(angle)
        
        # Get base and complementary base
        base1 = dna_sequence[i]
        base2 = "T" if base1 == "A" else "A" if base1 == "T" else "C" if base1 == "G" else "G"
        
        # Get color for the bases
        color1 = get_base_color(base1)
        color2 = get_base_color(base2)
        
        # Smooth transition of colors (interpolation)
        transition_progress = color_transition_progress[i]
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
        
        # Gradually increase the transition progress to switch colors over time
        if abs(x1 - x2) < 10:  # Check if the dots are near (i.e., bases are "connected")
            color_transition_progress[i] += 0.05  # Increase the transition progress
            if color_transition_progress[i] > 1.0:
                color_transition_progress[i] = 0.0  # Reset to 0 for next transition
        else:
            color_transition_progress[i] = max(0.0, color_transition_progress[i] - 0.01)  # Gradually reset

    # Update the animation
    angle_offset += speed
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
