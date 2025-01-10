import streamlit as st
import pandas as pd

# Specify the path to the .xlsx file
FILE_PATH = "AlumniListFinal.xlsx"

@st.cache_data
def load_data():
    # Load the data without treating the first row as headers
    return pd.read_excel(FILE_PATH, header=None)

# Title of the app
st.title("Mobile No to Ballot No Finder")

try:
    # Load the data
    data = load_data()

    # Input for mobile number
    st.write("Enter a mobile number to find the corresponding Ballot No.")
    mobile_no = st.text_input("Mobile No:")

    if st.button("Find Ballot No"):
        if mobile_no:
            # Access columns by position
            mobile_column_index = 5  # F corresponds to index 5 (0-based indexing)
            ballot_column_index = 0  # A corresponds to index 0 (0-based indexing)

            # Filter the data
            filtered_data = data[data.iloc[:, mobile_column_index].astype(str) == mobile_no]

            if not filtered_data.empty:
                ballot_no = filtered_data.iloc[0, ballot_column_index]  # Get the value from column A
                st.success(f"The corresponding Ballot No is: {ballot_no}")
            else:
                st.error("No Ballot No found for the entered Mobile No.")
        else:
            st.warning("Please enter a Mobile No.")
except FileNotFoundError:
    st.error(f"The file at '{FILE_PATH}' was not found. Please check the path and try again.")
except Exception as e:
    st.error(f"An error occurred: {e}")
