# A/B Testing  

## Project Description:

This project aims to conduct an A/B test to evaluate the impact of two variants (Group A and Group B) on user behavior in an e-commerce platform. The goal is to determine which of the two groups yields better results in terms of conversion rates and purchase volume.

## Project Objective

Analyze the impact of variants A and B on:

•	Conversion rate: the proportion of users who completed a purchase

•	Total purchase value per session

•	Quantity of products purchased

•	Influence of contextual factors such as coupon usage, payment methods, session duration, device, region, customer age, and gender

The purpose is to identify the most effective version to maximize business performance and enhance user experience.
## Repository Structure
GitHub Repository: Includes a .gitignore file to control which files and folders should be uploaded.
• Folder Structure:

    o data/: To store data files. 
        	data_raw.csv
        	clean_data.csv
        	notnulls_data.csv
        
    o jupyter/: To store Jupyter Notebook files. 
        	ab_testing.ipynb
        	clean.ipynb
        	eda_preliminar.ipynb
        	nulls.ipynb
    o py./ 
        	src_ab_testing.py
        	src_eda.py
        
             

    • Creating the Virtual Environment:
        1.	Navigate to the project folder.
        2.	Create a virtual environment: 
        3.	py -m venv venv
        4.	Activate the environment: 
        5.	venv/bin/activate
        6   Install required libraries: 
        7.	pip install pandas numpy jupyter, matplotlib, seaborn, scipy
        8.	Create a requirements file: 
        9.	pip freeze > requirements.txt

## Data Used

The dataset contains detailed information about user sessions on the platform, including the following relevant columns:

•	User Id: unique identifier for each user

•	Group: A or B

•	Visit Date: date of the session

•	Conversion: indicates whether a purchase occurred

•	Product Category, Product Id, Product Name

•	Quantity, Price, Discount, Total Value

•	Payment Method, Shipping Method

•	Region, Customer Age, Customer Gender

•	Device, Session Duration, Coupon Used

•	Browser, Referral Source

## Conclusion

The A/B analysis revealed significant differences between the two groups.
Group B demonstrated a higher conversion rate and a greater average purchase volume per session.
It is recommended to implement the conditions of Group B, as they deliver better performance both in terms of conversions and total economic value generated.

