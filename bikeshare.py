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
    Cycles through until the user inputs a correct City, caters for typos    
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter the City you would like to look at: chicago, new york city or washington? - ")
    while city not in ["chicago", "washington", "new york city"]:
        city = input("Please enter the City you would like to look at: chicago, new york city or washington? - ")

    if city == ["chicago", "washington", "new york city"]:
        print("city: {} ".format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter the month you would like to look at: all, january, february through to june? - ")

    if month not in ["all", "january","february","march","april","may","june"]:
        month = input("Ooops!! Please enter the month you would like to look at: all, january, february through to june? - ")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("Please enter the month you would like to look at: all, monday, tuesday...sunday? - ")
    if day not in ["all", "monday","tuesday","wednesday","thursday","friday","saturday","sunday"]:
        day = input("Ooops!! Please enter the month you would like to look at: all, monday, tuesday...sunday? - ")

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
    filename = CITY_DATA[city.lower()]
    df = pd.read_csv(filename)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #create station combo
    df['station_combo'] = df['Start Station'] + df['End Station']

    # filter by month if applicable
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most frequent month: ", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("Most frequent day of week: ", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("Most frequent hour: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most common journey start point: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most common journey end point: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("Most common journey: ", df['station_combo'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: ", df['Trip Duration'].sum()//60//60," hours")

    # TO DO: display mean travel time
    print("Total travel time: ", df['Trip Duration'].mean()//60, " minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Types: ", df.groupby(['User Type'])['User Type'].count())

    # TO DO: Display counts of gender
    if 'Gender' in df:
    # Only access Gender column in this case
        print("Gender breakdown: ", df.groupby(['Gender'])['Gender'].count())
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the data')
    if 'Birth Year' in df:
    # TO DO: Display earliest, most recent, and most common year of birth
        print("Birth Year for Oldest, Youngest & Most Frequent users: ", df['Birth Year'].min(), " , ", df['Birth Year'].max(), " , ", df['Birth Year'].mode()[0] )
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_data(df):

    start_loc = 0
    end_loc = start_loc + 5
    view_data = input("would you like to view 5 rows of data? Please enter yes or no")

    while view_data == "yes":
        print(df[start_loc:end_loc])
        start_loc += 5
        end_loc += 5
        view_data = input("would you like to view 5 more rows?")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_data(df)

        restart = input('\nDid you enjoy this? Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

try:
    if __name__ == "__main__":
    	main()

except KeyError:
    print("ooops!  No results found, try again")
    if __name__ == "__main__":
    	main()
