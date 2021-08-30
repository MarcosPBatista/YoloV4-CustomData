import cv2 as cv
import time

COLORS = [(0,255,255), (255, 255,0), (255, 0, 255)]

class_names = []

with open('coco.names', 'r') as f:
    class_names = [cname.strip() for cname in f.readlines()]

cap = cv.VideoCapture(0)

net = cv.dnn.readNet(r"C:\Users\marco\Documents\GitHub\LearningYolo\YoloV4-CustomData\yolo4-tiny.weights", r"C:\Users\marco\Documents\GitHub\LearningYolo\YoloV4-CustomData\yolo4-tiny.cfg")