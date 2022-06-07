import numpy as np
import cv2
from matplotlib import pyplot as plt

HEIGHT = 600
WIDTH = 600

BLUE = 255, 0, 0
RED = 0, 0, 255
GREEN = 0, 255, 0
WHITE = 255, 255, 255
BLACK = 0, 0, 0

CENTER_COORD = (HEIGHT//2, WIDTH//2)


def showImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()


def drawEllipse(img, rotation_angle, start_angle, end_angle, color, thickness):
    axes_length = (200, 50)
    cv2.ellipse(img,
                CENTER_COORD,
                axes_length,
                rotation_angle,
                start_angle,
                end_angle,
                color,
                thickness)


def drawCircle(img, center, radius, color, thickness):

    cv2.circle(img, center, radius, color, thickness)


def main():
    image = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    # parametros: imagem, coordenadas de centro, largura x e y, angulo de rotacao, angulo de abertura, angulo
    # de fechamento, cores, grossura
    drawEllipse(image, 0, 0, 360, BLUE, 5)
    drawEllipse(image, 45, 0, 360, BLUE, 5)
    drawEllipse(image, 90, 0, 360, BLUE, 5)
    drawEllipse(image, 135, 0, 360, BLUE, 5)
    drawCircle(image, CENTER_COORD, 30, RED, -1)

    showImage(image)
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    video_output = cv2.VideoWriter('atom.avi', fourcc, 20.0, (HEIGHT, WIDTH))
    frames = 0
    position_electron1 = 0
    angle = 0
    while frames < 1000:
        image_atom = image.copy()
        drawEllipse(image_atom, angle, position_electron1, position_electron1 + 5, WHITE, 20)
        drawEllipse(image_atom, angle+45, position_electron1, position_electron1 + 5, WHITE, 20)
        drawEllipse(image_atom, angle-45, position_electron1, position_electron1 + 5, WHITE, 20)

        if frames % 5 == 0:
            position_electron1 += 7

        video_output.write(image_atom)
        frames += 5

    video_output.release()


main()
