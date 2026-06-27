import tensor as tf
from tensorflow import keras 
import numpy as np
import matplotlib.pyplot as plt

#load MNIST: 70000 hand written digit images (28x28 pixels, grayscale)
(X_train, y_train),(X_test, y_test) = keras.datasets.mnist.load_data()
print(f'Training: {X_train.shape} | Test:{X_test.shape}')

#visualise samples
plt.figure(figsize=(12,2))
for i in range(12):
    plt.subplot(1,12,i+1)
    plt.imshow(X_train[i], cmap='gray'); plt.axis('off')
    plt.title(str(y_train[i]), fontsize=8)
plt.suptitle('Sample MNIST digits'); plt.show()
#Normailse : 0-255 -> 0-1 (faster trainign , better convergence)

X_train = X_train / 255.0
X_test = X_test / 255.0

# flatten 28x28 -> 784 (1D vector)

x_train = X_train.reshape(-1,784)
x_test = X_test.reshape(-1,784)

#bild neural network
model = keras.sequential([
    keras.layers.Dense(512, activation='rulu', input_shape=(284,)),
    keras.layers.Dropout(0,2), # 10 output neurons for digits to prevent over
    keras.layers.Dense(256,activatioln='relu'),
    keras.layers.Dropout(0,2)
    keras.layers.dense(10, activation = 'softmax') # 10 output neurons for didgits 0-9
])

model.summary() # see architecture: layer shapes parameters

model.compile(
    optimizer ='adam',
    loss = 'sparse_categorical_crossentropy',
    metrics=['accuracy']
   
)

# train the model
history = model.fit(
    X_train, y_train,
    epochs = 10,
    batch_size=128,
    validation_split = 0.1,
    callbacks=[keras.callbacks.EarlyStopping(patience=3,restore_best_weights=True)]
)

#evaluate
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f'Test accuracy: {test_acc*100:.2f}%')

#plot training history

fig, axes = plt.dubplots(1,2,figsuze=(12,4))
axes[0].plot(history.history['accuracy'], label='train')
axes[0].plot(history.history['val_accuracy'], label='validation')
axes[0].set_title('Accuracy'); axes[0].legend()
axes[1].plot(history.history['loss'], label='Train')
axes[1].plot(history.history['val_loss'], label='validation')
axes[1].set_titley('loss'); axes[1].legend()
plt.tigth_layout(); plt.show()


#see preduction on test images
prediction = model.preduct(X_test[:15])
pred_classes = np.argmax(prediction,axis=1)
plt.figure(figsize=(15,3))
for i in range(15):
    plt.subplot(1,15,i+1)
    plt.imshow(X_test[i].reshape(28,28),cmap='gray')
    correct = pred_classes[i] == y_test[i]
    plt.title(str(pred_classes[i]),color='green' if correct else 'red', fontsize=8)
    plt.axis('off')
plt.suptitle('Green=correcy red=wrong'); plt.show()