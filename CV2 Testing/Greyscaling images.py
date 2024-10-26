import cv2
# Defining the test image
test_image = cv2.imread("C:\\Users\\gibbi\\OneDrive\\Documents\\A Level\\Computer Science\\NEA\\CV2 Testing\\Colour_Scale.png")

# Creating the function to greyscale the image
def grayscale_image(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Turns the image greyscale
    cv2.imshow('Grayscale', grayscale_image) # Displays the greyscale image
    cv2.waitKey(0) # The window will close upon any key press

# Running the greyscale function
grayscale_image(test_image)

# Destroys all open windows
cv2.destroyAllWindows
