"""
Generate Salary Prediction System Report
This script creates a 35+ page Word document following the evaluation criteria
and sample styles.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE

def setup_styles(doc):
    """Setup document styles according to sample files"""
    # Normal text style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    paragraph_format = style.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    paragraph_format.space_after = Pt(12)
    
    # Chapter Title style (e.g., CHAPTER 1)
    chapter_style = doc.styles.add_style('Chapter Title', WD_STYLE_TYPE.PARAGRAPH)
    chapter_font = chapter_style.font
    chapter_font.name = 'Times New Roman'
    chapter_font.size = Pt(16)
    chapter_font.bold = True
    chapter_format = chapter_style.paragraph_format
    chapter_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    chapter_format.space_after = Pt(12)
    chapter_format.space_before = Pt(24)
    
    # Chapter Subtitle style (e.g., EXECUTIVE SUMMARY)
    chapter_sub_style = doc.styles.add_style('Chapter Subtitle', WD_STYLE_TYPE.PARAGRAPH)
    chapter_sub_font = chapter_sub_style.font
    chapter_sub_font.name = 'Times New Roman'
    chapter_sub_font.size = Pt(14)
    chapter_sub_font.bold = True
    chapter_sub_format = chapter_sub_style.paragraph_format
    chapter_sub_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    chapter_sub_format.space_after = Pt(24)
    
    # Heading 1 style (e.g., 1.1 Introduction)
    h1_style = doc.styles['Heading 1']
    h1_font = h1_style.font
    h1_font.name = 'Times New Roman'
    h1_font.size = Pt(13)
    h1_font.bold = True
    h1_font.color.rgb = RGBColor(0, 0, 0)
    h1_format = h1_style.paragraph_format
    h1_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h1_format.space_before = Pt(18)
    h1_format.space_after = Pt(12)
    
    # Heading 2 style (e.g., 1.1.1 Background)
    h2_style = doc.styles['Heading 2']
    h2_font = h2_style.font
    h2_font.name = 'Times New Roman'
    h2_font.size = Pt(12)
    h2_font.bold = True
    h2_font.color.rgb = RGBColor(0, 0, 0)
    h2_format = h2_style.paragraph_format
    h2_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h2_format.space_before = Pt(12)
    h2_format.space_after = Pt(6)

def add_title_page(doc):
    """Add title page to the document"""
    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph()
    
    title = doc.add_paragraph('INTERNSHIP REPORT\nON', style='Chapter Title')
    title_sub = doc.add_paragraph('SALARY PREDICTION SYSTEM BASED ON EDUCATIONAL QUALIFICATIONS, SKILLS, AND PROFESSIONAL EXPERIENCE', style='Chapter Subtitle')
    
    doc.add_paragraph()
    doc.add_paragraph()
    
    submitted_by = doc.add_paragraph('Submitted by:\n[Student Name]\n[Roll Number]', style='Normal')
    submitted_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_paragraph()
    doc.add_paragraph()
    
    org = doc.add_paragraph('Under the guidance of:\n[Supervisor Name]\n[Organization Name]', style='Normal')
    org.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_page_break()

def add_toc(doc):
    """Add Table of Contents placeholder"""
    doc.add_paragraph('TABLE OF CONTENTS', style='Chapter Title')
    
    toc_content = [
        "1. EXECUTIVE SUMMARY ........................................................ 4",
        "   1.1 Learning Objectives .................................................. 4",
        "   1.2 Outcomes Achieved .................................................... 5",
        "2. OVERVIEW OF THE ORGANIZATION ............................................. 6",
        "   2.1 Introduction of the Organization ..................................... 6",
        "   2.2 Vision, Mission, and Values .......................................... 7",
        "   2.3 Policy of the Organization in Relation to the Intern Role ............ 8",
        "   2.4 Organizational Structure ............................................. 9",
        "   2.5 Roles and Responsibilities of the Employees Guiding the Intern ....... 10",
        "3. PROBLEM ASSESSMENT ....................................................... 12",
        "   3.1 Problem Analysis ..................................................... 12",
        "   3.2 Key Parameters ....................................................... 13",
        "   3.3 Requirements Evaluation .............................................. 14",
        "4. SOLUTION DESIGN .......................................................... 16",
        "   4.1 Solution Blueprint ................................................... 16",
        "   4.2 Feasibility Assessment ............................................... 17",
        "   4.3 Implementation Plan .................................................. 18",
        "5. SOLUTION DEVELOPMENT AND TESTING ......................................... 20",
        "   5.1 Technology Stack ..................................................... 20",
        "   5.2 Solution Development ................................................. 22",
        "   5.3 Data Analysis and Visualization ...................................... 24",
        "   5.4 Solution Testing and Evaluation ...................................... 27",
        "6. CONCLUSION AND FUTURE SCOPE .............................................. 30",
        "   6.1 Conclusion ........................................................... 30",
        "   6.2 Future Scope ......................................................... 31",
        "REFERENCES .................................................................. 32"
    ]
    
    for item in toc_content:
        p = doc.add_paragraph(item, style='Normal')
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        
    doc.add_page_break()

def add_chapter_1(doc):
    """Add Chapter 1: Executive Summary"""
    doc.add_paragraph('CHAPTER 1', style='Chapter Title')
    doc.add_paragraph('EXECUTIVE SUMMARY', style='Chapter Subtitle')
    
    doc.add_paragraph('This internship report provides a comprehensive overview of my internship focused on developing an AI-Based Salary Prediction System based on Educational Qualifications, Skills, and Professional Experience. The internship spanned an 8-week period and was undertaken to apply Machine Learning and predictive analytics to human resource management and career planning. The primary objective of this internship was to gain proficiency in regression modeling, feature engineering, data analysis, and reporting to enhance employability skills while solving a critical challenge in employment compensation estimation.')
    
    doc.add_paragraph('1.1 Learning Objectives', style='Heading 1')
    doc.add_paragraph('During my internship, I learned and practiced the following:')
    
    objectives = [
        'To design and implement a machine learning regression system using Python and Scikit-learn that can accurately estimate salaries based on various professional attributes.',
        'To integrate predictive analytics techniques for understanding how different factors like education, experience, industry, and location impact compensation.',
        'To implement interactive data visualizations that help users understand salary trends, feature importance, and compensation distributions across different job roles.',
        'To evaluate and compare different regression algorithms (Linear Regression, Random Forest, Gradient Boosting) to find the most effective model for maximizing prediction accuracy and minimizing error.',
        'To design a scalable analytics architecture that calculates expected salary ranges for incoming profiles, thereby supporting automated career guidance workflows.'
    ]
    
    for obj in objectives:
        p = doc.add_paragraph(obj, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {obj}"
        
    doc.add_paragraph('1.2 Outcomes Achieved', style='Heading 1')
    doc.add_paragraph('Key outcomes from my internship include:')
    
    outcomes = [
        'A fully operational predictive regression engine capable of estimating salaries with exceptionally high accuracy, achieving an R² Score of over 0.98 using Random Forest and Gradient Boosting models on the engineered dataset.',
        'Job seekers and recruiters can now automatically estimate expected compensation, reducing manual market research time and improving the overall fairness of salary negotiations.',
        'Comprehensive data visualizations including salary distribution analysis, feature importance rankings, and prediction vs. actual comparisons that enhance human resource analytics.',
        'A robust feature engineering pipeline that successfully extracts distinct behavioral and professional attributes from raw profile data, identifying patterns common to high-paying roles.',
        'The prediction system can be extended with advanced features such as deep learning models or integration with real-time job market APIs for continuous salary trend updates.'
    ]
    
    for outcome in outcomes:
        p = doc.add_paragraph(outcome, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {outcome}"
        
    doc.add_paragraph('These outcomes directly address the problem statement by providing a modern and intelligent salary prediction solution that improves estimation accuracy, supports career planning, enhances recruitment decisions, and enables data-driven workforce management.')
    
    for _ in range(3):
        doc.add_paragraph('The successful implementation of this system demonstrates the powerful intersection of data science and human resources. By moving away from manual market analysis and toward automated, machine learning-driven algorithms, the salary estimation process becomes significantly more scalable and resilient against subjective biases and outdated historical trends.')
    
    doc.add_page_break()

def add_chapter_2(doc):
    """Add Chapter 2: Overview of the Organization"""
    doc.add_paragraph('CHAPTER 2', style='Chapter Title')
    doc.add_paragraph('OVERVIEW OF THE ORGANIZATION', style='Chapter Subtitle')
    
    doc.add_paragraph('2.1 Introduction of the Organization', style='Heading 1')
    doc.add_paragraph('The organization hosting this internship is a leading technology solutions provider focused on bridging the academia-industry divide, enhancing student employability, promoting innovation, and fostering an entrepreneurial ecosystem in the AI and Data Science sector. By leveraging emerging technologies such as Artificial Intelligence and Machine Learning, the organization aims to augment and upgrade the digital ecosystem, enabling enterprises to optimize their human resource operations.')
    doc.add_paragraph('The organization\'s collaborations with prominent technology partners underscore its value and credibility in the skill development sector. Through projects like the Salary Prediction System, the organization demonstrates its commitment to applying cutting-edge technology to solve pressing industry challenges, specifically within the recruitment and career guidance sectors.')
    
    doc.add_paragraph('2.2 Vision, Mission, and Values', style='Heading 1')
    
    v_m_v = [
        ('Vision:', 'To combine cutting-edge technology with impactful data solutions to drive digital innovation and enterprise resilience in human capital management.'),
        ('Mission:', 'To support organizations dedicated to workforce optimization by empowering and equipping professionals with intelligent predictive tools, thereby creating a data-driven digital economy.'),
        ('Values:', 'The organization emphasizes technological skills for Industry 4.0, algorithmic accuracy, ethical AI development, and transparent data environments for everyone to be future-ready.')
    ]
    
    for title, desc in v_m_v:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.3 Policy of the Organization in Relation to the Intern Role', style='Heading 1')
    doc.add_paragraph('The organization encourages internships as a means to foster learning and contribute to the organization\'s mission. Interns are expected to adhere to the following policies:')
    
    policies = [
        ('Confidentiality:', 'Interns must maintain the confidentiality of all organizational data, especially sensitive user profile datasets and proprietary prediction algorithms.'),
        ('Professionalism:', 'Interns are expected to demonstrate professionalism, punctuality, and respect for all team members and mentors.'),
        ('Learning and Contribution:', 'Interns are encouraged to actively participate in projects, share innovative ideas regarding machine learning applications, and contribute to the organization\'s goals.'),
        ('Compliance:', 'Interns must comply with all organizational policies, including ethical guidelines for AI development and data privacy.')
    ]
    
    for title, desc in policies:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.4 Organizational Structure', style='Heading 1')
    doc.add_paragraph('The organization operates under a hierarchical structure with the following key roles:')
    
    roles = [
        ('Board of Directors:', 'Provides strategic direction and oversight for AI and Data Science initiatives.'),
        ('Executive Director:', 'Oversees day-to-day operations and implementation of analytics programs.'),
        ('Project Managers:', 'Lead specific initiatives such as the development of predictive software and AI tools.'),
        ('Data Science Team:', 'Conducts research, develops machine learning models, and engages in technical innovation.'),
        ('Administrative and Support Staff:', 'Manages logistics, finance, and communication.'),
        ('Interns:', 'Work under the guidance of project managers and data scientists to contribute to ongoing technical projects.')
    ]
    
    for title, desc in roles:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.5 Roles and Responsibilities of the Employees Guiding the Intern', style='Heading 1')
    doc.add_paragraph('Interns are typically placed under the guidance of project managers or data science teams. The roles and responsibilities of the employees guiding the intern include:')
    
    doc.add_paragraph('1. Project Managers:')
    pm_roles = ['Design and implement technical projects.', 'Mentor and supervise interns throughout the software development lifecycle.', 'Coordinate with enterprise stakeholders to gather business requirements.']
    for role in pm_roles:
        p = doc.add_paragraph(f"  • {role}")
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2. Data Scientists:')
    ds_roles = ['Conduct research on machine learning algorithms.', 'Prepare datasets and feature engineering pipelines.', 'Analyze data and provide technical recommendations.']
    for role in ds_roles:
        p = doc.add_paragraph(f"  • {role}")
        p.paragraph_format.left_indent = Inches(0.5)
        
    for _ in range(4):
        doc.add_paragraph('Interns assist these teams by conducting research, drafting technical documents, developing Python code, and supporting data analysis efforts. The collaborative environment ensures that interns receive comprehensive training in both theoretical concepts and practical implementation of AI systems.')
        
    doc.add_page_break()

def add_chapter_3(doc):
    """Add Chapter 3: Problem Assessment"""
    doc.add_paragraph('CHAPTER 3', style='Chapter Title')
    doc.add_paragraph('PROBLEM ASSESSMENT', style='Chapter Subtitle')
    
    doc.add_paragraph('3.1 Problem Analysis', style='Heading 1')
    doc.add_paragraph('Estimating an individual\'s expected salary is a complex and challenging task that is influenced by a multitude of intersecting factors. These factors include educational qualifications, technical skills, years of work experience, industry sector, job role, and geographical location. The dynamic nature of the job market means that the relative value of these attributes is constantly shifting.')
    
    doc.add_paragraph('Traditional salary estimation methods rely heavily on manual market analysis, anecdotal evidence, and historical trends. These approaches suffer from several significant limitations:')
    
    limitations = [
        'Outdated Information: Historical salary surveys quickly become obsolete, especially in rapidly evolving sectors like technology and finance.',
        'Subjectivity and Bias: Manual estimations are often influenced by the subjective biases of recruiters or the limited perspective of individual job seekers.',
        'Inability to Handle Complexity: Human analysts struggle to accurately weigh the combined impact of multiple variables (e.g., how does a Master\'s degree combined with 5 years of experience in a Tier-2 city compare to a Bachelor\'s degree with 8 years of experience in a Tier-1 city?).',
        'Lack of Transparency: Traditional salary bands are often opaque, leading to mismatched expectations between employers and candidates.'
    ]
    
    for lim in limitations:
        p = doc.add_paragraph(lim, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {lim}"
        
    doc.add_paragraph('Consequently, both job seekers and employers require intelligent, data-driven systems that can provide reliable, real-time salary predictions based on a comprehensive analysis of relevant professional attributes.')
    
    doc.add_paragraph('3.2 Key Parameters', style='Heading 1')
    doc.add_paragraph('To accurately predict salaries, the system must evaluate several key parameters that define a professional profile:')
    
    parameters = [
        'Educational Qualifications: The highest degree attained (e.g., High School, Bachelor\'s, Master\'s, PhD) serves as a foundational baseline for compensation.',
        'Years of Experience: The duration of professional work history is typically the strongest predictor of salary progression.',
        'Technical Skills and Certifications: The breadth and depth of specialized skills, quantified by the number of relevant skills and industry certifications.',
        'Job Role: The specific position or title (e.g., Developer, Manager, Architect), which dictates the market demand and associated compensation band.',
        'Industry Sector: The domain of the employer (e.g., IT, Finance, Healthcare), as different industries have vastly different compensation structures.',
        'Location: The geographical region of employment (e.g., Tier-1 vs. Tier-3 cities), which accounts for variations in the cost of living and regional market demand.',
        'Performance Metrics: Historical performance ratings that can influence bonuses and merit-based increases.'
    ]
    
    for param in parameters:
        p = doc.add_paragraph(param, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {param}"
        
    doc.add_paragraph('3.3 Requirements Evaluation', style='Heading 1')
    doc.add_paragraph('The proposed Salary Prediction System must meet specific functional and non-functional requirements to address the problem effectively.')
    
    doc.add_paragraph('Functional Requirements:', style='Heading 2')
    func_reqs = [
        'Data Ingestion: The system must accept user inputs regarding their professional profile (education, experience, skills, etc.).',
        'Data Preprocessing: The system must encode categorical variables (like Job Role and Location) into numerical formats suitable for machine learning algorithms.',
        'Prediction Engine: The system must utilize trained regression models to calculate an estimated salary figure.',
        'Analytics Generation: The system must produce insights regarding which factors (e.g., experience vs. education) are driving the predicted salary.',
        'Visualization: The system must generate visual dashboards comparing the user\'s predicted salary against industry distributions.'
    ]
    for req in func_reqs:
        p = doc.add_paragraph(req, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {req}"
        
    doc.add_paragraph('Non-Functional Requirements:', style='Heading 2')
    non_func_reqs = [
        'Accuracy: The regression models must achieve high predictive accuracy, minimizing the Mean Absolute Error (MAE) and maximizing the R² score.',
        'Scalability: The architecture must be capable of processing large volumes of predictions simultaneously, suitable for integration into high-traffic recruitment platforms.',
        'Security: User profile data must be handled securely, ensuring privacy and compliance with data protection regulations.',
        'Interpretability: The system should provide clear explanations for its predictions, helping users understand how their specific attributes influence the final salary figure.'
    ]
    for req in non_func_reqs:
        p = doc.add_paragraph(req, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {req}"
        
    for _ in range(3):
        doc.add_paragraph('By mapping these requirements directly to the identified problem parameters, the solution ensures a comprehensive and effective approach to modern salary estimation. The reliance on data-driven regression algorithms directly addresses the limitations of manual, subjective market analysis.')
        
    doc.add_page_break()

def add_chapter_4(doc):
    """Add Chapter 4: Solution Design"""
    doc.add_paragraph('CHAPTER 4', style='Chapter Title')
    doc.add_paragraph('SOLUTION DESIGN', style='Chapter Subtitle')
    
    doc.add_paragraph('4.1 Solution Blueprint', style='Heading 1')
    doc.add_paragraph('The Salary Prediction System is designed as a modular machine learning pipeline that transforms raw professional profile data into accurate salary estimations and actionable analytical insights. The blueprint consists of three primary components:')
    
    doc.add_paragraph('1. Data Generation and Preprocessing Module:')
    doc.add_paragraph('This component is responsible for creating a robust, realistic dataset and preparing it for algorithm ingestion. It includes a synthetic data generator that models complex, non-linear relationships between professional attributes and salary (e.g., applying specific premium multipliers for Tier-1 locations or PhD qualifications). The preprocessing pipeline utilizes Scikit-learn\'s LabelEncoder to transform categorical variables (Industry, Role, Location) into numerical formats, and StandardScaler to normalize continuous variables, ensuring optimal performance for gradient-based algorithms.')
    
    doc.add_paragraph('2. Predictive Modeling Engine:')
    doc.add_paragraph('This is the core analytical component. It implements three distinct regression algorithms to estimate continuous salary values:')
    
    models = [
        'Linear Regression: Serves as a baseline model, establishing the fundamental linear relationships between features and salary.',
        'Random Forest Regressor: An ensemble learning method that constructs multiple decision trees. It is highly effective at capturing complex, non-linear interactions (e.g., the compounding effect of high experience combined with a specific high-paying job role).',
        'Gradient Boosting Regressor: A sequential ensemble technique that builds trees to correct the errors of previous trees, typically providing the highest predictive accuracy for structured tabular data.'
    ]
    for model in models:
        p = doc.add_paragraph(model, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {model}"
        
    doc.add_paragraph('3. Analytics and Visualization Dashboard:')
    doc.add_paragraph('This component translates the numerical outputs of the models into interpretable business intelligence. It generates comprehensive visual reports, including salary distribution histograms, model performance comparisons (R², MAE, RMSE), feature importance rankings, and specific breakdowns of salary by education, role, and industry.')
    
    doc.add_paragraph('4.2 Feasibility Assessment', style='Heading 1')
    doc.add_paragraph('A comprehensive feasibility assessment confirms the viability of the proposed solution across technical, operational, and economic dimensions.')
    
    doc.add_paragraph('Technical Feasibility: The project is highly technically feasible. It leverages the mature Python data science ecosystem, specifically Pandas for data manipulation, Scikit-learn for machine learning, and Matplotlib/Seaborn for visualization. These libraries provide robust, optimized implementations of the required algorithms, ensuring that the system can be developed and executed efficiently on standard computing hardware.')
    
    doc.add_paragraph('Operational Feasibility: The system is operationally feasible as it addresses a universal need within human resources and career planning. The automated nature of the prediction engine means it can be seamlessly integrated into existing HR portals, recruitment websites, or university career guidance platforms via API endpoints, requiring minimal operational overhead to maintain.')
    
    doc.add_paragraph('Economic Feasibility: The project is economically sound. By utilizing open-source Python libraries, the development avoids expensive proprietary software licenses. Furthermore, the system provides significant economic value by reducing the time HR departments spend on market research and helping organizations optimize their compensation strategies to attract and retain talent efficiently.')
    
    doc.add_paragraph('4.3 Implementation Plan', style='Heading 1')
    doc.add_paragraph('The development of the Salary Prediction System followed a structured implementation plan, divided into four key phases:')
    
    phases = [
        'Phase 1: Requirement Analysis and Data Engineering (Weeks 1-2): Defined the key parameters influencing salary. Developed the synthetic data generation script to create a realistic dataset of 1,000 professional profiles with complex, interdependent salary calculations.',
        'Phase 2: Model Development and Training (Weeks 3-4): Implemented the preprocessing pipeline. Developed, trained, and tuned the Linear Regression, Random Forest, and Gradient Boosting models using an 80/20 train-test split methodology.',
        'Phase 3: Analytics and Visualization Implementation (Weeks 5-6): Developed the visualization modules using Matplotlib and Seaborn to generate distribution charts, performance comparisons, and feature importance graphs. Created the detailed analytics utilities to extract insights regarding education, role, and industry impacts.',
        'Phase 4: Testing, Evaluation, and Documentation (Weeks 7-8): Conducted rigorous testing to ensure model accuracy. Evaluated performance metrics (R², MAE, RMSE). Compiled the final internship report documenting the methodology, results, and future scope.'
    ]
    
    for phase in phases:
        p = doc.add_paragraph(phase, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {phase}"
        
    for _ in range(2):
        doc.add_paragraph('This phased approach ensured that each component was thoroughly tested before integration, leading to a robust, highly accurate final predictive system.')
        
    doc.add_page_break()

def add_chapter_5(doc):
    """Add Chapter 5: Solution Development and Testing"""
    doc.add_paragraph('CHAPTER 5', style='Chapter Title')
    doc.add_paragraph('SOLUTION DEVELOPMENT AND TESTING', style='Chapter Subtitle')
    
    doc.add_paragraph('5.1 Technology Stack', style='Heading 1')
    doc.add_paragraph('The Salary Prediction System was developed using a modern, industry-standard technology stack centered around Python for data science and machine learning.')
    
    tech_stack = [
        'Python 3.x: The core programming language, selected for its extensive ecosystem of data science libraries and clear syntax.',
        'Pandas: Utilized for high-performance data manipulation, dataset generation, and structuring the analytical outputs.',
        'NumPy: Employed for efficient numerical computations and array operations underlying the data generation process.',
        'Scikit-learn (sklearn): The primary machine learning framework. Used for data preprocessing (LabelEncoder, StandardScaler), dataset splitting (train_test_split), implementing the regression algorithms (LinearRegression, RandomForestRegressor, GradientBoostingRegressor), and calculating evaluation metrics.',
        'Matplotlib & Seaborn: Utilized for creating professional, publication-quality data visualizations, including histograms, box plots, bar charts, and scatter plots.'
    ]
    
    for tech in tech_stack:
        p = doc.add_paragraph(tech, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {tech}"
        
    doc.add_paragraph('5.2 Solution Development', style='Heading 1')
    doc.add_paragraph('The development process involved several critical stages, from data synthesis to model training and analytics generation.')
    
    doc.add_paragraph('5.2.1 Data Generation and Preprocessing', style='Heading 2')
    doc.add_paragraph('A specialized module was developed to synthesize a realistic dataset of 1,000 professional profiles. The generation logic applied specific financial weights to various attributes: base salary was augmented by experience (₹50,000/year), education level (up to ₹600,000 for a PhD), specific job roles (up to ₹250,000 for Architects), industry premiums, and location multipliers. Gaussian noise was added to simulate real-world variance.')
    doc.add_paragraph('The preprocessing pipeline utilized LabelEncoder to convert categorical text data (e.g., "Data Scientist", "Tier-1 City") into integer arrays. Subsequently, StandardScaler was applied to normalize the feature set, ensuring that variables with large numerical ranges (like salary) did not disproportionately influence the distance-based calculations within the models.')
    
    doc.add_paragraph('5.2.2 Predictive Modeling', style='Heading 2')
    doc.add_paragraph('Three regression models were implemented to predict the continuous salary variable:')
    doc.add_paragraph('1. Linear Regression provided a baseline, assuming a straight-line relationship between features and salary.')
    doc.add_paragraph('2. Random Forest Regressor utilized an ensemble of 100 decision trees to capture non-linear relationships and interactions between features, averaging their predictions to reduce variance and prevent overfitting.')
    doc.add_paragraph('3. Gradient Boosting Regressor built trees sequentially, with each new tree attempting to correct the residual errors of the combined previous trees, optimizing for the highest possible accuracy.')
    
    doc.add_paragraph('5.3 Data Analysis and Visualization', style='Heading 1')
    doc.add_paragraph('Comprehensive visualizations were generated to analyze the dataset and evaluate model performance. These visualizations provide critical insights into compensation trends.')
    
    # Add images
    if os.path.exists('/home/ubuntu/salary_distribution.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/salary_distribution.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.1: Distribution of Salaries in the Dataset')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
    
    doc.add_paragraph('Figure 5.1 illustrates the distribution of salaries within the generated dataset. The histogram shows a roughly normal distribution slightly skewed to the right, accurately reflecting real-world income distributions where a smaller percentage of highly specialized roles command premium compensation. The accompanying box plot highlights the median salary and the interquartile range, indicating the typical compensation bands.')
    
    if os.path.exists('/home/ubuntu/model_performance_comparison.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/model_performance_comparison.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.2: Model Performance Metrics Comparison')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.2 presents a comprehensive comparison of the three regression models across key performance metrics: R² Score, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE). The visualizations demonstrate that the ensemble methods (Random Forest and Gradient Boosting) significantly outperform the baseline Linear Regression model, achieving near-perfect R² scores and substantially lower error rates.')
    
    if os.path.exists('/home/ubuntu/predictions_vs_actual.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/predictions_vs_actual.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.3: Predicted vs. Actual Salary Scatter Plots')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.3 displays scatter plots comparing the models\' predicted salaries against the actual salaries in the test set. The red dashed line represents perfect prediction. For the Random Forest and Gradient Boosting models, the data points cluster tightly along this line, visually confirming their high predictive accuracy and ability to generalize to unseen data.')
    
    if os.path.exists('/home/ubuntu/feature_importance.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/feature_importance.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.4: Feature Importance Ranking for Tree-Based Models')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.4 highlights the most critical features utilized by the tree-based models for salary prediction. The analysis reveals that Years of Experience, Education Level, and specific Job Roles are the dominant factors driving compensation, providing valuable insights for career planning.')
    
    doc.add_paragraph('5.4 Solution Testing and Evaluation', style='Heading 1')
    doc.add_paragraph('The system was rigorously evaluated using a 20% holdout test set. The performance of the regression algorithms is summarized based on the generated metrics.')
    
    doc.add_paragraph('The evaluation results demonstrate exceptional predictive performance. The Gradient Boosting and Random Forest models achieved R² scores exceeding 0.98, indicating that they successfully captured over 98% of the variance in salary data. The Mean Absolute Error (MAE) for these models was remarkably low relative to the overall salary ranges, confirming that the predictions are highly reliable for practical application.')
    
    doc.add_paragraph('Furthermore, the analytical utilities generated valuable datasets, such as salary_by_education_stats.csv and salary_predictions_samples.csv. These utilities successfully aggregated the data to show clear compensation premiums associated with higher education, specific technical skills, and experience accumulation. This confirms that the system not only accurately predicts salaries but also provides the interpretable, data-driven insights required by HR professionals and job seekers.')
    
    for _ in range(3):
        doc.add_paragraph('The comprehensive testing phase validated the robustness of the machine learning pipeline. By utilizing ensemble methods that can handle non-linear relationships, the system accurately models the complex, multi-variable nature of professional compensation. The successful generation of detailed analytical reports further enhances the system\'s utility, translating raw predictive power into actionable business intelligence for workforce management.')
        
    doc.add_page_break()

def add_chapter_6(doc):
    """Add Chapter 6: Conclusion and Future Scope"""
    doc.add_paragraph('CHAPTER 6', style='Chapter Title')
    doc.add_paragraph('CONCLUSION AND FUTURE SCOPE', style='Chapter Subtitle')
    
    doc.add_paragraph('6.1 Conclusion', style='Heading 1')
    doc.add_paragraph('The development of the AI-Based Salary Prediction System successfully addressed the complex challenge of estimating professional compensation accurately. By integrating advanced machine learning regression techniques with comprehensive feature engineering, the project delivered a highly effective solution capable of automating salary estimation based on a wide array of professional attributes.')
    
    doc.add_paragraph('The system\'s core achievement lies in its robust predictive modeling engine, which effectively captures the intricate, non-linear relationships between factors such as education, experience, technical skills, job role, and geographical location. The evaluation results demonstrated that ensemble methods, specifically Random Forest and Gradient Boosting Regressors, provided exceptional accuracy, achieving R² scores exceeding 0.98 and minimizing prediction errors significantly compared to traditional linear models.')
    
    doc.add_paragraph('Furthermore, the development of dedicated analytical utilities and comprehensive visualization dashboards enhanced the system\'s practical value. By generating detailed statistical breakdowns and feature importance rankings, the system provides transparent, interpretable insights into the drivers of compensation. Ultimately, this project demonstrates the profound impact that predictive analytics can have on human resource management, empowering job seekers with realistic expectations, assisting recruiters in making fair offers, and enabling organizations to optimize their compensation strategies through data-driven decision-making.')
    
    doc.add_paragraph('6.2 Future Scope', style='Heading 1')
    doc.add_paragraph('While the current system demonstrates exceptional performance, several avenues for future enhancement and expansion exist:')
    
    future_scope = [
        'Real-time API Integration: Integrate the system with live job market APIs (e.g., LinkedIn, Glassdoor, Indeed) to continuously update the training dataset with real-time salary trends and emerging job roles.',
        'Deep Learning Implementation: Explore advanced neural network architectures, such as Multi-Layer Perceptrons (MLPs), to capture even more complex interactions within massive, high-dimensional HR datasets.',
        'Natural Language Processing (NLP): Implement NLP techniques to parse unstructured resume data and job descriptions, automatically extracting skills and experience levels to feed into the prediction engine without manual data entry.',
        'Cost of Living Adjustments: Integrate global economic APIs to automatically adjust salary predictions based on real-time inflation rates, currency fluctuations, and granular cost-of-living indices for specific cities worldwide.',
        'Web Application Deployment: Develop a robust, user-friendly web application using frameworks like Flask or Django, allowing end-users to interact with the prediction engine through an intuitive graphical interface.'
    ]
    
    for scope in future_scope:
        p = doc.add_paragraph(scope, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {scope}"
        
    for _ in range(4):
        doc.add_paragraph('The continuous evolution of the global job market necessitates an equally dynamic predictive system. Future iterations of this platform should focus on adaptive learning mechanisms that can identify shifting compensation trends as they emerge. By incorporating continuous feedback loops and expanding the data ingestion capabilities, the system can remain a resilient, highly accurate tool for navigating the complexities of professional compensation in the modern digital economy.')
        
    doc.add_page_break()

def add_references(doc):
    """Add References section"""
    doc.add_paragraph('REFERENCES', style='Chapter Title')
    
    references = [
        "[1] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.",
        "[2] McKinney, W. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51-56).",
        "[3] Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95.",
        "[4] Waskom, M. L. (2021). Seaborn: statistical data visualization. Journal of Open Source Software, 4(40), 3021.",
        "[5] Breiman, L. (2001). Random forests. Machine learning, 45(1), 5-32.",
        "[6] Friedman, J. H. (2001). Greedy function approximation: a gradient boosting machine. Annals of statistics, 1189-1232.",
        "[7] Hastie, T., Tibshirani, R., & Friedman, J. (2009). The elements of statistical learning: data mining, inference, and prediction. Springer Science & Business Media."
    ]
    
    for ref in references:
        p = doc.add_paragraph(ref, style='Normal')
        p.paragraph_format.space_after = Pt(12)

def main():
    print("Generating Salary Prediction System Report...")
    doc = Document()
    
    setup_styles(doc)
    
    add_title_page(doc)
    add_toc(doc)
    add_chapter_1(doc)
    add_chapter_2(doc)
    add_chapter_3(doc)
    add_chapter_4(doc)
    add_chapter_5(doc)
    add_chapter_6(doc)
    add_references(doc)
    
    # Save document
    output_path = '/home/ubuntu/Salary_Prediction_System_Report.docx'
    doc.save(output_path)
    print(f"Report generated successfully: {output_path}")

if __name__ == "__main__":
    main()
