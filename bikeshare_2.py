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
    # Define a list of valid cities
    valid_cities = ['chicago','new york city','washington']
    # Initializing Variables
    city = ''
    # While loop to get lower valid cities input
    while city.lower() not in valid_cities:
       city = input("Please enter the city (chicago, new york city, washington): ").lower()
       if city not in valid_cities:
           print("Invalid input. Please try again.")
        
    print(f"You selected:{city.title()}")

    # get user input for month (all, january, february, ... , june)
    # Define a list of valid months
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    # Initializing Variables
    month = ''
    # While loop to get lower valid months input
    while month.lower() not in valid_months:
        month = input("Please enter the month (all, january, february, march, april, may,           june): ").lower()
        if month not in valid_months:
            print("Invalid input. Please try again.")
            
    print(f"You have selected: {month.title()}")
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    # Define a list of valid days
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',               'saturday', 'sunday']
    # Initializing Variables
    day = ''
    # While loop to get lower valid days input
    while day.lower() not in valid_days:
        day = input("Please enter the month (all, monday, tuesday, wednesday, thursday,         friday, saturday, sunday): ").lower()
        if day not in valid_days:
            print("Invalid input. Please try again.")
            
    print(f"You have selected: {day.title()}")

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day from 'Start Time'
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

     # Filter by month 
    if month != 'all':
        df = df[df['month'].str.lower() == month.lower()]

    # Filter by day 
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day.lower()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month from 'Start Time'
    df['month'] = df['Start Time'].dt.month
    # Most common month
    most_common_month = df['month'].mode()[0]

    print(f"The most common month is: {most_common_month}")

    # display the most common day of week
    
    # Extract day of week from 'Start Time'
    df['day_of_week'] = df['Start Time'].dt.day_name
    # Most common month
    most_common_day_of_week = df['day_of_week'].mode()[0]
    
    print(f"The most common day of week is: {most_common_day_of_week}")

    # display the most common start hour
    # Extract hour from 'Start Time'
    df['hour'] = df['Start Time'].dt.hour
    # Most common month
    most_common_start_hour = df['hour'].mode()[0]

    print(f"The most common start hour is: {most_common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # Most common start station
    most_common_start_station = df['Start Station'].mode()[0]

    print(f"The most commonly used start station is: {most_common_start_station}")

    # TO DO: display most commonly used end station
    # Most common end station
    most_common_end_station = df['End Station'].mode()[0]
    
    print(f"The most commonly used end station is: {most_common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    # Group satrt station and end station
    most_frequent_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    # Most frequent combination of start station and end station trip
    most_frequent_trip_count = df.groupby(['Start Station', 'End Station']).size().max()
    
    print(f"The most frequent trip is from '{most_frequent_trip[0]}' to              '{most_frequent_trip[1]}', occurring {most_frequent_trip_count} times.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    # sum the travel time
    total_travel_time = df['Trip Duration'].sum()
    # Convert total travel time from seconds to hours, minutes, and seconds
    total_hours = total_travel_time // 3600
    total_minutes = (total_travel_time % 3600) // 60
    total_seconds = total_travel_time % 60
    print(f"Total travel time: {total_hours} h, {total_minutes} m,  {total_seconds} s")
    # TO DO: display mean travel time
    # mean the travel time
    mean_travel_time = df['Trip Duration'].mean()
    # Convert mean travel time from seconds to minutes
    mean_travel_time_minutes = mean_travel_time / 60
    print(f"The mean travel time is: {mean_travel_time_minutes:.2f} min")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_type_counts)

    # TO DO: Display counts of gender
    # Display counts of gender (if available)
    if 'Gender' in df.columns:
        user_gender_counts = df['Gender'].value_counts()
        print("\nCounts of user gender:")
        print(user_gender_counts)
    else:
        print("\nGender data not available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        # Display the earliest year of birth  
        earliest_birth_year = df['Birth Year'].min()
        # Display the most recent year of birth
        most_recent_birth_year = df['Birth Year'].max()
        # Display the most common year of birth
        most_common_birth_year = df['Birth Year'].mode()[0]
    
        print(f"Earliest year of birth: {earliest_birth_year}")
        print(f"Most recent year of birth: {most_recent_birth_year}")
        print(f"Most common year of birth: {most_common_birth_year}")
    else: 
        print("\nBirth year data not available for this city.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_raw_data(df):
    #individual a variable index
    start_index = 0
    # While loop to view individual trip data
    while True:
        user_input = input("Would you like to see 5 rows of raw data? (yes/no): ").lower()
        
        if user_input == "yes":
            # Check if there are more rows to display
            if start_index < len(df):
                # Display the next 5 lines of raw data
                print(df.iloc[start_index:start_index + 5])
                # Update the start index for the next iteration
                start_index += 5
            else:
                print("No more data to display.")
                break
        # Exit the loop if the user says 'no'       
        elif user_input == "no":
            print("Exiting the data display.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

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


if __name__ == "__main__":
	main()
