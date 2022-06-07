import cv2
import numpy as np
from matplotlib import pyplot as plt


def showImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()


def getColor(img, y, x):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)


def setColor(img, x, y, r, g, b):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)

    return img


def showImageGrid(img, title):
    fig, axis = plt.subplots()
    img_mplib = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(img_mplib)
    axis.set_title(title)
    plt.show()


def convert(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def showMultipleImageGrid(imgsarray, titles_array, x, y):
    if x < 1 or y < 1:
        print("Erro: X e Y não podem ser zero ou abaixo de zero simultaneamente!")
        return

    elif x == 1 and y == 1:
        showImageGrid(imgsarray[0], titles_array[0])

    elif x == 1:
        fig, axis = plt.subplots(y)
        fig.suptitle(titles_array)
        axis_id = 0
        for img in imgsarray:
            img_mplib = convert(img)
            axis[axis_id].imshow(img_mplib)
            axis_id += 1

    elif y == 1:
        fig, axis = plt.subplots(1, x)
        fig.suptitle(titles_array)
        axis_id = 0
        for img in imgsarray:
            img_mplib = convert(img)
            axis[axis_id].imshow(img_mplib)
            axis_id += 1

    else:
        fig, axis = plt.subplots(y, x)
        x_id, y_id, title_id = 0, 0, 0
        for img in imgsarray:
            img_mplib = convert(img)
            axis[y_id, x_id].set_title(titles_array[title_id])
            axis[y_id, x_id].imshow(img_mplib)
            if len(titles_array[title_id]) == 0:
                axis[y_id, x_id].axis('off')
            title_id += 1
            x_id += 1
            if x_id == x:
                x_id = 0
                y_id += 1
        fig.tight_layout(pad=0.5)
    plt.show()


def plotTwoImageHorizontal(img_original):
    img_replicate = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_REPLICATE)

    # criando grid com 2 imagens a segunda com borda replicada
    imgsarray = [img_original, img_replicate]
    title = "Imagem original e imagem com borda replicada"
    showMultipleImageGrid(imgsarray, title, 2, 1)


def plotTwoImageVertical(img_original):
    img_replicate = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_REPLICATE)

    # criando grid com 2 imagens a segunda com borda replicada
    imgsarray = [img_original, img_replicate]
    title = "Imagem original e imagem com borda replicada"
    showMultipleImageGrid(imgsarray, title, 1, 2)


def plotThreeImages(img_original):
    img_replicate = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    img_reflect = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    img_transparent = np.ones((img_original.shape[0], img_original.shape[1], 4), np.uint8) * 255

    # criando grid com 3 imagens, a segunda com borda replicada  e a terceira com borda espelho
    # a ultima imagem é transparente
    imgs_array = [img_original, img_replicate, img_reflect, img_transparent]
    titles_array = ['Imagem Original', 'Imagem com borda Replicada', 'Imagem com Borda de Espelho',
                    '']
    showMultipleImageGrid(imgs_array, titles_array, 2, 2)

def plotFourImages(img_original):
    img_replicate = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    img_reflect = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    img_reflect101 = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_REFLECT_101)
    # criando grid com 3 imagens, a segunda com borda replicada  e a terceira com borda espelho
    # a ultima imagem é transparente
    imgs_array = [img_original, img_replicate, img_reflect, img_reflect101]
    titles_array = ['Original', 'Borda Replicada', 'Borda de Espelho', 'Borda de Espelho 101']
    showMultipleImageGrid(imgs_array, titles_array, 2, 2)


def plotSixImages(img_original):
    img_replicate = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    img_reflect = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    img_reflect101 = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_REFLECT_101)
    img_wrap = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_WRAP)

    blue = [255, 0, 0]
    img_constant = cv2.copyMakeBorder(img_original, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value=blue)

    # criando grid com 3 imagens, a segunda com borda replicada  e a terceira com borda espelho
    # a ultima imagem é transparente

    imgs_array = [img_original, img_replicate, img_reflect, img_reflect101, img_wrap, img_constant]
    titles_array = ['Original', 'Borda Replicada', 'Borda de Espelho', 'Borda de Espelho 101', 'Borda Wrap',
                    'Borda Constante']
    showMultipleImageGrid(imgs_array, titles_array, 3, 2)


def main():
    obj_img = cv2.imread("arnold_schwarzenegger.jpg")
    plotSixImages(obj_img)


main()
