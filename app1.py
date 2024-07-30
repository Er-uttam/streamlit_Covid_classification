# import streamlit as st
# import pandas as pd
# import pickle as pk
import pandas as pd
import pickle as pk
import streamlit as st

# Title 
st.title('COVID Classification')

# form start
Name = st.text_input("Enter Name")
Cough_symptoms = st.radio("Cough symptoms",[True,False])
Fever = st.radio("Fever",[True,False])
Sore_throat = st.radio("Sore throat",[True,False])
Shortness_of_breath = st.radio("Shortness of breath",[True,False])
Headache = st.radio("Headache",[True,False])
Age_60_above = st.selectbox("Is Age 60 above ?", ["Yes","No"])
Sex = st.selectbox("Gender",["Male","Female"])
Known_contact = st.selectbox("Known Contact",['Abroad','Contact with confirmed','Other'])

if st.button("Submit"):
    #Create a DataFrame
    df = pd.DataFrame({
        "Cough_symptoms":[Cough_symptoms],
        "Fever":[Fever],
        "Sore_throat":[Sore_throat],
        "Shortness_of_breath":[Shortness_of_breath],
        "Headache":[Headache],
        "Age_60_above":[Age_60_above],
        "Sex":[Sex],
        "Known_contact":[Known_contact]
        })

#Encoding the data
    if Age_60_above == "No":
        df["Age_60_above"] = 0
    else:
        df["Age_60_above"] = 1

    if Sex == "Female":
        df['Sex'] = 0
    else:
        df['Sex'] = 1
    if Known_contact == "Abroad":
        df["Known_contact"] = 0
    if Known_contact == "Other":
        df["Known_contact"] = 2
    else:
        df["Known_contact"] = 1

    # open a file , where you stored the pickled data
    file = open('model.pickle','rb')
    
    # dumb information to that file
    my_model = pk.load(file)
    result = my_model.predict(df)
    if int(result) == 1:
        output = "Positive"
    else:
        output = "Negative" 
    st.write(f"{Name} got the result of  : ",output)
    st.write("Form Submitted")
