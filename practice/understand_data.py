from practice import commons as cm


def understand_data():
    """
    Let's use pandas to better understand the bike share data! Use this code editor to explore chicago.csv and answer
    the questions below. The file included here is a mini version of one of the actual data files you will work with for
    the project. It only includes 400 rows, but the structure and columns are the same.

    1. What columns are in this dataset?
    2. Are there any missing values?
    3. What are the different types of values in each column?
    """

    df = cm.load_chicago_data().head()

    # What columns are in this data set?
    print("Column names: \n{}".format(df.columns))

    # Are there any missing values?
    print("Does column contains NAN: \n{}".format(df.isnull().any(0)))

    # What are the different types of values in each column?
    for column in df.columns:
        value_counts = df[column].value_counts()
        unique_values = df[column].unique()
        print("Column {} has {} values. Unique values are \n{}".format(column, value_counts, unique_values))
