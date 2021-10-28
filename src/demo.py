import cv2
import dlib
import numpy as np
from PIL import Image

from src.factory import setup_model


def draw_label(image, point, label, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.8, thickness=1):
    size = cv2.getTextSize(label, font, font_scale, thickness)[0]
    x, y = point
    cv2.rectangle(image, (x, y - size[1]), (x + size[0], y), (255, 0, 0), cv2.FILLED)
    cv2.putText(
        image, label, point, font, font_scale, (255, 255, 255), thickness, lineType=cv2.LINE_AA
    )


def convert_pil_2_cv2(img: Image.Image) -> np.array:
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)


def convert_cv2_2_pil(img: np.array) -> Image.Image:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return Image.fromarray(img)


def resize_image(img: np.array) -> np.array:
    h, w, _ = img.shape
    r = 640 / max(w, h)
    return cv2.resize(img, (int(w * r), int(h * r)))


def detect_age_gender(img: Image.Image) -> Image.Image:
    margin = 0.4

    # for face detection
    detector = dlib.get_frontal_face_detector()

    # load model and weights
    model, img_size = setup_model()

    img = convert_pil_2_cv2(img)
    img = resize_image(img)
    # dlib needs image in rgb format
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_h, img_w, _ = np.shape(img_rgb)

    # detect faces using dlib detector
    detected = detector(img_rgb, 1)
    faces = np.empty((len(detected), img_size, img_size, 3))
    print(f"# faces: {len(detected)}")
    if len(detected) > 0:
        for i, d in enumerate(detected):
            x1, y1, x2, y2, w, h = (
                d.left(),
                d.top(),
                d.right() + 1,
                d.bottom() + 1,
                d.width(),
                d.height(),
            )
            xw1 = max(int(x1 - margin * w), 0)
            yw1 = max(int(y1 - margin * h), 0)
            xw2 = min(int(x2 + margin * w), img_w - 1)
            yw2 = min(int(y2 + margin * h), img_h - 1)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # cv2.rectangle(img, (xw1, yw1), (xw2, yw2), (255, 0, 0), 2)
            faces[i] = cv2.resize(img[yw1 : yw2 + 1, xw1 : xw2 + 1], (img_size, img_size))

        # predict ages and genders of the detected faces
        results = model.predict(faces)
        predicted_genders = results[0]
        ages = np.arange(0, 101).reshape(101, 1)
        predicted_ages = results[1].dot(ages).flatten()
        print(predicted_ages)
        # draw results
        for i, d in enumerate(detected):
            label = "{}, {}".format(
                int(predicted_ages[i]), "M" if predicted_genders[i][0] < 0.5 else "F"
            )
            draw_label(img, (d.left(), d.top()), label)
            print(label)
    return convert_cv2_2_pil(img)
