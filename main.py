from flask import Flask, render_template, request
import cv2

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/process', methods=['POST'])
def process():
    # получаем файл фото из формы на сайте
    img = request.files['file']
    img.save("static/image.jpg")  # сохраняем фото в папке static

    # загружаем фото и переводим в оттенки серого
    image = cv2.imread("static/image.jpg")
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ищем круглый объект синего цвета на фото
    circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=30, minRadius=0, maxRadius=0)

    # если объект найден, то отправляем сообщение на сайт об успехе
    if circles is not None:
        return "На фото найден синий круг!"

    # если объект не найден, то отправляем сообщение на сайт о неудаче
    else:
        return "На фото не найден синий круг."


if __name__ == '__main__':
    app.run(debug=True)




