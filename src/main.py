import cv2

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("DMS - Camera", frame)

        # ESC to quit
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
