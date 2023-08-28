import cv2
import pygame

pygame.init()

cap = cv2.VideoCapture(0)

# pygame window class
class Window:
    def __init__(self):
        self.window = pygame.display.set_mode((1280, 720))
        
    def update(self, image):
        
        original_surface = pygame.surfarray.make_surface(image)
        
        rotated_surface = pygame.transform.rotate(original_surface, -90)
        
        self.window.blit(rotated_surface, (50, 50))
        pygame.display.flip()
        
        self.window.fill((255,255,255))
    
window = Window()

# main loop
while True:
    # frame capture
    ret, frame = cap.read()
    
    if not ret:
        break
    
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # update pygame window
    window.update(rgb_image)
    
    # close cv video feed
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

