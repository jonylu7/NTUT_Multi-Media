import cv2

parentPath = "Images/"
savePath = "Result/"


def showImage(title, image, ifSave: 0):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    if (ifSave):
        cv2.imwrite(savePath + title + ".jpg", image)
    cv2.destroyAllWindows()


def drawRectanglesAndText(image, f, rectangle_coordinates, rectangle_color, rectangle_thickness,
                          text, text_position: (70, 200),
                          text_color: (255, 255, 255), text_thickness: 1, text_scale: 0.8, ifSave: 0):
    # Draw the rectangle on the image
    cv2.rectangle(image, rectangle_coordinates[0], rectangle_coordinates[1], rectangle_color, rectangle_thickness)

    # Define text parameters
    text_font = cv2.FONT_HERSHEY_SIMPLEX

    # Put text on the image
    cv2.putText(image, text, text_position, text_font, text_scale, text_color, text_thickness)
    showImage("label_" + f, image, 0)


def morpbologyEx(binary_image, f, kernel, morphMode: cv2.MORPH_ERODE, ifSave: 0):
    ## cv2.MORPH_DILATE cv2.MORPH_OPEN cv2.MORPH_CLOSE
    eroded_image = cv2.morphologyEx(binary_image, morphMode, kernel)
    showImage("morpbology_" + f, eroded_image, ifSave)
    return eroded_image


def greythreshold(grey_image, f, threshold_value: 0, max_value: 255, method, ifSave: 0):
    if (method == "SELF"):
        _, thresholded_image = cv2.threshold(grey_image, threshold_value, max_value, cv2.THRESH_BINARY)
    elif (method == "OTSU"):
        _, thresholded_image = cv2.threshold(grey_image, 0, 255, cv2.THRESH_OTSU)

    showImage("binarization_" + f, thresholded_image, ifSave)
    return thresholded_image


def bFilter(image, f, d, sigmaColor, sigmaSpace, ifSave: 0):
    filtered_image = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    showImage("filter_" + f, filtered_image, ifSave)
    return filtered_image


def blur(image, f, kernel_size, method, ifSave: 0):
    if (method == "G"):
        blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    elif (method == "N"):
        blurred_image = cv2.blur(image, (kernel_size, kernel_size))
    elif (method == "M"):
        blurred_image = cv2.medianBlur(image, kernel_size)

    showImage("filter_" + f, blurred_image, ifSave)
    return blurred_image


def convertImageToGrey(image, f, ifSave: 0):
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    showImage("gray_" + f, grey_image, ifSave)
    return grey_image


def readFiles(filepath):
    image = cv2.imread(filepath)
    ##showImage("OG_", image)
    return image
