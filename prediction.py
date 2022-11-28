import streamlit as st
import joblib
import time
from PIL import Image
import numpy as np
import sklearn.externals

anomaly_model = open("model/ourmodel.pkl", "rb")
anomaly_clf = joblib.load(anomaly_model)


def predict_anomaly(data):
    # vect = lst.transform(data).toarray()
    # anomaly_clf.fit(data)
    result = anomaly_clf.predict(data)
    return result


def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)


# def load_images(file_name):
#     img = Image.open(file_name)
#     return st.image(img, width=300)

def main():
    """Anomaly detection App
    With Streamlit

  """

    st.title("Anomaly detection")
    html_temp = """
  <div style="background-color:blue;padding:10px">
  <h2 style="color:grey;text-align:center;">Streamlit App </h2>
  </div>

  """
    st.markdown(html_temp, unsafe_allow_html=True)
    # load_css('icon.css')
    # load_icon('people')

    duration = st.text_input("Enter duration")
    src_bytes = st.text_input("Enter src_bytes")
    dst_bytes = st.text_input("Enter dst_bytes")
    if st.button("Predict"):
        result = predict_anomaly([[int(duration), int(src_bytes), int(dst_bytes)]])
        # print(result)
        if result[0] == 1:
            prediction = 'normal'
        elif result[0] == -1:
            # result[0] == 1
            prediction = 'anomaly'
        st.success('Session: was classified as {}'.format(prediction))


if __name__ == "__main__":
    main()