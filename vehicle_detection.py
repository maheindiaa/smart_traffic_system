import cv2

image = cv2.imread("traffic.jpg")

if image is None:
    print("Image not found")

else:

    gray = cv2.cvtColor(
        image,
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

    contours, hierarchy = cv2.findContours(
        edges,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    contour_image = image.copy()

    vehicle_count = 0

    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 500:

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                contour_image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            vehicle_count += 1

    # cv2.drawContours(
    #     contour_image,
    #     contours,
    #     -1,
    #     (0, 255, 0),
    #     2
    # )

    

    cv2.namedWindow(
        "Original Image",
        cv2.WINDOW_NORMAL
    )

    resized_image = cv2.resize(
        image,
        (1000, 600)
    )

    cv2.imshow(
        "Original Image",
        resized_image
    )

    

    cv2.namedWindow(
        "Gray Image",
        cv2.WINDOW_NORMAL
)

    resized_gray = cv2.resize(
        gray,
        (1000, 600)
    )

    cv2.imshow(
        "Gray Image",
        resized_gray
    )

    cv2.namedWindow(
        "Blur Image",
        cv2.WINDOW_NORMAL
    )

    resized_blur = cv2.resize(
        blur,
        (1000, 600)
    )

    cv2.imshow(
        "Blur Image",
        resized_blur
    )

    cv2.namedWindow(
        "Edge Detection",
        cv2.WINDOW_NORMAL
    )

    resized_edges = cv2.resize(
        edges,
        (1000, 600)
    )

    cv2.imshow(
        "Edge Detection",
        resized_edges
    )

    cv2.namedWindow(
        "Contours",
        cv2.WINDOW_NORMAL
    )

    resized_contours = cv2.resize(
        contour_image,
        (1000, 600)
    )

    cv2.imshow(
        "Contours",
        resized_contours
    )

    print(
        "Vehicles Detected:",
        vehicle_count
    )

    def get_vehicle_count():
        return vehicle_count

    # print(
    #     "Detected vehicles variable:",
    #     detected_vehicles
    # )


    cv2.waitKey(0)

    cv2.destroyAllWindows()


    # cv2.imshow(
    #     "Original Image",
    #     image
    # )
    
    
    # resized_image = cv2.resize(
    #     image,
    #     (1000, 600)
    # )

    # cv2.imshow(
    #     "Original Image",
    #     resized_image
    # )

    # cv2.imshow(
    #     "Gray Image",
    #     gray
    # )

    # resized_gray = cv2.resize(
    #     gray,
    #     (1000, 600)
    # )

    # cv2.imshow(
    #     "Gray Image",
    #     resized_gray
    # )
