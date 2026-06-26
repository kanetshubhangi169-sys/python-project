import json
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Model

IMG_SIZE = (224, 224)

train_gen = ImageDataGenerator(
    rescale=1./255
)

train_data = train_gen.flow_from_directory(
    "dataset",
    target_size=IMG_SIZE,
    batch_size=4,
    class_mode="categorical"
)

print("Class Mapping:")
print(train_data.class_indices)

with open("class_names.json", "w") as f:
    json.dump(train_data.class_indices, f)

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    pooling="avg",
    input_shape=(224,224,3)
)

base_model.trainable = False

output = Dense(
    train_data.num_classes,
    activation="softmax"
)(base_model.output)

model = Model(
    inputs=base_model.input,
    outputs=output
)

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    train_data,
    epochs=10
)

model.save("face_recognition_model.h5")

print("Training Completed")