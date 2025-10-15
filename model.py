class NeuralNetwork:
    def __init__(self, layers, dropout_rate=0.0):
        self.layers = layers
        self.dropout_rate = dropout_rate

    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def backward(self, grad):
        for layer in reversed(self.layers):
            grad = layer.backward(grad)
        return grad

    def update_weights(self, learning_rate):
        for layer in self.layers:
            layer.update_weights(learning_rate)