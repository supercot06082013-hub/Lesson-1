import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
image = cv2.imread("input.jpg")
overlay = cv2.imread("mask.jpg")
results = model(image)
count = 0
for result in results:
    boxes = result.boxes.xyxy.cpu().numpy()

    for box in boxes:
        x1, y1, x2, y2 = map(int, box[:4])
        count += 1
        if count > 2:
            break
        w = x2 - x1
        h = y2 - y1
        resized_overlay = cv2.resize(overlay, (w, h))
        image[y1:y2, x1:x2] = resized_overlay
cv2.imwrite("result.jpg", image)
print("Готово! result.jpg створено.")