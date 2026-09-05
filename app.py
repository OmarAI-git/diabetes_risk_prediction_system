import streamlit as st
import pandas as pd
import requests
from src.mapping import MappingData

@st.cache_data()
def get_data():
    return pd.read_csv('data/raw_data/diabetes_012_health_indicators_BRFSS2015.csv')

title = st.container()
data = st.container()
features = st.container()
predict = st.container()
metrics = st.container()

st.session_state.user_data = {}


with title:
    st.title('Data Science Project')
    st.header('Wlecome to my end to end project (diabetes prediction system)')


with data:
    st.header('Dataset')
    st.subheader('diabetes_012_health_indicators_BRFSS2015')
    st.text('This data is from kaggle')

    data = get_data()

    st.write(data.head(5))


with features:
    st.markdown('## Select the features')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.session_state.user_data['HighBP'] = st.radio('High BP', ['No high BP', 'high BP'], horizontal = True)
        st.session_state.user_data['HighChol'] = st.radio('High cholesterol', ['No high cholesterol', 'High cholesterol'], horizontal = True)
        st.session_state.user_data['CholCheck'] = st.radio('Cholesterol check', ['No cholesterol check', 'Yes cholesterol check'])
        st.session_state.user_data['BMI'] = st.number_input('BMI', min_value = 12., max_value = 99., step = 0.1, format = '%0.1f')
        st.session_state.user_data['Smoker'] = st.radio('Smoker', ['No', 'Yes'], horizontal = True)
        st.session_state.user_data['Stroke'] = st.radio('Stroke', ['No', 'Yes'], horizontal = True)
        st.session_state.user_data['Age'] = st.number_input('Age', min_value = 18, max_value = 100)

    with col2:
        st.session_state.user_data['HeartDiseaseorAttack'] = st.radio('Heart disease', ['No', 'Yes'], horizontal = True)
        st.session_state.user_data['PhysActivity'] = st.radio('Physical activity', ['No', 'Yes'], horizontal = True)
        st.session_state.user_data['Fruits'] = st.radio('Consume Fruits', ['No', 'Yes'], horizontal = True)
        st.session_state.user_data['Veggies'] = st.radio('Consume Vegetables', ['No', 'Yes'], horizontal = True)
        st.session_state.user_data['HvyAlcoholConsump'] = st.radio('Heavy drinkers', ['No', 'Yes'], horizontal = True)
        st.session_state.user_data['AnyHealthcare'] = st.radio('Have any kind of health care coverage', ['No', 'Yes'], horizontal = True)
        st.session_state.user_data['Sex'] = st.radio('Gender', ['Female', 'Male'], horizontal = True)

    with col3:
        st.session_state.user_data['NoDocbcCost'] = st.radio('Was there a time when you needed to see a doctor but could not because of cost', ['No', 'Yes'], horizontal = True)
        st.session_state.user_data['GenHlth'] = st.selectbox('Would you say that in general your health', ['excellent', 'very good', 'good', 'fair', 'poor'])
        st.session_state.user_data['MentHlth'] = st.number_input('For how many days during the past 30 days was your mental health not good?', min_value = 1, max_value = 30)
        st.session_state.user_data['PhysHlth'] = st.number_input('For how many days during the past 30 days was your physical health not good?', min_value = 1, max_value = 30)
        st.session_state.user_data['DiffWalk'] = st.radio('Do you have serious difficulty walking or climbing stairs?', ['No', 'Yes'], horizontal = True)


map = MappingData(st.session_state.user_data)

data = map.mapping_data()


with predict:
    col1, col2, col3 = st.columns(3)
    with col2:
        predict_button = st.button('Predict', icon = '▶️', width = 100, type = 'primary')
        if predict_button:
            response = requests.post('http://127.0.0.1:8000/predict', json = data)


            result = response.json()

            prediction = result['Diabetes Prediction']

            st.write('### Prediction result:')

            if prediction == 0:
               st.success('### \t No diabetes')
            elif prediction == 1:
                st.warning('### \t Pre diabetes')
            elif prediction == 2:
                st.error('### \t Diabetes')


