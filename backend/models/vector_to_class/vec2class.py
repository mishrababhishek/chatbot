from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
import config
import models.vector_to_class.utils as utils
from models.sequence_to_vector.seq2vec import SequenceToVector
import numpy as np

class VectorToClass:
    def __init__(self):
        self.epochs: int = None
        self.embedding:int = None
        self.learning_rate: float = None
        self.batch_size: int = None
        self.classes: list = []
        self.model: Sequential = None

    def initialize(self, s2v: SequenceToVector):
        self.classes = utils.get_intends()
        self.classes.append("no_indent")
        self.setup_config()
        self.create_model()
        train_x, train_y = self.generate_traning_data(s2v)
        self.model.fit(train_x, train_y, self.batch_size, self.epochs, verbose=2)
    
    def setup_config(self):
        self.embedding = config.config_file["embedding"]
        this_config = config.config_file["vector_to_class"]
        self.epochs = this_config["epochs"]
        self.learning_rate = this_config["learning_rate"]
        self.batch_size = this_config["batch_size"]

    def create_model(self):
        network: list = config.config_file["vector_to_class"]["netowrk"]
        self.model = Sequential(name="Vector_to_Class")
        first_layer = network.pop(0)
        self.model.add(Dense(first_layer["neurons"], first_layer["activation"], input_shape=(self.embedding,)))
        for net in network:
            match net["type"]:
                case "dense":
                    self.model.add(Dense(net["neurons"], net["activation"]))
                case "dropout":
                    self.model.add(Dropout(net["rate"]))
        self.model.add(Dense(len(self.classes), "softmax"))
        self.model.compile(optimizer=Adam(self.learning_rate), loss="categorical_crossentropy", metrics=["accuracy"])

    def generate_traning_data(self, s2v: SequenceToVector):
        train_x = []
        train_y = []
        querys = utils.get_query_with_intends()
        for query in querys:
            indent = query["intent"]
            for question in query["questions"]:
                train_x.append(s2v.get_embedding(question))
                train_y.append(utils.one_hot_encode(self.classes.index(indent), len(self.classes)))
        train_x.append(s2v.get_embedding(""))
        train_y.append(utils.one_hot_encode(self.classes.index("no_indent"), len(self.classes)))
        return np.asarray(train_x), np.asarray(train_y)
    
    def get_class(self, embedding: np.ndarray):
        embedding = embedding.reshape(1,-1)
        result = self.model.predict(embedding, verbose=0)[0]
        result = np.argsort(result)[::-1]
        return self.classes[result[0]]
    
    def to_json(self):
        return {
            "model": self.model.get_config(),
            "weights": [weights.tolist() for weights in self.model.get_weights()]
        }
    
    @staticmethod
    def from_json(data: dict):
        v2c = VectorToClass()
        v2c.classes = utils.get_intends()
        v2c.classes.append("no_indent")
        v2c.model = Sequential.from_config(data["model"])
        v2c.model.set_weights([np.asarray(weights) for weights in data["weights"]])
        return v2c