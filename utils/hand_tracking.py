from cvzone.HandTrackingModule import HandDetector as CvzoneHandDetector

class HandDetector(CvzoneHandDetector):
    """
    Inherits from cvzone's HandDetector to provide modular hand detection functionality.
    """
    def __init__(self, staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5):
        super().__init__(staticMode, maxHands, modelComplexity, detectionCon, minTrackCon)
