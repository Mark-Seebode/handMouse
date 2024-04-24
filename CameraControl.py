import cv2


def start_camera():
    cap = cv2.VideoCapture(0)

    for i in range(1000):
        pass

    if not cap.isOpened():
        print("Error: Could not open camera")
        exit()

    print("Camera successfully opened")

    for i in range(1000):
        pass

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame")

            cap = cv2.VideoCapture(0)
            break

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


start_camera()
