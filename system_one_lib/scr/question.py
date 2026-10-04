import json


class Question:
    _TYPES = {list: "score", dict: "choice", type(None): "noul"}

    def __init__(self, title, text, criteria=None):
        """ 
        question() class constructor
            :param title: str
            :param text: str
            :param criteria: list, dict or None
        """
        self.title, self.text = title, text
        self.criteria = criteria
        self.type = self._TYPES.get(type(criteria))
        if self.type is None:
            raise ValueError(type(criteria))

    def to_dict(self):
        return {"title": self.title, "text": self.text,
                "type": self.type, "criteria": self.criteria}
    


class QuestionSet:
    def __init__(self, questions: list[Question]):
        """ 
        question_set() class constructor
            :param questions: list of Question objects
        """
        self.questions = questions



class QuestionEvaluator:
    def run(self, library, state=None):
        if library == "laya":
            import laya
            return laya.evaluate(data, state=state)
        elif library == "jev":
            import jev
            return jev.evaluate(data)