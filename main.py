import cv2
import RPi.GPIO as GPIO
import time

servoPIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)


def main():
	p = GPIO.PWM(servoPIN, 50)
	p.start(2.5) # Initialization

	face_cascade = cv2.CascadeClassifier('frontalface.xml')

	vid = cv2.VideoCapture(0)


	if not vid:
		print("!!! Failed VideoCapture: invalid parameter!")

	faceConfidence = 0
	while True:
		# Read the frame
		_, img = vid.read()
		# Convert to grayscale
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		# Detect the faces
		faces = face_cascade.detectMultiScale(gray, 1.1, 4)
		# Draw the rectangle around each face
		for (x, y, w, h) in faces:
			cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
		# Display
		cv2.imshow('img', img)
		# Stop if escape key is pressed
		k = cv2.waitKey(30) & 0xff
		if k==27:
			break

	if len(faces) >= 1:
		faceConfidence += 0.1
	else:
		faceConfidence = 0
	if faceConfidence > 0.8:
		print("FACE DETECTED!!!!!")
		p.ChangeDutyCycle(5)
		time.sleep(1)
	else:
		print()
		p.ChangeDutyCycle(2.5)
		time.sleep(1)

	# Release the VideoCapture object
	cap.release()

try:
	main()
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
