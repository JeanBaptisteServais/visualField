
import dlib
import cv2
import os

class Foldering:
    def __init__(self, folderPath):
        self.folderPath = folderPath
        self.listPicture = []
  
    def runFolder(self):
        self.listPicture = os.listdir(self.folderPath)

    def getterListPicture(self):
        return self.listPicture








class PictureReader:

    def __init__(self, pathPicture, picture):

        self.pathPicture = pathPicture
        self.picture = picture
        self.pictureGray = None


    def makeACopy(self):
        
        copy = self.picture()
        return copy


    def reader(self):

        self.picture = cv2.imread(self.pathPicture.format(picture))
        self.picture = cv2.resize(self.picture, (1260, 940))
        self.pictureGray = cv2.cvtColor(self.picture, cv2.COLOR_BGR2GRAY)


    def displayPicture(self, mode, picture):

        cv2.imshow("picture", picture)
        cv2.waitKey(mode)
        cv2.destroyAllWindows()



    def getterPicture(self):
        return self.picture


    def getterGrayPicture(self):
        return self.pictureGray








class Dlib:

    def __init__(self):

        self.landmarks = []
        self.detector = dlib.get_frontal_face_detector()

        self.predictor = None


    def landmarksLoad(self):
        pass


    def getterDetector(self):
        return self.detector





class headPosition:

    def __init__(self, detector, grayPicture, picture):

        self.detector = detector
        self.grayPicture = grayPicture
        self.picture = picture

        self.squareHead = []
        self.headLandmarks = [1, 20, 25, 17, 9]

        self.facesPoints = None


    def localisationFace(self):
        self.facesPoints = self.detector(grayPicture)


    def squareHead(self):
        pass

    def detectFace(self):
        faces = self.detector(self.grayPicture)
        self.facesPoints = [(face.left(), face.top(), face.right(),
                             face.bottom()) for face in faces]


    def displayRectangleFace(self, showing):

        copy = self.picture

        for face in self.facesPoints:
 
            x, y, w, h = face
            cv2.rectangle(copy, (x, y), (w, h),(0, 0, 255), 2)

        return copy


    def getterFacePoints(self):
        return self.facesPoints

    def getterSquareHead(self):
        return self.squareHead







class eyesTracking:

    def __init__(self):
        self.fieldVisual = fieldVisual
        self.eyesRightLandmarks = [37, 38, 39, 40, 41, 42]
        self.eyesLeftLandmarks  = [43, 44, 45, 46, 47, 48]

    def localiseEye(self):
        pass

    def fieldVisual(self):
        pass

    def getterField(self):
        return self.fieldVisual





if __name__ == "__main__":

    
    PATH_PICTURE = r"C:\Users\jeanbaptiste\Desktop\visuVisu\pictures"

    pictureFolder = Foldering(PATH_PICTURE)
    pictureFolder.runFolder()
    listPicture = pictureFolder.getterListPicture()

    print("[INFO] run picture folder.")
    print("there are: {}".format(len(listPicture)))


    for picture in listPicture:

        print("[INFO] reading picture.")
        print("in course: {}".format(picture))

        pathPicture = r"C:\Users\jeanbaptiste\Desktop\visuVisu\pictures\{}"

        picturing = PictureReader(pathPicture, picture)
        picturing.reader()

        picture = picturing.getterPicture()
        grayPicture = picturing.getterGrayPicture()

    
        print("[INFO] dlib detections.")

        dlibClass = Dlib()
        detector = dlibClass.getterDetector()


        print("[INFO] dlib FACE detections.")

        heading = headPosition(detector, grayPicture, picture)
        heading.localisationFace()
        heading.detectFace()
        facePoints = heading.getterFacePoints()

        print("faces points detected: {}".format(len(facePoints)))

        

        pictureRectFace = heading.displayRectangleFace(True)

        picturing.displayPicture(0, pictureRectFace)









        [print("") for i in range(5)]







