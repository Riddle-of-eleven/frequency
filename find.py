import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


from rich.table import Table
from rich.console import Console

import utility as u

def find_objects(image, low=1, high=5, step=10, threshold=0.5):
    """Ищет повторения и закономерности на заданном изображении

    :param PIL Image image: анализируемое изображение
    :param int low: нижняя граница масштаба, defaults to 1
    :param int high: верхняя граница масштаба, defaults to 5
    :param int step: шаг проверки рядов пикселей, defaults to 10
    :param int threshold: пороговое значение амплитуды, defaults to 0.5
    """


    print(u.get_coefficints(image[0], low, high, threshold))
    # similarities = []
    # for key, value in enumerate(image):
    #     if key == 0: continue
    #     similarities.append(u.cosine_similarity(value, image[key - 1]))

    # print(similarities)