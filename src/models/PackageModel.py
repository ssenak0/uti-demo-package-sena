from pydantic import Field, validator
from typing import List, Union, Literal, Optional
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config

class InputImageOne(Input):
    name: Literal["inputImageOne"] = "inputImageOne"
    value: Union[List[Image], Image]
    type: Literal["object"] = "object"

    @validator("type",pre=True, always=True)
    def set_type_based_on_value(cls,value,values):
        value=values.get('value')
        if isinstance(value,Image):
            return "object"
        elif isinstance(value,list):
            return "list"
        return "object"

    class Config:
        title = "Image Input 1"

class InputImageTwo(Input):
    name: Literal["inputImageTwo"] = "inputImageTwo"
    value: Union[List[Image], Image]
    type: Literal["object"] = "object"


    @validator("type",pre=True, always=True)
    def set_type_based_on_value(cls,value,values):
        value=values.get('value')
        if isinstance(value,Image):
            return "object"
        elif isinstance(value,list):
            return "list"
        return "object"

    class Config:
        title = "Image Input 2"

class OutputImageOne(Output):
    name: Literal["outputImageOne"] = "outputImageOne"
    value: Union[List[Image], Image]
    type: Literal["object"] = "object"

    @validator("type",pre=True, always=True)
    def set_type_based_on_value(cls,value,values):
        value=values.get('value')
        if isinstance(value,Image):
            return "object"
        elif isinstance(value,list):
            return "list"
        return "object"

    class Config:
        title = "Result Output Image 1"

class OutputImageTwo(Output):
    name: Literal["outputImageTwo"] = "outputImageTwo"
    value: Union[List[Image], Image]
    type: Literal["object"] = "object"

    @validator("type",pre=True, always=True)
    def set_type_based_on_value(cls,value,values):
        value=values.get('value')
        if isinstance(value,Image):
            return "object"
        elif isinstance(value,list):
            return "list"
        return "object"

    class Config:
        title = "Result Output Image 2"

class OptionAIntegerField(Config):
    name: Literal["OptionAIntegerField"] = "OptionAIntegerField"
    value: int = Field(default=10)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Integer Field for A"

class BoolOptionTrue(Config):
    name: Literal["True"] = "True"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"
    class Config:
        title = "Enable"

class BoolOptionFalse(Config):
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"
    class Config:
        title = "Disable"

class OptionABoolField(Config):
    name: Literal["OptionABoolField"] = "OptionABoolField"
    value: Union[BoolOptionTrue, BoolOptionFalse]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Boolean Field for A"
        schema_extra = {
            "target": "value"
        }

class OptionA(Config):
    name: Literal["OptionA"] = "OptionA"
    optionAIntegerField: OptionAIntegerField
    optionABoolField: OptionABoolField
    value: Literal["OptionA"] = "OptionA"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Method A"

class OptionBFloatField(Config):
    name: Literal["OptionBFloatField"] = "OptionBFloatField"
    value: float = Field(default=1.5)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Float Field for B"

class OptionBStringField(Config):
    name: Literal["OptionBStringField"] = "OptionBStringField"
    value: str = Field(default="default_string")
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "String Field for B"

class OptionB(Config):
    name: Literal["OptionB"] = "OptionB"
    optionBFloatField: OptionBFloatField
    optionBStringField: OptionBStringField
    value: Literal["OptionB"] = "OptionB"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "Method B"

class DemoDependentDropdown(Config):
    name: Literal["demoDependentDropdown"] = "demoDependentDropdown"
    value: Union[OptionA, OptionB]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    class Config:
        title = "Select Method"
        schema_extra = {
            "target": "value"
        }




class ExecutorOneInputs(Inputs):
    inputImageOne: InputImageOne

class ExecutorTwoInputs(Inputs):
    inputImageOne: InputImageOne
    inputImageTwo: InputImageTwo


class ExecutorOneConfigs(Configs):
    demoDependentDropdown: DemoDependentDropdown

class ExecutorTwoConfigs(Configs):
    demoDependentDropdown: DemoDependentDropdown

class ExecutorOneRequest(Request):
    inputs: Optional[ExecutorOneInputs]
    configs: ExecutorOneConfigs
    class Config:
        schema_extra = {"target": "configs"}


class ExecutorTwoRequest(Request):
    inputs: Optional[ExecutorTwoInputs]
    configs: ExecutorTwoConfigs

    class Config:
        schema_extra = {"target": "configs"}


class ExecutorOneOutputs(Outputs):
    outputImageOne: OutputImageOne

class ExecutorTwoOutputs(Outputs):
    outputImageOne: OutputImageOne
    outputImageTwo: OutputImageTwo

class ExecutorOneResponse(Response):
    outputs: ExecutorOneOutputs

class ExecutorTwoResponse(Response):
    outputs: ExecutorTwoOutputs

class ExecutorOne(Config):
    name: Literal["ExecutorOne"] = "ExecutorOne"
    value: Union[ExecutorOneRequest, ExecutorOneResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "ExecutorOne"
        schema_extra = {
            "target": {
                "value": 1
            }
        }

class ExecutorTwo(Config):
    name: Literal["ExecutorTwo"] = "ExecutorTwo"
    value: Union[ExecutorTwoRequest, ExecutorTwoResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "ExecutorTwo"
        schema_extra = {
            "target": {
                "value": 1
            }
        }

class ConfigExecutor(Config):
    name: Literal["executor"] = "executor"
    value: Union[ExecutorOne, ExecutorTwo]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"

class PackageConfigs(Configs):
    executor: ConfigExecutor

class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["DemoPackage"] = "DemoPackage"
