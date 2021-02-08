Final Task of QTI-Bootcamp 2021
--------------------------------

## topic
Computer Vision

build an object detection apps that build on python language using flask

apps run at port 5000

### API routes:
#### a
0.0.0.0:5000/detections


params: images: file(could be multiple image file)

return:
```
{
    "response": [
        {
            "detections": [
                {
                    "class": "chair",
                    "confidence": 76.57
                },
                {
                    "class": "person",
                    "confidence": 71.95
                }
            ],
            "image": "IMG_3541.jpg"
        }
    ]
}
```

#### b
0.0.0.0:5000/image


params: images: file(could be multiple image file)

return:
image file that already processed

*nb:
weight data are on google drive

https://drive.google.com/drive/folders/1wKIHbWN7Vv01tQSNvmDV04hBfGKXaaij?usp=sharing

\

### reference
https://svitla.com/blog/image-processing-and-computer-vision-libraries-for-python