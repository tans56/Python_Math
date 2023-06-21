from tensorflow import keras
import data_reader


EPOCHS = 20

dr = data_reader.DataReader()

model = keras.Sequential([
    keras.layers.Dense(3),                      # 첫번째 층은 3개의 유닛을 가지는 레이어 구성
    keras.layers.Dense(128, activation="relu"),  # 두번째 층은 128개의 유닛을 가지는 레이어 구성
    keras.layers.Dense(3, activation="softmax") # 세번째 층은 3개의 유닛을 가지는 레이어 구성
])

'''
metrics
    - 어떤 것을 기준으로 성능을 체크할것인지 정의함
    - accuracy : 정확도를 기준으로 모델의 성능을 평가함
sparse_categorical_crossentropy
    - 모델이 어떤 문제를 어떤 카테고리로 잘 분류 했는지 쉽게 확인 할수 있음    
'''
model.compile(optimizer="adam", metrics=["accuracy"], loss="sparse_categorical_crossentropy")

print("*********************** Training Start ============================ ")
model.fit(dr.train_X, dr.train_Y,epochs=EPOCHS, validation_data=(dr.test_X, dr.test_Y))