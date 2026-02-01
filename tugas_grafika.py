import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

# Data Titik dan Garis Kubus
vertices = ( (1,-1,-1), (1,1,-1), (-1,1,-1), (-1,-1,-1), (1,-1,1), (1,1,1), (-1,-1,1), (-1,1,1) )
edges = ( (0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7) )

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    # Gunakan bendera OPENGL dan DOUBLEBUF
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Tugas Grafika Komputer - Kubus & Persegi")
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -12)

    # State awal objek
   # Ganti baris ini:
    c_pos = [-3, 0, 0]; c_rot = 0; c_scale = 0.4  # <--- Ubah 1.0 jadi 0.4
    s_pos = [3, 0, 0]; s_rot = 0; s_scale = 1.0; s_shear = 0.0; s_reflect = 1.0
    
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        # Kontrol Kubus (W,S,A,Q)
        if keys[K_w]: c_pos[1] += 0.1
        if keys[K_s]: c_pos[1] -= 0.1
        if keys[K_a]: c_rot += 2
        if keys[K_q]: c_scale += 0.05

        # Kontrol Persegi (Panah, L, U, I, O)
        if keys[K_UP]:    s_pos[1] += 0.1
        if keys[K_DOWN]:  s_pos[1] -= 0.1
        if keys[K_l]:     s_rot += 2
        if keys[K_u]:     s_scale += 0.05
        if keys[K_i]:     s_shear += 0.05 
        if keys[K_o]:     s_reflect *= -1 # Tekan O untuk membalik (refleksi)
        if keys[K_p]:     s_shear = 0     # Reset miring

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # --- KUBUS 3D (Kiri) ---
        glPushMatrix()
        glTranslatef(c_pos[0], c_pos[1], c_pos[2])
        glRotatef(c_rot, 1, 1, 0)
        glScalef(c_scale, c_scale, c_scale)
        glColor3f(1, 1, 1)
        draw_cube()
        glPopMatrix()

        # --- PERSEGI 2D (Kanan) ---
        glPushMatrix()
        glTranslatef(s_pos[0], s_pos[1], s_pos[2])
        glRotatef(s_rot, 0, 0, 1)
        glScalef(s_scale * s_reflect, s_scale, 1)
        
        # Matriks Shearing
        shear_m = [1, s_shear, 0, 0, 
                   0, 1, 0, 0, 
                   0, 0, 1, 0, 
                   0, 0, 0, 1]
        glMultMatrixf(shear_m)
        
        glColor3f(0, 1, 0)
        draw_square()
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60) # Batasi 60 FPS agar tidak crash

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()