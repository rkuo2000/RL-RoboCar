import cv2
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('output.mp4', fourcc, 30.0, (1280,  720))

for i in range(1000): # merge 1000 .png into .mp4
    print(i)
    frame = cv2.imread("screenshot_"+str(i)+".png")
    video.write(frame)
