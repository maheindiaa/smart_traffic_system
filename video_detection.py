import cv2

video = cv2.VideoCapture(
    "traffic.mp4"
)
cv2.namedWindow(
    "Traffic Video",
    cv2.WINDOW_NORMAL
)

cv2.resizeWindow(
    "Traffic Video",
    1280,
    720
)


cv2.namedWindow(
    "Gray Video",
    cv2.WINDOW_NORMAL
)

cv2.namedWindow(
    "Edge Video",
    cv2.WINDOW_NORMAL
)

while True:

    ret, frame = video.read()

    if not ret:
        break

    resized_frame = cv2.resize(
        frame,
        (1280, 720)
    )

    gray = cv2.cvtColor(
        resized_frame,
        cv2.COLOR_BGR2GRAY
    )

    blur = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    edges = cv2.Canny(
        blur,
        50,
        150
    )

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    vehicle_count = 0

    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 1000:

            x, y, w, h = cv2.boundingRect(
                contour
            )

            cv2.rectangle(
                resized_frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            vehicle_count += 1
    
    cv2.putText(
        resized_frame,
        f"Vehicles: {vehicle_count}",
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Traffic Video",
        resized_frame
    )

    gray_resized = cv2.resize(
        gray,
        (640, 360)
    )

    edges_resized = cv2.resize(
        edges,
        (640, 360)
    )

    cv2.imshow(
        "Gray Video",
        gray_resized
    )

    cv2.imshow(
        "Edge Video",
        edges_resized
    )

    

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()

cv2.destroyAllWindows()