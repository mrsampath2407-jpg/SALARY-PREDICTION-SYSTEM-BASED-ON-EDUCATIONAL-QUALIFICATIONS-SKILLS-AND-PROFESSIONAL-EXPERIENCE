"""
Salary Prediction System using Machine Learning
Predicts salary based on educational qualifications, skills, and professional experience
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

# Set style for visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 10

def generate_salary_dataset(n_samples=1000, random_state=42):
    """Generate a synthetic salary dataset based on professional attributes"""
    np.random.seed(random_state)
    
    # Generate features
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
    
    # Generate salary based on features with realistic relationships
    salary = 300000  # Base salary
    
    # Add experience component
    salary = salary + (df['Years_Experience'] * 50000)
    
    # Add education component
    education_map = {'High School': 0, 'Bachelor': 200000, 'Master': 400000, 'PhD': 600000}
    salary = salary + df['Education_Level'].map(education_map)
    
    # Add skills component
    salary = salary + (df['Technical_Skills_Count'] * 30000)
    
    # Add certifications component
    salary = salary + (df['Certifications'] * 25000)
    
    # Add job role component
    role_map = {'Developer': 100000, 'Data Scientist': 150000, 'Manager': 200000, 'Analyst': 80000, 'Architect': 250000}
    salary = salary + df['Job_Role'].map(role_map)
    
    # Add industry component
    industry_map = {'IT': 150000, 'Finance': 200000, 'Healthcare': 100000, 'Manufacturing': 80000, 'Retail': 50000}
    salary = salary + df['Industry'].map(industry_map)
    
    # Add location component
    location_map = {'Tier-1 City': 200000, 'Tier-2 City': 100000, 'Tier-3 City': 50000}
    salary = salary + df['Location'].map(location_map)
    
    # Add performance component
    salary = salary + (df['Performance_Rating'] * 100000)
    
    # Add some noise
    salary = salary + np.random.normal(0, 100000, n_samples)
    
    # Ensure salary is positive
    salary = np.maximum(salary, 200000)
    
    df['Salary'] = salary.astype(int)
    
    return df

def preprocess_data(df):
    """Preprocess the dataset for modeling"""
    df_processed = df.copy()
    
    # Encode categorical variables
    le_education = LabelEncoder()
    le_job_role = LabelEncoder()
    le_industry = LabelEncoder()
    le_location = LabelEncoder()
    
    df_processed['Education_Level'] = le_education.fit_transform(df_processed['Education_Level'])
    df_processed['Job_Role'] = le_job_role.fit_transform(df_processed['Job_Role'])
    df_processed['Industry'] = le_industry.fit_transform(df_processed['Industry'])
    df_processed['Location'] = le_location.fit_transform(df_processed['Location'])
    
    return df_processed, {
        'education': le_education,
        'job_role': le_job_role,
        'industry': le_industry,
        'location': le_location
    }

def train_models(X_train, X_test, y_train, y_test):
    """Train multiple regression models"""
    models = {}
    results = {}
    
    # Model 1: Linear Regression
    print("Training Linear Regression...")
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    
    models['Linear Regression'] = lr_model
    results['Linear Regression'] = {
        'predictions': y_pred_lr,
        'mse': mean_squared_error(y_test, y_pred_lr),
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred_lr)),
        'mae': mean_absolute_error(y_test, y_pred_lr),
        'r2': r2_score(y_test, y_pred_lr)
    }
    
    # Model 2: Random Forest
    print("Training Random Forest...")
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    
    models['Random Forest'] = rf_model
    results['Random Forest'] = {
        'predictions': y_pred_rf,
        'mse': mean_squared_error(y_test, y_pred_rf),
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred_rf)),
        'mae': mean_absolute_error(y_test, y_pred_rf),
        'r2': r2_score(y_test, y_pred_rf)
    }
    
    # Model 3: Gradient Boosting
    print("Training Gradient Boosting...")
    gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    gb_model.fit(X_train, y_train)
    y_pred_gb = gb_model.predict(X_test)
    
    models['Gradient Boosting'] = gb_model
    results['Gradient Boosting'] = {
        'predictions': y_pred_gb,
        'mse': mean_squared_error(y_test, y_pred_gb),
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred_gb)),
        'mae': mean_absolute_error(y_test, y_pred_gb),
        'r2': r2_score(y_test, y_pred_gb)
    }
    
    return models, results

def plot_salary_distribution(df):
    """Plot salary distribution"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Histogram
    axes[0].hist(df['Salary'], bins=50, color='steelblue', edgecolor='black', alpha=0.7)
    axes[0].set_xlabel('Salary (INR)', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Frequency', fontsize=11, fontweight='bold')
    axes[0].set_title('Distribution of Salaries in Dataset', fontsize=12, fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)
    
    # Box plot
    axes[1].boxplot(df['Salary'], vert=True)
    axes[1].set_ylabel('Salary (INR)', fontsize=11, fontweight='bold')
    axes[1].set_title('Salary Box Plot', fontsize=12, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/salary_distribution.png', dpi=300, bbox_inches='tight')
    print("Saved: salary_distribution.png")
    plt.close()

def plot_model_comparison(results):
    """Compare model performance metrics"""
    models = list(results.keys())
    metrics = ['r2', 'mae', 'rmse']
    
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    
    # R² Score
    r2_scores = [results[m]['r2'] for m in models]
    axes[0].bar(models, r2_scores, color=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8, edgecolor='black')
    axes[0].set_ylabel('R² Score', fontsize=11, fontweight='bold')
    axes[0].set_title('Model R² Score Comparison', fontsize=12, fontweight='bold')
    axes[0].set_ylim([0, 1])
    for i, v in enumerate(r2_scores):
        axes[0].text(i, v + 0.02, f'{v:.4f}', ha='center', fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)
    
    # MAE
    mae_scores = [results[m]['mae'] for m in models]
    axes[1].bar(models, mae_scores, color=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8, edgecolor='black')
    axes[1].set_ylabel('Mean Absolute Error (INR)', fontsize=11, fontweight='bold')
    axes[1].set_title('Model MAE Comparison', fontsize=12, fontweight='bold')
    for i, v in enumerate(mae_scores):
        axes[1].text(i, v + 5000, f'{v:,.0f}', ha='center', fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    # RMSE
    rmse_scores = [results[m]['rmse'] for m in models]
    axes[2].bar(models, rmse_scores, color=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8, edgecolor='black')
    axes[2].set_ylabel('Root Mean Squared Error (INR)', fontsize=11, fontweight='bold')
    axes[2].set_title('Model RMSE Comparison', fontsize=12, fontweight='bold')
    for i, v in enumerate(rmse_scores):
        axes[2].text(i, v + 5000, f'{v:,.0f}', ha='center', fontweight='bold')
    axes[2].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/model_performance_comparison.png', dpi=300, bbox_inches='tight')
    print("Saved: model_performance_comparison.png")
    plt.close()

def plot_predictions_vs_actual(results, y_test):
    """Plot predictions vs actual values"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    
    for idx, (model_name, result) in enumerate(results.items()):
        predictions = result['predictions']
        
        axes[idx].scatter(y_test, predictions, alpha=0.5, s=30, color='steelblue', edgecolors='black', linewidth=0.5)
        
        # Add perfect prediction line
        min_val = min(y_test.min(), predictions.min())
        max_val = max(y_test.max(), predictions.max())
        axes[idx].plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
        
        axes[idx].set_xlabel('Actual Salary (INR)', fontsize=11, fontweight='bold')
        axes[idx].set_ylabel('Predicted Salary (INR)', fontsize=11, fontweight='bold')
        axes[idx].set_title(f'{model_name}\nR² = {result["r2"]:.4f}', fontsize=12, fontweight='bold')
        axes[idx].legend()
        axes[idx].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/predictions_vs_actual.png', dpi=300, bbox_inches='tight')
    print("Saved: predictions_vs_actual.png")
    plt.close()

def plot_feature_importance(models, feature_names):
    """Plot feature importance for tree-based models"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Random Forest
    rf_importance = models['Random Forest'].feature_importances_
    rf_indices = np.argsort(rf_importance)[-10:]
    axes[0].barh(range(len(rf_indices)), rf_importance[rf_indices], color='#ff7f0e', alpha=0.8, edgecolor='black')
    axes[0].set_yticks(range(len(rf_indices)))
    axes[0].set_yticklabels([feature_names[i] for i in rf_indices])
    axes[0].set_xlabel('Importance', fontsize=11, fontweight='bold')
    axes[0].set_title('Random Forest - Top 10 Feature Importance', fontsize=12, fontweight='bold')
    axes[0].grid(axis='x', alpha=0.3)
    
    # Gradient Boosting
    gb_importance = models['Gradient Boosting'].feature_importances_
    gb_indices = np.argsort(gb_importance)[-10:]
    axes[1].barh(range(len(gb_indices)), gb_importance[gb_indices], color='#2ca02c', alpha=0.8, edgecolor='black')
    axes[1].set_yticks(range(len(gb_indices)))
    axes[1].set_yticklabels([feature_names[i] for i in gb_indices])
    axes[1].set_xlabel('Importance', fontsize=11, fontweight='bold')
    axes[1].set_title('Gradient Boosting - Top 10 Feature Importance', fontsize=12, fontweight='bold')
    axes[1].grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/feature_importance.png', dpi=300, bbox_inches='tight')
    print("Saved: feature_importance.png")
    plt.close()

def plot_salary_by_education(df):
    """Plot salary distribution by education level"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Box plot
    education_order = ['High School', 'Bachelor', 'Master', 'PhD']
    df_sorted = df.copy()
    df_sorted['Education_Level'] = pd.Categorical(df_sorted['Education_Level'], categories=education_order, ordered=True)
    df_sorted = df_sorted.sort_values('Education_Level')
    
    sns.boxplot(data=df_sorted, x='Education_Level', y='Salary', ax=axes[0], palette='Set2')
    axes[0].set_xlabel('Education Level', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Salary (INR)', fontsize=11, fontweight='bold')
    axes[0].set_title('Salary Distribution by Education Level', fontsize=12, fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)
    
    # Violin plot
    sns.violinplot(data=df_sorted, x='Education_Level', y='Salary', ax=axes[1], palette='Set2')
    axes[1].set_xlabel('Education Level', fontsize=11, fontweight='bold')
    axes[1].set_ylabel('Salary (INR)', fontsize=11, fontweight='bold')
    axes[1].set_title('Salary Distribution Density by Education Level', fontsize=12, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/salary_by_education.png', dpi=300, bbox_inches='tight')
    print("Saved: salary_by_education.png")
    plt.close()

def plot_salary_by_role_and_industry(df):
    """Plot salary by job role and industry"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # By Job Role
    role_salary = df.groupby('Job_Role')['Salary'].mean().sort_values(ascending=False)
    axes[0].bar(role_salary.index, role_salary.values, color='steelblue', alpha=0.8, edgecolor='black')
    axes[0].set_xlabel('Job Role', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Average Salary (INR)', fontsize=11, fontweight='bold')
    axes[0].set_title('Average Salary by Job Role', fontsize=12, fontweight='bold')
    axes[0].tick_params(axis='x', rotation=45)
    for i, v in enumerate(role_salary.values):
        axes[0].text(i, v + 20000, f'{v:,.0f}', ha='center', fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)
    
    # By Industry
    industry_salary = df.groupby('Industry')['Salary'].mean().sort_values(ascending=False)
    axes[1].bar(industry_salary.index, industry_salary.values, color='#ff7f0e', alpha=0.8, edgecolor='black')
    axes[1].set_xlabel('Industry', fontsize=11, fontweight='bold')
    axes[1].set_ylabel('Average Salary (INR)', fontsize=11, fontweight='bold')
    axes[1].set_title('Average Salary by Industry', fontsize=12, fontweight='bold')
    axes[1].tick_params(axis='x', rotation=45)
    for i, v in enumerate(industry_salary.values):
        axes[1].text(i, v + 20000, f'{v:,.0f}', ha='center', fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/salary_by_role_industry.png', dpi=300, bbox_inches='tight')
    print("Saved: salary_by_role_industry.png")
    plt.close()

def main():
    print("="*80)
    print("SALARY PREDICTION SYSTEM - MACHINE LEARNING ANALYSIS")
    print("="*80)
    
    # Generate dataset
    print("\n[1] Generating synthetic salary dataset...")
    df = generate_salary_dataset(n_samples=1000)
    df.to_csv('/home/ubuntu/salary_data.csv', index=False)
    print(f"Dataset generated: {df.shape[0]} records, {df.shape[1]} features")
    print(f"Salary range: ₹{df['Salary'].min():,.0f} - ₹{df['Salary'].max():,.0f}")
    
    # Preprocess data
    print("\n[2] Preprocessing data...")
    df_processed, encoders = preprocess_data(df)
    
    # Prepare features and target
    X = df_processed.drop('Salary', axis=1)
    y = df_processed['Salary']
    feature_names = X.columns.tolist()
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"Training set: {X_train_scaled.shape[0]} samples")
    print(f"Test set: {X_test_scaled.shape[0]} samples")
    
    # Train models
    print("\n[3] Training regression models...")
    models, results = train_models(X_train_scaled, X_test_scaled, y_train, y_test)
    
    # Print results
    print("\n[4] Model Performance Results:")
    print("-" * 80)
    for model_name, result in results.items():
        print(f"\n{model_name}:")
        print(f"  R² Score:              {result['r2']:.6f}")
        print(f"  Mean Absolute Error:   ₹{result['mae']:,.2f}")
        print(f"  Root Mean Squared Error: ₹{result['rmse']:,.2f}")
    
    # Generate visualizations
    print("\n[5] Generating visualizations...")
    plot_salary_distribution(df)
    plot_model_comparison(results)
    plot_predictions_vs_actual(results, y_test)
    plot_feature_importance(models, feature_names)
    plot_salary_by_education(df)
    plot_salary_by_role_and_industry(df)
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE - All visualizations saved")
    print("="*80)

if __name__ == "__main__":
    main()
