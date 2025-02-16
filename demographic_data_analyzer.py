import pandas as pd

# What is renovate.json used for?



def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # Count of each race
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # Percentage of people with a Bachelor's degree
    percentage_bachelors = (df['education'].value_counts(normalize=True)['Bachelors']) * 100

    # Higher education (Bachelors, Masters, Doctorate)
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentage of people earning >50K with/without higher education
    higher_education_rich = (higher_education['salary'] == '>50K').mean() * 100
    lower_education_rich = (lower_education['salary'] == '>50K').mean() * 100

    # Minimum working hours per week
    min_work_hours = df['hours-per-week'].min()

    # Percentage of people who work the minimum hours and earn >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

    # Country with highest percentage of high earners
    country_salary_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    highest_earning_country = (country_salary_counts / country_counts * 100).idxmax()
    highest_earning_country_percentage = (country_salary_counts / country_counts * 100).max()

    # Most common high-earning occupation in India
    top_IN_occupation = df.loc[
        (df['native-country'] == 'India') & (df['salary'] == '>50K'),
        'occupation'
    ].value_counts().idxmax()

    if print_data:
        print("Race Count:\n", race_count)
        print("Average Age of Men:", average_age_men)
        print(f"Percentage with Bachelors: {percentage_bachelors:.2f}%")
        print(f"Percentage with Advanced Education earning >50K: {higher_education_rich:.2f}%")
        print(f"Percentage without Advanced Education earning >50K: {lower_education_rich:.2f}%")
        print(f"Min work hours: {min_work_hours}")
        print(f"Rich Percentage among Min Workers: {rich_percentage:.2f}%")
        print(f"Highest earning country: {highest_earning_country} ({highest_earning_country_percentage:.2f}%)")
        print(f"Top occupation in India among >50K earners: {top_IN_occupation}")

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }