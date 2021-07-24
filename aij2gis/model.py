import onnx
import os
import numpy as np


class Model:
    def __init__(self):
        os.system("pip install onnx")
        self.model1 = onnx.load("model.onnx")
        self.model2 = onnx.load("model.onnx")

    def predict(self, model, inp):
        return model.predict(inp)

    def enum(self, model_out):
        return model_out.argmax(1)

    def image_preprocessing(self, image):
        image = image.copy().resize((55, 55)).convert("L")
        x = np.array(image).reshape((1, 1, 55, 55, 1))
        return x

    def get_result(self, image):
        ind = 0
        inp = self.image_preprocessing(image)
        out1 = self.enum(self.predict(self.model1, inp))
        if out1[ind] == 1:
            out = out1 + self.enum(self.predict(self.model2, inp))
        else:
            out = out1
        return out
