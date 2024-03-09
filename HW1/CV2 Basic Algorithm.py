import cv2

parentPath = "Images/"


def showImage(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.imwrite(parentPath + title + ".jpg", image)
    cv2.destroyAllWindows()


def drawRectanglesAndText(image, rectangle_coordinates, rectangle_color, rectangle_thickness):
    # Draw the rectangle on the image
    cv2.rectangle(image, rectangle_coordinates[0], rectangle_coordinates[1], rectangle_color, rectangle_thickness)

    # Define text parameters
    text = "Hello, OpenCV!"
    text_color = (255, 255, 255)  # White color in BGR format
    text_font = cv2.FONT_HERSHEY_SIMPLEX
    text_scale = 0.8
    text_thickness = 1
    text_position = (70, 200)

    # Put text on the image
    cv2.putText(image, text, text_position, text_font, text_scale, text_color, text_thickness)
    showImage("RectangleImage & Text", image)


def morpbologyEx(image, kernel):
    binary_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ## cv2.MORPH_DILATE cv2.MORPH_OPEN cv2.MORPH_CLOSE
    eroded_image = cv2.morphologyEx(binary_image, cv2.MORPH_ERODE, kernel)
    showImage("MorpbologyImage", image)
    return eroded_image


def greythreshold(image, threshold_value: 0, max_value: 255, method):
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if (method == "SELF"):
        _, thresholded_image = cv2.threshold(grey_image, threshold_value, max_value, cv2.THRESH_BINARY)
    elif (method == "OTSU"):
        _, thresholded_image = cv2.threshold(grey_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    showImage(method + "_Grey_Image", thresholded_image)
    return thresholded_image


def bFilter(image, d, sigmaColor, sigmaSpace):
    filtered_image = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    showImage("bilateralFilter_Image", filtered_image)
    return filtered_image


def blur(image, kernel_size, method):
    if (method == "G"):
        blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    elif (method == "N"):
        blurred_image = cv2.blur(image, (kernel_size, kernel_size))
    elif (method == "M"):
        blurred_image = cv2.medianBlur(image, (kernel_size, kernel_size))

    showImage(method + "blurred_Image", blurred_image)
    return blurred_image


def convertImageToGrey(image):
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    showImage("greyImage", grey_image)
    return grey_image


def readFiles(filepath):
    image = cv2.imread(filepath)
    showImage("OGImage", image)
    return image


def main():
    files = [parentPath + "people.jpg", parentPath + "pic1.jpg", parentPath + "pic2.jpg", parentPath + "pic3.jpg"]
    for f in files:
        image = readFiles(f)
        convertImageToGrey(image)


if __name__ == "__main__":
    # Call the main function
    main()
