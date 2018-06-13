from practice import commons as cm


def display_breakdown_of_user_types():
    """
    Use pandas to load chicago.csv into a dataframe, and find the most frequent hour when people start traveling.
    There isn't an hour column in this dataset, but you can create one by extracting the hour from the "Start Time"
    column. To do this, you can convert "Start Time" to the datetime datatype using the pandas to_datetime() method and
    extracting properties such as the hour with these properties.
    """
    # load data file into a dataframe
    df = cm.load_chicago_data()

    # Find the value count for each type of the user.
    # You can find the possible user types using df['User Type'].unique()
    user_types = df['User Type'].value_counts()

    print(user_types)


if __name__ == "__main__":
    display_breakdown_of_user_types()
