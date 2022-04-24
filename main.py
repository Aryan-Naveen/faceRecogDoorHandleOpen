import cv2

def main():
    face_cascade = cv2.CascadeClassifier('frontalface.xml')

    vid = cv2.VideoCapture(0)


    if not vid:
        print("!!! Failed VideoCapture: invalid parameter!")


    faceConfidence  = 0
    while True:
        # Read the frame
        _, img = vid.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces) >= 1:
            faceConfidence += 0.05
        else:
            faceConfidence = 0
        
        if faceConfidence > 0.8:
            print("FACE DETECTED!!!!!")
        else:
            print()


    # Release the VideoCapture object
    cap.release()


main()