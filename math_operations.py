from pydantic import BaseModel, validator, ValidationError
from time import sleep

class UserDataValidator(BaseModel):
    name: str
    age: int

    @validator('name')
    def user_name_validator(cls, obj):
        if not obj:
            raise ValidationError
        return obj

    @validator('age')
    def age_validator(cls, obj):
        if obj <= 0:
            raise ValidationError
        return obj

class BaseUserData:
    def __init__(self, data: list, validator_class=UserDataValidator):
        self._validator_class = validator_class
        self._data = data
        self._validated_data = []
        self._result = None

    def _validate_data(self):
        for rec in self._data:
            try:
                temp = self._validator_class.parse_obj(rec)
            except ValidationError as e:
                pass
            else:
                self._validated_data.append(temp)

        return self._validated_data


class MedianCalculator(BaseUserData):

    def __call__(self, *args, **kwargs):
        sleep(3)
        return self._validate_data()

class AgeRangeCalculator(BaseUserData):

    def __call__(self, *args, **kwargs):
        sleep(3)
        return self._validate_data()

class UniqueNamesCalculator(BaseUserData):

    def __call__(self, *args, **kwargs):
        sleep(3)
        return self._validate_data()

