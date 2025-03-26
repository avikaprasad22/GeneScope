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
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)

# DNA Base Colors
COLORS = {
    "A": (0, 255, 0),       # Green (Adenine)
    "T": (0, 100, 255),     # Blue (Thymine)
    "C": (255, 255, 0),     # Yellow (Cytosine)
    "G": (255, 0, 0)        # Red (Guanine)
}

# DNA Data
DNA_TYPES = {
    "Human": "ATGCGTACGTTGACCTAGGCTAACCGTTCAGC",
    "Virus": "TTAAGCGGCTGACCGAATTCCGGTAGCTTAGG",
    "Bacteria": "GCTTAGGCCAATCGTTAAGGCCGATCCTAGGT",
    "Strawberry": "ATGGTGAGCTCAGTTGGTGACCTGAGGCTTCA"
}

# UI Elements
font = pygame.font.Font(None, 24)
buttons = {
    "Human": pygame.Rect(50, 50, 120, 40),
    "Virus": pygame.Rect(50, 100, 120, 40),
    "Bacteria": pygame.Rect(50, 150, 120, 40),
    "Strawberry": pygame.Rect(50, 200, 120, 40)
}
examine_button = pygame.Rect(WIDTH - 120, 20, 100, 40)
selected_dna = None
zoomed_in = False
hover_text = ""
angle_offset = 0

def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect)
    label = font.render(text, True, BLACK)
    screen.blit(label, (rect.x + 10, rect.y + 10))

# Main loop
running = True
dna_sequence = []
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Draw selection buttons
    for name, rect in buttons.items():
        draw_button(name, rect, LIGHT_GRAY if selected_dna == name else GRAY)
    
    # Draw DNA strands if selected
    if selected_dna:
        if zoomed_in:
            for i, base in enumerate(dna_sequence):
                y = 100 + i * 40
                color = COLORS[base]
                pygame.draw.circle(screen, color, (WIDTH//2, y), 20)
                label = font.render(base, True, BLACK)
                screen.blit(label, (WIDTH//2 - 10, y - 10))
                
                # Hover effect
                if WIDTH//2 - 20 < mouse_x < WIDTH//2 + 20 and y - 20 < mouse_y < y + 20:
                    hover_text = f"{base}: {['Adenine', 'Thymine', 'Cytosine', 'Guanine'][['A', 'T', 'C', 'G'].index(base)]}"
        else:
            for i, base in enumerate(dna_sequence[:16]):
                angle = i * 0.4 + angle_offset
                y = 100 + i * 40
                x1 = WIDTH // 2 + 100 * math.sin(angle)
                x2 = WIDTH // 2 - 100 * math.sin(angle)
                pygame.draw.line(screen, BLACK, (x1, y), (x2, y), 2)
                pygame.draw.circle(screen, COLORS[base], (x1, y), 8)
                pygame.draw.circle(screen, COLORS[base], (x2, y), 8)
    
    # Update animation
    angle_offset += 0.05
    
    # Draw "Examine" button if DNA is selected
    if selected_dna:
        draw_button("Examine", examine_button, GRAY)
    
    # Show hover text
    if hover_text:
        hover_label = font.render(hover_text, True, BLACK)
        screen.blit(hover_label, (mouse_x + 10, mouse_y + 10))
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for name, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    selected_dna = name
                    dna_sequence = list(DNA_TYPES[name])
                    zoomed_in = False
            if examine_button.collidepoint(event.pos) and selected_dna:
                zoomed_in = not zoomed_in
            
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
