import cv2


def start_camera():
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera")
        exit()

    print("Camera started")

    while True:
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow('Camera', frame)

        # Check for key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture
    cap.release()
    cv2.destroyAllWindows()
