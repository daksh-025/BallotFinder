import streamlit as st
import pandas as pd

# Specify the path to the .xlsx file
FILE_PATH = "AlumniListFinal.xlsx"

@st.cache_data
def load_data():
    # Load the data without treating the first row as headers
    return pd.read_excel(FILE_PATH, header=None)

# Title of the app
st.title("Find Membership ID by Name or Mobile No")

try:
    # Load the data
    data = load_data()

    # Input fields for name or mobile number
    st.write("Enter either a name or a mobile number to find the corresponding Membership ID")
    name = st.text_input("Name:")
    mobile_no = st.text_input("Mobile No:")

    if st.button("Find Membership ID"):
        if name or mobile_no:
            # Access columns by position
            ballot_column_index = 0  # A corresponds to index 0 (Ballot No)
            name_column_index = 1    # B corresponds to index 1 (Name)
            mobile_column_index = 5  # F corresponds to index 5 (Mobile No)

            # Filter by name or mobile number
            filtered_data = data[
                (data.iloc[:, name_column_index].astype(str).str.lower() == name.strip().lower()) |
                (data.iloc[:, mobile_column_index].astype(str) == mobile_no)
            ]

            if not filtered_data.empty:
                ballot_no = filtered_data.iloc[0, ballot_column_index]  # Get the value from column A
                st.success(f"The corresponding Membership ID is: {ballot_no}")
            else:
                st.error("No Ballot No found for the entered Name or Mobile No.")
        else:
            st.warning("Please enter either a Name or a Mobile No.")
except FileNotFoundError:
    st.error(f"The file at '{FILE_PATH}' was not found. Please check the path and try again.")
except Exception as e:
    st.error(f"An error occurred: {e}")
