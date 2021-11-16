import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    # What is the average age of men?
    men = df.loc[(df['sex'] == 'Male')]
    average_age_men = men['age'].mean()
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?

    percentage_bachelors = (df.loc[(df['education'] == 'Bachelors')].shape[0]) / df['education'].shape[0] * 100
    percentage_bachelors = round(percentage_bachelors, 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    educated_groups = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    
    educatedCount = (educated_groups.shape[0])
    educated50K = (educated_groups.loc[educated_groups['salary'] == '>50K'].shape[0])

    higher_education = educatedCount


    lower_education = df.loc[~df['education'].isin(['Bachelors', 'Masters','Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = educated50K / educatedCount * 100
    higher_education_rich = round(higher_education_rich, 1)

    count50K = df.loc[df['salary'] == '>50K'].shape[0]
    lower_education_rich = lower_education.loc[(lower_education['salary'] == '>50K')].shape[0] / lower_education.shape[0] * 100
    lower_education_rich = round(lower_education_rich,1)###
    higher_education_rich = round(higher_education_rich, 1)
    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[(df['hours-per-week'] == 1)].shape[0]


    rich_min_workers = df.loc[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].shape[0]


    rich_percentage = rich_min_workers / num_min_workers * 100
    rich_percentage = round(rich_percentage, 1)

    # What country has the highest percentage of people that earn >50K?
    rich_people = df.loc[df['salary'] == '>50K']
    rich_countries = rich_people['native-country'].value_counts().sort_index(ascending=True)


    people = df['native-country'].value_counts().sort_index(ascending=True)
    richest_countries = (rich_countries / people * 100).sort_values(ascending=False)


    highest_earning_country = richest_countries.first_valid_index()

    highest_earning_country_percentage = round(richest_countries.iloc[0], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    RichIndia = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = RichIndia['occupation'].value_counts().first_valid_index()
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
