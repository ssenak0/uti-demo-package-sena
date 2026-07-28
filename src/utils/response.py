from sdks.novavision.src.helper.package import PackageHelper
from components.UtiDemoPackageSena.src.models.PackageModel import (
    PackageModel, PackageConfigs, ConfigExecutor, 
    ExecutorOne, ExecutorOneResponse, ExecutorOneOutputs, OutputImageOne,
    ExecutorTwo, ExecutorTwoResponse, ExecutorTwoOutputs, OutputImageTwo,
)

def build_response_one(context):
    outputImageOne = OutputImageOne(value=context.output_image_one)
    outputs = ExecutorOneOutputs(outputImageOne=outputImageOne)
    response = ExecutorOneResponse(outputs=outputs)
    executorOne = ExecutorOne(value=response)
    configExecutor = ConfigExecutor(value=executorOne)
    packageConfigs = PackageConfigs(executor=configExecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

def build_response_two(context):
    outputImageOne = OutputImageOne(value=context.output_image_one)
    outputImageTwo = OutputImageTwo(value=context.output_image_two)
    outputs = ExecutorTwoOutputs(outputImageOne=outputImageOne, outputImageTwo=outputImageTwo)
    response = ExecutorTwoResponse(outputs=outputs)
    executorTwo = ExecutorTwo(value=response)
    configExecutor = ConfigExecutor(value=executorTwo)
    packageConfigs = PackageConfigs(executor=configExecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
