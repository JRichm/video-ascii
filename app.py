import cv2
import pygame, sys
from pygame.locals import *

pygame.init()

cap = cv2.VideoCapture(0)

detail = 20
ascii_chars = " .,:;-~+=*|ivcJYLOVU@&#M%"


# pygame window class
class Window:
    def __init__(self):
        self.window = pygame.display.set_mode((730, 700))
        self.image_width = cap.read()[1].shape[1]
        self.image_height = cap.read()[1].shape[0]
        self.new_surface = pygame.Surface((self.image_width, self.image_height))
        self.colorSquare = pygame.Surface((detail, detail))

    def update(self, image):
        original_surface = pygame.surfarray.make_surface(image)
        rotated_surface = pygame.transform.rotate(original_surface, -90)

        for x in range((int)(self.image_width / detail)):
            for y in range((int)(self.image_height / detail)):
                pixel_color = rotated_surface.get_at((x * detail, y * detail))
                brightness = (pixel_color.r + pixel_color.g + pixel_color.b) / 3
                char_index = int(brightness / 255 * (len(ascii_chars) - 1))
                char = ascii_chars[char_index]
                pygame.draw.rect(
                    self.new_surface,
                    (
                        0,
                        0,
                        0,
                    ),
                    (x * detail, y * detail, detail, detail),
                )
                font = pygame.font.Font(None, 32)
                self.new_surface.blit(
                    font.render(char, True, pixel_color), (x * detail, y * detail)
                )

        self.window.blit(self.new_surface, (50, 50))
        # self.window.blit(rotated_surface, (50, 50))
        pygame.display.flip()

        self.window.fill((255, 255, 255))


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
    if cv2.waitKey(1) == ord("q"):
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

cap.release()
cv2.destroyAllWindows()
