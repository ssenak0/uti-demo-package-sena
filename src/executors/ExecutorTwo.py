import os
import sys
import cv2

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.UtiDemoPackageSena.src.models.PackageModel import PackageModel
from components.UtiDemoPackageSena.src.utils.response import build_response_two

class ExecutorTwo(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.image_one = self.request.get_param("inputImageOne")
        self.image_two = self.request.get_param("inputImageTwo")
        self.method = self.request.get_param("demoDependentDropdown")

        if self.method == "OptionA":
            self.val_int = self.request.get_param("optionAIntegerField")
            self.val_bool = self.request.get_param("optionABoolField")
        else:
            self.val_float = self.request.get_param("optionBFloatField")
            self.val_string = self.request.get_param("optionBStringField")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def process(self, img_one, img_two):
        height, width = img_one.shape[:2]
        img_two_resized = cv2.resize(img_two, (width, height))
        blended_image = cv2.addWeighted(img_one, 0.5, img_two_resized, 0.5, 0)
        difference_image = cv2.absdiff(img_one, img_two_resized)
        return blended_image, difference_image

    def run(self):
        img_one = Image.get_frame(img=self.image_one, redis_db=self.redis_db)
        img_two = Image.get_frame(img=self.image_two, redis_db=self.redis_db)
        
        result = self.process(img_one.value, img_two.value)
        
        img_one.value = result[0]
        self.output_image_one = Image.set_frame(img=img_one, package_uID=self.uID, redis_db=self.redis_db)
        
        img_two.value = result[1]
        self.output_image_two = Image.set_frame(img=img_two, package_uID=self.uID, redis_db=self.redis_db)
        
        packageModel = build_response_two(self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()
