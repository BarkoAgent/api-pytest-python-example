import allure
import pytest_check as check
class Utils():

    def assert_parameter(self, response, assertType, resultKey, resultValue, typeOfResult):
        if assertType == "contains":
            self.check_contains(response, resultKey, resultValue, typeOfResult)
        


    @allure.step("Check Contains")
    def check_contains(self, response, resultKey, resultValue, typeOfResult):

        value_list = self.json_extract(response, resultKey)
        check.is_true(value_list, "resultKey is empty")
        if(typeOfResult == "string"):
            for value in value_list:
                if check.is_instance(value, str):
                    check.is_in(str(resultValue).lower(), str(value).lower())
        if(typeOfResult == "list"):
            for value in value_list:
                if check.is_instance(value, list):
                    check.is_in(str(resultValue).lower(), str(value).lower())

    def params_extractor(self, params_file):
        validator_dict = {}
        validator_dict["resultKey"] = params_file.get('resultKey')
        validator_dict["typeOfResult"] = params_file.get('typeOfResult')
        validator_dict["resultValue"] = params_file.get('resultValue')
        validator_dict["assertType"] = params_file.get('assertType')
        params_file.pop('resultKey', None)
        params_file.pop('typeOfResult', None)
        params_file.pop('resultValue', None)
        params_file.pop('assertType', None)

        return params_file, validator_dict


    def json_extract(self, obj, key):
        arr = []
        def extract(obj, arr, key):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        if k == key:
                            arr.append(v)
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
                        
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr
        values = extract(obj, arr, key)
        return values