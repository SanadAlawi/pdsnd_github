import pandas as pd
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def popular_times_of_travel(df):
    MONTH = ['January', 'February', 'March', 'April', 'May', 'June']
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    popular_month = df['month'].mode()[0]
    popular_day = df['day'].mode()[0]
    popular_hour = df['hour'].mode()[0]
    
    return popular_hour, popular_day, MONTH[popular_month - 1]

def popular_stations_and_trip(df):
    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    
    return popular_start_station, popular_end_station, popular_trip


def trip_duration(df):
    total_travel_time = df['Trip Duration'].sum()
    avg_travel_time = df['Trip Duration'].mean()
    return total_travel_time, avg_travel_time

def user_info(df):
    user_types = df['User Type'].value_counts()
    gender_counts = None
    earliest_birth = recent_birth = common_birth = None

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        
    return user_types, gender_counts, earliest_birth, recent_birth, common_birth

def show_data(df):
    pd.set_option("display.max_columns", 200)
    gap = 5
    start_index = 0;
    end_index = gap 
    show_more = True
    while show_more:
        print(df.iloc[start_index: end_index])
        choice = input('show more 5 rows (yes / no). ')
        if choice == 'no':
            show_more = False
        start_index = end_index
        end_index += gap
        
def get_city_name():
    right_format = True
    while right_format:
        city_name = input("Would you like to see data for Chicago, New York, Washington? : ").lower().strip()
        if city_name in CITY_DATA: right_format = False
        else: print("Please enter one of the options!!!")
    return CITY_DATA[city_name]


def get_data_file(city_name):
    df = pd.read_csv(city_name)
    return df

def prompt_date_filter_options(): 
    FILTER_BY = ['month', 'day', 'both', 'none']
    filter_by = ""
    wrong_format = True
    while wrong_format:
        filter_by = input("Would you like to filter The data by month, day, both, or not at all? Type \"none\" for no time filter: ").lower().strip()
        if filter_by in FILTER_BY: wrong_format = False
        else: print("Wrong Option? Please chosse one of the options!!")
    return filter_by

def filter_data_by_month(df):
    MONTH = ['January', 'February', 'March', 'April', 'May', 'June']
    df['month'] = df['Start Time'].dt.month
    wrong_format = True
    while wrong_format:
        month = input('Which month? January, February, March, April, May, or June?').title().strip()
        if month in MONTH: wrong_format = False
        else: print('Enter valid month!!!')
    month_index = MONTH.index(month) + 1
    df = df[df['month'] == month_index]
    return df

def filter_data_by_day(df):
    DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    df['day'] = df['Start Time'].dt.day_name()
    
    wrong_format = True
    while wrong_format:
        day = input('Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday?').lower().strip().title()
        if day in DAYS: wrong_format = False
        else: print('Enter valid day!!!')
    df = df[df['day'] == day]
    return df

def filter_data_by(df, filter_by):
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    if filter_by == 'month': 
        return filter_data_by_month(df)
        
    if filter_by == 'day': 
        return filter_data_by_day(df)
        
    if filter_by == 'both':
        df = filter_data_by_month(df)
        return filter_data_by_day(df)
        
    return df

def main():
    print('Hello! Let\'s explore some US bikeshare data!')
    city_name = get_city_name()
    df = get_data_file(city_name)
    filter_by = prompt_date_filter_options()
    
    df = filter_data_by(df, filter_by)
    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    print('', end='\n\n')
    
    popular_hour, popular_day, popular_month = popular_times_of_travel(df)
    print('Popular times of travel...')
    print(f"Most common hour of day: {popular_hour}")
    print(f"Most common day of week: {popular_day}")
    print(f"Most common month: {popular_month}")
    
    print('', end='\n\n')
    
    popular_start_station, popular_end_station, popular_trip = popular_stations_and_trip(df)
    print('Popular stations and trip...')
    print(f"Most common start station: {popular_start_station}")
    print(f"Most common end station: {popular_end_station}")
    print(f"Most common trip from start to end : {popular_trip}")
    
    print('', end='\n\n')
    
    total_travel_time, avg_travel_time = trip_duration(df)
    print('Trip duration...')
    print(f'Total travel time: {total_travel_time}')
    print(f'Average travel time: {avg_travel_time}')
    
    print('', end='\n\n')
    
    user_types, gender_counts, earliest_birth, recent_birth, common_birth = user_info(df)
    print('User info...')
    print(f'Counts of each user type: {user_types}')
    print(f'Counts of each gender: {gender_counts}')
    print(f'Earliest year of birth {earliest_birth}')
    print(f'Most recent year of birth {recent_birth}')
    print(f'Most common year of birth {common_birth}')
    
    print('', end='\n\n')
    
    
    show_data(df)
    
restart = True
while restart:
    main()
    choice = input('Do you want to restart?(yes / no)')
    if choice == 'no': restart = False
        
print('', end='\n\n')
        
print('Yahoooooooooooo!!! Well Done.')