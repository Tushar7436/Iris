import streamlit as st
import pickle

# Load the model
model = pickle.load(open('savedmodel.sav', 'rb'))

def main():
    st.title("Flower Prediction App")

    sepal_length = st.slider("Sepal Length", 0.0, 10.0)
    sepal_width = st.slider("Sepal Width", 0.0, 10.0)
    petal_length = st.slider("Petal Length", 0.0, 10.0)
    petal_width = st.slider("Petal Width", 0.0, 10.0)

    if st.button("Predict"):
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
        st.success(f"The predicted flower class is {result}")

if __name__ == '__main__':
    main()
