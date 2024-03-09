import CV2_Basic_Algorithm as cvba
import cv2

files = ["people.jpg", "pic1.jpg", "pic2.jpg", "pic3.jpg"]


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
                               "Doggy", (96, 64), (100, 200, 100), 2, 0.5)


def process():
    filter_kernal_size = [3, ]
    filter_method = [["G"], ["N"], ["M"]]

    bfilter_data = [[5, 75, 75]]
    ## d=5~15 sigma 75~200 sigma_space 75~200

    bin_threshold_value = [10, ]
    bin_max_value = [200, ]
    bin_mehod = ["SELF", "OTSU"]

    morph_kernel = [[2, 2]]
    morph_mode = [cv2.MORPH_ERODE, cv2.MORPH_DILATE, cv2.MORPH_OPEN, cv2.MORPH_CLOSE]

    for f in files:
        newf = f[:-4]
        image = cvba.readFiles(cvba.parentPath + f)
        ##grey = convertImageToGrey(image, newf)


def main():
    labels3()


if __name__ == "__main__":
    # Call the main function
    main()
