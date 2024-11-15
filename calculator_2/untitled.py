import streamlit as st

# Define investment plans
investment_plans = [
    {"name": "Investment Plan 1", "min_tenure": 0.5, "rate_range": (2.0, 2.2), "description": "Min. 6 months"},
    {"name": "Investment Plan 2", "min_tenure": 1, "rate_range": (2.2, 2.5), "description": "Min. 1 year"},
    {"name": "Investment Plan 3", "min_tenure": 2, "rate_range": (2.5, 2.7), "description": "Min. 2 years"},
    {"name": "Investment Plan 4", "min_tenure": 3, "rate_range": (2.7, 3.0), "description": "Min. 3 years"},
    {"name": "Investment Plan 5", "min_tenure": 3.1, "rate_range": (3.0, 3.3), "description": "More than 3 years"},
]

# Streamlit app layout
st.title("Investment Plan Recommender")
st.write("Answer a few questions to find an investment plan that aligns with your needs.")

# Question 1: Investment amount
investment_amount = st.number_input("1. How much money do you intend to invest? (in Rs.)", min_value=0.0, step=10000.0, format="%f")

# Question 2: Investment tenure in years
investment_tenure_years = st.number_input("2. Over how many years do you wish to invest?", min_value=0.5, step=0.5, format="%f")

# Question 3: Expected monthly return
expected_monthly_return = st.slider("3. What monthly return do you expect to receive on your investment?", min_value=2.0, max_value=3.3, step=0.1)
expected_annual_return = expected_monthly_return * 12
st.write(f"Your expected annual return is approximately **{expected_annual_return}%**.")

# Function to match the user's answers to the closest plan
def recommend_investment_plan(amount, tenure, monthly_return):
    for plan in investment_plans:
        if tenure >= plan["min_tenure"] and plan["rate_range"][0] <= monthly_return <= plan["rate_range"][1]:
            return plan
    return None

# Recommend a plan based on the user's input
if st.button("Find My Investment Plan"):
    recommended_plan = recommend_investment_plan(investment_amount, investment_tenure_years, expected_monthly_return)
    
    if recommended_plan:
        st.success(f"We recommend: **{recommended_plan['name']}**")
        st.write(f"**Plan Tenure Requirement:** {recommended_plan['description']}")
        st.write(f"**Monthly Rate Range:** {recommended_plan['rate_range'][0]}% to {recommended_plan['rate_range'][1]}%")
        st.write("Your investment is fully secured, and an agreement will be signed directly with our SECP-registered company.")
    else:
        st.error("Sorry, we currently don't have a plan that matches all your criteria. Please adjust your requirements and try again.")

# Additional information
st.write("---")
st.info("The investment is fully secured, and an agreement will be signed directly between the investor and the company (registered by SECP).")