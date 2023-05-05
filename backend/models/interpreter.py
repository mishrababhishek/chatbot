from models.sequence_to_vector.seq2vec import SequenceToVector
from models.vector_to_class.vec2class import VectorToClass
import json

class Interpreter:
    def __init__(self) -> None:
        self.s2v: SequenceToVector = None
        self.v2c : VectorToClass = None

    def parse(self, sequence: str):
        return self.v2c.get_class(self.s2v.get_embedding(sequence))
    
    @staticmethod
    def create_new_interpreter(name: str):
        s2v = SequenceToVector()
        v2c = VectorToClass()
        s2v.initialize()
        v2c.initialize(s2v)
        with open(f"models/saved/{name}.json", "w") as f:
            json.dump({
                "s2v": s2v.to_json(),
                "v2c": v2c.to_json()
            }, f, indent=1)
    
    @staticmethod
    def load_interpreter(name: str = "default_stem"):
        interpreter = Interpreter()
        _file = open(f"models/saved/{name}.json", "r")
        saved_model = json.load(_file)
        interpreter.s2v = SequenceToVector.from_json(saved_model["s2v"])
        interpreter.v2c = VectorToClass.from_json(saved_model["v2c"])
        return interpreter

        