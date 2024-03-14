import CV2_Basic_Algorithm as cvba
import cv2
import numpy as np

##"people.jpg",
files = ["pic1.jpg", "pic2.jpg", "pic3.jpg"]


def labels1():
    f = files[1]
    newf = f[:-4]
    image = cvba.readFiles(cvba.parentPath + f)
    cvba.drawRectanglesAndText(image, newf, [(62, 89), (446, 325)], (100, 200, 100), 3,
                               "animated_character", (200, 90), (100, 200, 100), 3, 1)


def labels0():
    f = files[0]
    newf = f[:-4]
    image = cvba.readFiles(cvba.parentPath + f)
    cvba.drawRectanglesAndText(image, newf, [(168, 279), (440, 550)], (100, 200, 100), 3,
                               "Girl", (231, 556), (100, 200, 100), 3, 1)


def labels2():
    f = files[2]
    newf = f[:-4]
    image = cvba.readFiles(cvba.parentPath + f)
    cvba.drawRectanglesAndText(image, newf, [(97, 154), (640, 404)], (100, 200, 100), 3,
                               "Sq", (178, 104), (100, 200, 100), 3, 1)


def labels3():
    f = files[3]
    newf = f[:-4]
    image = cvba.readFiles(cvba.parentPath + f)
    cvba.drawRectanglesAndText(image, newf, [(107, 279), (459, 924)], (100, 200, 100), 3,
                               "Doggy", (96, 64), (100, 200, 100), 2, 0.5, 0)


def morph():
    morph_kernel = [4, 4, 4, 4, 4]
    morph_mode = [cv2.MORPH_ERODE, cv2.MORPH_DILATE, cv2.MORPH_OPEN, cv2.MORPH_CLOSE]
    bfilter_data = [[5, 75, 75], [5, 75, 200], [5, 200, 75], [3, 100, 100], [15, 200, 200]]
    bin_threshold_value = [100]
    bin_max_value = [255]
    bin_mehod = ["SELF", "OTSU"]
    index = 2
    bIndex = 0
    mIndex = 2
    for i, f in enumerate(files):
        newf = f[:-4]
        image = cvba.readFiles(cvba.parentPath + f)
        grey = cvba.convertImageToGrey(image, newf, 0)
        bf = cvba.bFilter(grey, newf, bfilter_data[index][0], bfilter_data[index][1], bfilter_data[index][2], 1)
        bin = cvba.greythreshold(bf, newf, bin_threshold_value[bIndex], bin_max_value[bIndex], bin_mehod[1], 1)
        k = np.ones((morph_kernel[mIndex], morph_kernel[mIndex]), np.uint8)
        cvba.morpbologyEx(bin, newf, k, morph_mode[mIndex], 1)


def bfilter():
    bfilter_data = [[5, 75, 75], [5, 75, 200], [5, 200, 75], [3, 100, 100], [15, 200, 200]]
    ## d=5~15 sigma 75~200 sigma_space 75~200
    ## color more color
    ## space further away
    index = 10
    for i, f in enumerate(files):
        newf = f[:-4]
        image = cvba.readFiles(cvba.parentPath + f)
        grey = cvba.convertImageToGrey(image, newf, 0)
        cvba.bFilter(grey, newf, bfilter_data[index][0], bfilter_data[index][1], bfilter_data[index][2], 1)


def otherFilter():
    oFData = [[3, "G"], [5, "G"], [9, "G"], [3, "N"], [5, "N"], [9, "N"], [3, "M"], [5, "M"], [9, "M"]]
    index = 8
    for i, f in enumerate(files):
        newf = f[:-4]
        image = cvba.readFiles(cvba.parentPath + f)
        grey = cvba.convertImageToGrey(image, newf, 0)
        cvba.blur(grey, newf, oFData[index][0], oFData[index][1], 1)


def binFilter():
    bfilter_data = [[5, 75, 75], [5, 75, 200], [5, 200, 75], [3, 100, 100], [15, 200, 200]]
    bin_threshold_value = [100]
    bin_max_value = [255]
    bin_mehod = ["SELF", "OTSU"]
    index = 2
    bIndex = 0
    for i, f in enumerate(files):
        newf = f[:-4]
        image = cvba.readFiles(cvba.parentPath + f)
        grey = cvba.convertImageToGrey(image, newf, 0)
        bf = cvba.bFilter(grey, newf, bfilter_data[index][0], bfilter_data[index][1], bfilter_data[index][2], 0)
        cvba.greythreshold(bf, newf, bin_threshold_value[bIndex], bin_max_value[bIndex], bin_mehod[1], 1)


def main():
    morph()


if __name__ == "__main__":
    # Call the main function
    main()
