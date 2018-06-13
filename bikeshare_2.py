import time

import pandas as pd

CITY_DATA = {'1': 'chicago.csv',
             '2': 'new_york_city.csv',
             '3': 'washington.csv'}
VALID_CITIES = {'1': 'Chicago',
                '2': 'New york city',
                '3': 'Washington'}
VALID_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
VALID_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze. e.g. 1
        (str) month - name of the month to filter by, or "all" to apply no month filter. e.g. january
        (str) day - name of the day of week to filter by, or "all" to apply no day filter. e.g. monday
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = get_city_from_user()
    print('-' * 10)

    # get user input for month (all, january, february, ... , june)
    month = get_month_from_user()
    print('-' * 10)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_day_of_week_from_user()
    print('-' * 40)
    return city, month, day


def get_day_of_week_from_user():
    """Get user input for day of week (all, monday, tuesday, ... sunday)"""
    while True:
        day = input('Select the month to explore. Enter from monday, tuesday, wednesday, thursday, friday, '
                    'saturday, sunday or all: ').lower()

        if day in VALID_DAYS:
            confirm = input("You have selected {}. Press 'y' to confirm: ".format(day.title()))

            if confirm == 'y':
                break
            else:
                print("Try again.\n")
        else:
            print("Invalid input: {}. Try again.\n".format(day))
    return day


def get_month_from_user():
    """Get user input for month (all, january, february, ... , june)"""
    while True:
        month = input('Select month to explore. Enter from january, february, march, april, may, june or all: ').lower()

        if month in VALID_MONTHS:
            confirm = input("You have selected {}. Press 'y' to confirm: ".format(month.title()))

            if confirm == 'y':
                break
            else:
                print("Try again.\n")
        else:
            print("Invalid input: {}. Try again.\n".format(month))
    return month


def get_city_from_user():
    """Get user input for the city."""
    while True:
        city = input('Select the city you want to explore. \n1. Chicago\n2. New york city\n3. Washington\n Press 1,'
                     '2 or 3 to select the city: ')

        if city in VALID_CITIES.keys():
            confirm = input("You have selected {}. Press 'y' to confirm: ".format(VALID_CITIES[city]))

            if confirm == 'y':
                break
            else:
                print("Try again.\n")
        else:
            print("Invalid input: {}. Try again.\n".format(city))
    return city


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = VALID_MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(most_common_month(df))

    # display the most common day of week
    print(most_common_day_of_week(df))

    # display the most common start hour
    print(most_common_start_hour(df))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(popular_start_station(df))

    # display most commonly used end station
    print(popular_end_station(df))

    # display most frequent combination of start station and end station trip
    print(popular_trip(df))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is {} minutes.".format(df["Trip Duration"].sum()))

    # display mean travel time
    print("Mean travel time is {} minutes.".format(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types: \n{}\n".format(df["User Type"].value_counts()))

    # Display counts of gender
    if 'Gender' in df:
        print("Counts of user types: \n{}\n".format(df['Gender'].value_counts()))
    else:
        print("Given data doesn't contain gender data.\n")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("The earliest birth year is: {}.".format(df["Birth Year"].min()))
        print("The most recent birth year is: {}.".format(df["Birth Year"].max()))
        print("The most common birth year is: {}.".format(df["Birth Year"].mode()[0]))
    else:
        print("Given data doesn't contain birth year data.\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


def get_month_name(month_of_year):
    """
    Converts the index of month in a year to name of month.
    :param month_of_year: (int) The index of month. e.g. 1 for january, 2 for february etc.
    :return: Name of the month. e.g. January.
    """
    return VALID_MONTHS[month_of_year - 1].title()


def popular_start_station(df):
    """Get most commonly used start station"""
    return "The most commonly used start station is: {}.".format(df["Start Station"].mode()[0])


def popular_end_station(df):
    """Get most commonly used end station"""
    return "The most commonly used end station is: {}.".format(df["End Station"].mode()[0])


def popular_trip(df):
    """
    Provides most popular trip. (i.e. Most commonly used start and end station combination.)
    :param df: DataFrame.
    :return: User message with popular trip stations to print.
    """
    trips_station = df.groupby(["Start Station", "End Station"])['Start Time'].count()
    sorted_trip_stations = trips_station.sort_values(ascending=False, axis=0)
    return "The most commonly used station combination is: \nStart station:{}\nEnd station:{}." \
        .format(sorted_trip_stations.index[0][0], sorted_trip_stations.index[0][1])


def most_common_month(df):
    """Get the most common month for the bike sharing service."""
    common_month = df['month'].mode()[0]
    print("Most common month is {}.".format(get_month_name(common_month)))


def most_common_day_of_week(df):
    """Get the most common day of week for the bike sharing service."""
    common_day = df['day_of_week'].mode()[0].title()
    return "Most common day is {}.".format(common_day)


def most_common_start_hour(df):
    """Get the most common start hour for the bike sharing service."""
    df['Start Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Start Hour'].mode()[0]
    return "Most common start hour is {}.".format(common_start_hour)


if __name__ == "__main__":
    main()
