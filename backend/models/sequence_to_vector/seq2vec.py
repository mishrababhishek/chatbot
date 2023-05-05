from keras.models import Sequential, Model
from keras.layers import Dense
from keras.optimizers import Adam
import config
import models.sequence_to_vector.utils as utils
import numpy as np
import matplotlib.pyplot as plt

class SequenceToVector:
    def __init__(self):
        self.window: int = None
        self.embedding: int = None
        self.epochs: int = None
        self.learning_rate: float = None
        self.batch_size: int = None
        self.tokenization: str = None
        self.tokens: list = None
        self.word_to_id: dict = {}
        self.id_to_word: dict = {}
        self.sequential: Sequential = None
        self.model: Model = None
        
    def initialize(self):
        self.setup_config()
        self.tokens: list = utils.sequence_to_token(utils.questions_to_sequece(), self.tokenization)
        self.map_tokens()
        self.create_model()
        train_x, train_y = self.generate_traning_data()
        self.sequential.fit(train_x, train_y, self.batch_size, self.epochs, verbose=2)

    def map_tokens(self):
        for index, token in enumerate(set(self.tokens)):
            self.word_to_id[token] = index
            self.id_to_word[index] = token

    def setup_config(self):
        this_config = config.config_file["sequence_to_vector"]
        self.window = this_config["window"]
        self.embedding = config.config_file["embedding"]
        self.epochs = this_config["epochs"]
        self.tokenization = this_config["tokenization"]
        self.learning_rate = this_config["learning_rate"]
        self.batch_size = this_config["batch_size"]

    def create_model(self):
        self.sequential = Sequential(name="Sequence_to_Vector")
        self.sequential.add(Dense(self.embedding, activation="relu", input_shape=(len(self.word_to_id),)))
        self.sequential.add(Dense(len(self.word_to_id), activation="softmax"))
        self.sequential.compile(optimizer=Adam(self.learning_rate), loss="categorical_crossentropy", metrics=["accuracy"])
        self.model = Model(inputs=self.sequential.input, outputs=self.sequential.layers[0].output)

    def generate_traning_data(self):
        train_X = []
        train_y = []
        for index, _ in enumerate(self.tokens):
            ids = utils.concat_iterables(
                range(max(0, index - self.window), index),
                range(index, min(len(self.tokens), index + self.window + 1))
            )
            for _id in ids:
                if _id == index:
                    continue
                train_X.append(utils.one_hot_encode([self.word_to_id[self.tokens[index]]], len(self.word_to_id)))
                train_y.append(utils.one_hot_encode([self.word_to_id[self.tokens[_id]]], len(self.word_to_id)))
        ids = []
        for word in utils.get_stopwords():
            if word in self.word_to_id:
                ids.append(self.word_to_id[word])
        train_X.append(utils.one_hot_encode(ids, len(self.word_to_id)))
        train_y.append(utils.one_hot_encode([], len(self.word_to_id)))
        train_X.append(utils.one_hot_encode([], len(self.word_to_id)))
        train_y.append(utils.one_hot_encode([], len(self.word_to_id)))
        return np.asarray(train_X), np.asarray(train_y)
    
    def get_embedding(self, sequence: str):
        tokens = utils.sequence_to_token(sequence, self.tokenization)
        ids = []
        for token in tokens:
            if token in self.word_to_id:
                ids.append(self.word_to_id[token])
        model_input = utils.one_hot_encode(ids, len(self.word_to_id))
        model_input = np.asarray([model_input])
        return self.model.predict(model_input, verbose="0")[0]

    
    def visualize(self):
        x = []
        y = []
        tokens = set(self.tokens)
        print(self.tokens)
        for token in tokens:
            embedding = self.get_embedding(token)
            x.append(embedding[0])
            y.append(embedding[1])
        fig, ax = plt.subplots()
        ax.scatter(x, y, color="blue")
        for i, token in enumerate(tokens):
            ax.annotate(token, (x[i], y[i]))
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Plot with words and there Embedding')
        plt.show()

    def to_json(self):
        return {
            "model": self.model.get_config(),
            "weights": [weights.tolist() for weights in self.model.get_weights()],
            "tokens": self.tokens,
            "tokenization": self.tokenization,
            "word_to_id": self.word_to_id,
            "id_to_word": self.id_to_word,
        }
    
    @staticmethod
    def from_json(data: dict):
        s2v = SequenceToVector()
        s2v.tokens = data["tokens"]
        s2v.tokenization = data["tokenization"]
        s2v.word_to_id = data["word_to_id"]
        s2v.id_to_word = data["id_to_word"]
        s2v.model = Model.from_config(data["model"])
        s2v.model.set_weights([np.asarray(weights) for weights in data["weights"]])
        return s2v
