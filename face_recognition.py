from __future__ import print_function
import json
from os.path import abspath
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

test_url = 'https://www.ibm.com/ibm/ginni/images' \
           '/ginni_bio_780x981_v4_03162016.jpg'

service = VisualRecognitionV3(
    '2018-03-19',
    url='https://gateway.watsonplatform.net/visual-recognition/api',
    iam_apikey='EeL-xEkEsYicxbmcG5aFh9rMH5YFHACCVnfJIVh9M0M-'


)
car_path = abspath("camera.zip")
try:
    with open(car_path, 'rb') as images_file:
        car_results = service.classify(
            images_file=images_file,
            threshold='0.1',
            classifier_ids=['default']).get_result()
        print(json.dumps(car_results, indent=2))
except WatsonApiException as ex:
    print(ex)



classifiers = service.list_classifiers().get_result()
print(json.dumps(classifiers, indent=2))

face_path = abspath('opencv_frame_0.PNG')
with open(face_path, 'rb') as image_file:
    face_result = service.detect_faces(images_file=image_file).get_result()
    print(json.dumps(face_result, indent=2))

