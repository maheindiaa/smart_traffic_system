from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

video = cv2.VideoCapture("traffic.mp4")

cv2.namedWindow(
    "YOLO Traffic Detection",
    cv2.WINDOW_NORMAL
)

cv2.resizeWindow(
    "YOLO Traffic Detection",
    1280,
    720
)

while True:

    ret, frame = video.read()

    if not ret:
        break
    
    resized_frame = cv2.resize(
        frame,
        (1280, 720)
    )

    results = model(resized_frame)
    # results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow(
        "YOLO Traffic Detection",
        annotated_frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()