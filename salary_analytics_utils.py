"""
Salary Analytics Utilities
Generates detailed analytical datasets and insights for salary prediction
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

def generate_salary_dataset(n_samples=1000, random_state=42):
    """Generate synthetic salary dataset"""
    np.random.seed(random_state)
    
    data = {
        'Years_Experience': np.random.randint(0, 30, n_samples),
        'Education_Level': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_samples),
        'Technical_Skills_Count': np.random.randint(1, 15, n_samples),
        'Certifications': np.random.randint(0, 10, n_samples),
        'Job_Role': np.random.choice(['Developer', 'Data Scientist', 'Manager', 'Analyst', 'Architect'], n_samples),
        'Industry': np.random.choice(['IT', 'Finance', 'Healthcare', 'Manufacturing', 'Retail'], n_samples),
        'Location': np.random.choice(['Tier-1 City', 'Tier-2 City', 'Tier-3 City'], n_samples),
        'Performance_Rating': np.random.uniform(2.5, 5.0, n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Generate salary
    salary = 300000
    salary = salary + (df['Years_Experience'] * 50000)
    
    education_map = {'High School': 0, 'Bachelor': 200000, 'Master': 400000, 'PhD': 600000}
    salary = salary + df['Education_Level'].map(education_map)
    
    salary = salary + (df['Technical_Skills_Count'] * 30000)
    salary = salary + (df['Certifications'] * 25000)
    
    role_map = {'Developer': 100000, 'Data Scientist': 150000, 'Manager': 200000, 'Analyst': 80000, 'Architect': 250000}
    salary = salary + df['Job_Role'].map(role_map)
    
    industry_map = {'IT': 150000, 'Finance': 200000, 'Healthcare': 100000, 'Manufacturing': 80000, 'Retail': 50000}
    salary = salary + df['Industry'].map(industry_map)
    
    location_map = {'Tier-1 City': 200000, 'Tier-2 City': 100000, 'Tier-3 City': 50000}
    salary = salary + df['Location'].map(location_map)
    
    salary = salary + (df['Performance_Rating'] * 100000)
    salary = salary + np.random.normal(0, 100000, n_samples)
    salary = np.maximum(salary, 200000)
    
    df['Salary'] = salary.astype(int)
    
    return df

def analyze_salary_by_education(df):
    """Analyze salary statistics by education level"""
    print("[1] Analyzing salary by education level...")
    
    education_stats = df.groupby('Education_Level')['Salary'].agg([
        ('Count', 'count'),
        ('Mean_Salary', 'mean'),
        ('Median_Salary', 'median'),
        ('Min_Salary', 'min'),
        ('Max_Salary', 'max'),
        ('Std_Dev', 'std')
    ]).round(2)
    
    education_stats.to_csv('/home/ubuntu/salary_by_education_stats.csv')
    print("✓ Saved: salary_by_education_stats.csv")
    return education_stats

def analyze_salary_by_role(df):
    """Analyze salary statistics by job role"""
    print("[2] Analyzing salary by job role...")
    
    role_stats = df.groupby('Job_Role')['Salary'].agg([
        ('Count', 'count'),
        ('Mean_Salary', 'mean'),
        ('Median_Salary', 'median'),
        ('Min_Salary', 'min'),
        ('Max_Salary', 'max'),
        ('Std_Dev', 'std')
    ]).round(2)
    
    role_stats.to_csv('/home/ubuntu/salary_by_role_stats.csv')
    print("✓ Saved: salary_by_role_stats.csv")
    return role_stats

def analyze_salary_by_industry(df):
    """Analyze salary statistics by industry"""
    print("[3] Analyzing salary by industry...")
    
    industry_stats = df.groupby('Industry')['Salary'].agg([
        ('Count', 'count'),
        ('Mean_Salary', 'mean'),
        ('Median_Salary', 'median'),
        ('Min_Salary', 'min'),
        ('Max_Salary', 'max'),
        ('Std_Dev', 'std')
    ]).round(2)
    
    industry_stats.to_csv('/home/ubuntu/salary_by_industry_stats.csv')
    print("✓ Saved: salary_by_industry_stats.csv")
    return industry_stats

def analyze_salary_by_location(df):
    """Analyze salary statistics by location"""
    print("[4] Analyzing salary by location...")
    
    location_stats = df.groupby('Location')['Salary'].agg([
        ('Count', 'count'),
        ('Mean_Salary', 'mean'),
        ('Median_Salary', 'median'),
        ('Min_Salary', 'min'),
        ('Max_Salary', 'max'),
        ('Std_Dev', 'std')
    ]).round(2)
    
    location_stats.to_csv('/home/ubuntu/salary_by_location_stats.csv')
    print("✓ Saved: salary_by_location_stats.csv")
    return location_stats

def analyze_experience_impact(df):
    """Analyze impact of experience on salary"""
    print("[5] Analyzing experience impact...")
    
    # Create experience bins
    df_exp = df.copy()
    df_exp['Experience_Group'] = pd.cut(df_exp['Years_Experience'], 
                                         bins=[0, 5, 10, 15, 20, 30],
                                         labels=['0-5 years', '5-10 years', '10-15 years', '15-20 years', '20+ years'])
    
    exp_stats = df_exp.groupby('Experience_Group')['Salary'].agg([
        ('Count', 'count'),
        ('Mean_Salary', 'mean'),
        ('Median_Salary', 'median'),
        ('Min_Salary', 'min'),
        ('Max_Salary', 'max'),
        ('Std_Dev', 'std')
    ]).round(2)
    
    exp_stats.to_csv('/home/ubuntu/salary_by_experience_stats.csv')
    print("✓ Saved: salary_by_experience_stats.csv")
    return exp_stats

def analyze_skills_impact(df):
    """Analyze impact of technical skills on salary"""
    print("[6] Analyzing technical skills impact...")
    
    # Create skills bins
    df_skills = df.copy()
    df_skills['Skills_Group'] = pd.cut(df_skills['Technical_Skills_Count'],
                                        bins=[0, 3, 6, 9, 12, 15],
                                        labels=['1-3 skills', '4-6 skills', '7-9 skills', '10-12 skills', '13-15 skills'])
    
    skills_stats = df_skills.groupby('Skills_Group')['Salary'].agg([
        ('Count', 'count'),
        ('Mean_Salary', 'mean'),
        ('Median_Salary', 'median'),
        ('Min_Salary', 'min'),
        ('Max_Salary', 'max'),
        ('Std_Dev', 'std')
    ]).round(2)
    
    skills_stats.to_csv('/home/ubuntu/salary_by_skills_stats.csv')
    print("✓ Saved: salary_by_skills_stats.csv")
    return skills_stats

def generate_salary_predictions(df, n_predictions=50):
    """Generate sample salary predictions for different profiles"""
    print("[7] Generating sample salary predictions...")
    
    predictions = []
    
    profiles = [
        {'Education': 'Bachelor', 'Experience': 2, 'Skills': 5, 'Role': 'Developer', 'Industry': 'IT', 'Location': 'Tier-1 City'},
        {'Education': 'Bachelor', 'Experience': 5, 'Skills': 8, 'Role': 'Developer', 'Industry': 'IT', 'Location': 'Tier-1 City'},
        {'Education': 'Master', 'Experience': 3, 'Skills': 7, 'Role': 'Data Scientist', 'Industry': 'Finance', 'Location': 'Tier-1 City'},
        {'Education': 'Master', 'Experience': 7, 'Skills': 10, 'Role': 'Data Scientist', 'Industry': 'Finance', 'Location': 'Tier-1 City'},
        {'Education': 'Bachelor', 'Experience': 8, 'Skills': 9, 'Role': 'Manager', 'Industry': 'IT', 'Location': 'Tier-1 City'},
        {'Education': 'Master', 'Experience': 10, 'Skills': 11, 'Role': 'Manager', 'Industry': 'Finance', 'Location': 'Tier-1 City'},
        {'Education': 'PhD', 'Experience': 5, 'Skills': 12, 'Role': 'Architect', 'Industry': 'IT', 'Location': 'Tier-1 City'},
        {'Education': 'Bachelor', 'Experience': 1, 'Skills': 3, 'Role': 'Analyst', 'Industry': 'Healthcare', 'Location': 'Tier-2 City'},
        {'Education': 'High School', 'Experience': 3, 'Skills': 2, 'Role': 'Analyst', 'Industry': 'Retail', 'Location': 'Tier-3 City'},
        {'Education': 'Master', 'Experience': 12, 'Skills': 14, 'Role': 'Architect', 'Industry': 'Finance', 'Location': 'Tier-1 City'},
    ]
    
    for i, profile in enumerate(profiles):
        # Calculate estimated salary based on profile
        salary = 300000
        salary += profile['Experience'] * 50000
        
        education_map = {'High School': 0, 'Bachelor': 200000, 'Master': 400000, 'PhD': 600000}
        salary += education_map[profile['Education']]
        
        salary += profile['Skills'] * 30000
        
        role_map = {'Developer': 100000, 'Data Scientist': 150000, 'Manager': 200000, 'Analyst': 80000, 'Architect': 250000}
        salary += role_map[profile['Role']]
        
        industry_map = {'IT': 150000, 'Finance': 200000, 'Healthcare': 100000, 'Manufacturing': 80000, 'Retail': 50000}
        salary += industry_map[profile['Industry']]
        
        location_map = {'Tier-1 City': 200000, 'Tier-2 City': 100000, 'Tier-3 City': 50000}
        salary += location_map[profile['Location']]
        
        salary = max(salary, 200000)
        
        predictions.append({
            'Profile_ID': i + 1,
            'Education_Level': profile['Education'],
            'Years_Experience': profile['Experience'],
            'Technical_Skills': profile['Skills'],
            'Job_Role': profile['Role'],
            'Industry': profile['Industry'],
            'Location': profile['Location'],
            'Predicted_Salary': int(salary),
            'Salary_Range_Min': int(salary * 0.9),
            'Salary_Range_Max': int(salary * 1.1)
        })
    
    pred_df = pd.DataFrame(predictions)
    pred_df.to_csv('/home/ubuntu/salary_predictions_samples.csv', index=False)
    print("✓ Saved: salary_predictions_samples.csv")
    return pred_df

def generate_salary_insights(df):
    """Generate key insights about salary data"""
    print("[8] Generating salary insights...")
    
    insights = []
    
    # Overall statistics
    insights.append(f"Total Employees: {len(df)}")
    insights.append(f"Average Salary: ₹{df['Salary'].mean():,.0f}")
    insights.append(f"Median Salary: ₹{df['Salary'].median():,.0f}")
    insights.append(f"Salary Range: ₹{df['Salary'].min():,.0f} - ₹{df['Salary'].max():,.0f}")
    insights.append(f"Salary Std Dev: ₹{df['Salary'].std():,.0f}")
    
    # Education insights
    insights.append(f"\nHighest avg salary by education: {df.groupby('Education_Level')['Salary'].mean().idxmax()}")
    insights.append(f"Lowest avg salary by education: {df.groupby('Education_Level')['Salary'].mean().idxmin()}")
    
    # Role insights
    insights.append(f"Highest avg salary by role: {df.groupby('Job_Role')['Salary'].mean().idxmax()}")
    insights.append(f"Lowest avg salary by role: {df.groupby('Job_Role')['Salary'].mean().idxmin()}")
    
    # Industry insights
    insights.append(f"Highest avg salary by industry: {df.groupby('Industry')['Salary'].mean().idxmax()}")
    insights.append(f"Lowest avg salary by industry: {df.groupby('Industry')['Salary'].mean().idxmin()}")
    
    # Location insights
    insights.append(f"Highest avg salary by location: {df.groupby('Location')['Salary'].mean().idxmax()}")
    insights.append(f"Lowest avg salary by location: {df.groupby('Location')['Salary'].mean().idxmin()}")
    
    # Experience insights
    high_exp = df[df['Years_Experience'] >= 15]['Salary'].mean()
    low_exp = df[df['Years_Experience'] < 5]['Salary'].mean()
    insights.append(f"\nAvg salary (15+ years experience): ₹{high_exp:,.0f}")
    insights.append(f"Avg salary (<5 years experience): ₹{low_exp:,.0f}")
    insights.append(f"Experience Premium: {((high_exp/low_exp - 1) * 100):.1f}%")
    
    # Skills insights
    high_skills = df[df['Technical_Skills_Count'] >= 10]['Salary'].mean()
    low_skills = df[df['Technical_Skills_Count'] < 5]['Salary'].mean()
    insights.append(f"\nAvg salary (10+ skills): ₹{high_skills:,.0f}")
    insights.append(f"Avg salary (<5 skills): ₹{low_skills:,.0f}")
    insights.append(f"Skills Premium: {((high_skills/low_skills - 1) * 100):.1f}%")
    
    # Write insights to file
    with open('/home/ubuntu/salary_insights.txt', 'w') as f:
        f.write("SALARY PREDICTION SYSTEM - KEY INSIGHTS\n")
        f.write("="*60 + "\n\n")
        for insight in insights:
            f.write(insight + "\n")
    
    print("✓ Saved: salary_insights.txt")
    return insights

def main():
    print("="*80)
    print("SALARY ANALYTICS UTILITIES - GENERATING DETAILED DATASETS")
    print("="*80)
    print()
    
    # Generate main dataset
    print("Generating salary dataset...")
    df = generate_salary_dataset(n_samples=1000)
    print(f"✓ Dataset created: {df.shape[0]} records\n")
    
    # Generate analytical datasets
    analyze_salary_by_education(df)
    analyze_salary_by_role(df)
    analyze_salary_by_industry(df)
    analyze_salary_by_location(df)
    analyze_experience_impact(df)
    analyze_skills_impact(df)
    generate_salary_predictions(df)
    generate_salary_insights(df)
    
    print("\n" + "="*80)
    print("ANALYTICS COMPLETE - All datasets generated successfully")
    print("="*80)

if __name__ == "__main__":
    main()
