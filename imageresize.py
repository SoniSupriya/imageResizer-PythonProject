import cv2

#parmeter configuration
initial_img = "sampleImg2.jpg"
output_img = "resized_image2.jpg"

 #load image
image = cv2.imread(initial_img,cv2.IMREAD_UNCHANGED)      

scale_percent = 50

#new width and height
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

result = cv2.resize(image, (new_width, new_height))

#save the resized image
cv2.imwrite(output_img, result)  