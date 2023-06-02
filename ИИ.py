#Нахождение контуров объектов на изображении
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Отрисовка контуров и выделение области синего цвета
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 500:
        cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 2)

#Отображение видео с контурами
cv2.imshow('frame', frame)

# Выход из цикла по нажатию клавиши q
if cv2.waitKey(1) & 0xFF == ord('q'):
    break

#Освобождение ресурсов
cap.release()
cv2.destroyAllwindows()

import cv2
import numpy as пр

#Определение диапазона синего цвета

lower_blue = np.array ([110, 56, 50])
upper_blue = np.array ([130, 255, 255])

#Инициализация камеры
cap = cv2.VideoCapture(0)
while True:
    # Получение кадра с камеры
    ret, frame = cap.read()

    # Преобразование изображения в пространство цветов HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Создание маски для синего цвета
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Применение морфологических операций для удаления шума
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
