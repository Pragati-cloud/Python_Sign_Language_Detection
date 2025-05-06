import os
import cv2

# Create data directory if it doesn't exist
DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# Try different camera indices if needed
cap = cv2.VideoCapture(0)  # Change 0 to 1 or 2 if needed

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Collecting data for class {j}')

    # Ensure the frame is valid before showing
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame. Check camera.")
            break

        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Frame not captured.")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        file_path = os.path.join(class_dir, f'{counter}.jpg')

        # Ensure frame is valid before saving
        if frame is not None and frame.size > 0:
            cv2.imwrite(file_path, frame)
            counter += 1
        else:
            print(f"Warning: Skipping frame {counter}, it's empty.")

cap.release()
cv2.destroyAllWindows()
