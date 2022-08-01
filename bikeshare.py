import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    inp = input("Enter city name chicago, new york city or washington : ")

    while inp.lower() not in CITY_DATA.keys():
        print("Enter valid city name: ")
        inp = input("Enter city name: ")

    city = inp.lower()


    # get user input for month (all, january, february, ... , june)
    inp2 = input("Enter month name or just say \'all\' to apply no month filter: ")
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while inp2.lower() not in months:
        print("Enter valid month name: ")
        inp2 = input("Enter month name:")
    month = inp2.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    inp3 = input("Enter weekday or just say \'all\' again to apply no day filter: ")
    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while inp3.lower() not in days:
        print("Enter valid weekday: ")
        inp3 = input("Enter weekday: ")

    day = inp3.lower()
    print('-'*40)
    return city, month, day


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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print('Most Frequent Month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print('Most Frequent Day:', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most commonly used Start Station:', popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most commonly used End Station:', popular_end)

    # display most frequent combination of start station and end station trip
    df['Station Comb'] = df['Start Station'] + '' + df['End Station']
    popular_comb = df['Station Comb'].mode()[0]
    print('Most commonly used combination of start station and end station trip:', popular_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ',total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('user types are: ')
    print(user_types)

    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('count of each gender: ')
        print(gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_by = df['Birth Year'].min()
        recent_by = df['Birth Year'].max()
        cmmn_by = df['Birth Year'].mode()[0]

        print('earliest, most recent, and most common year of birth: ')
        print(earliest_by)
        print(recent_by)
        print(cmmn_by)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    print(df.head())
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_data.lower() != 'yes':
            return
        start_loc += 5
        print(df.iloc[start_loc:start_loc+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            view_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_data.lower() != 'yes':
                break
            display_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
