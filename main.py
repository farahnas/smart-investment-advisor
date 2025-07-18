import streamlit as st
import matplotlib.pyplot as plt

from utils.risk import assess_risk, agent_advice
from utils.data import fetch_asset_data, ASSETS
from utils.optimizer import optimize_portfolio

# ------------------------
# 1. Page Setup
# ------------------------
st.set_page_config(page_title="Smart Investment Advisor", layout="centered")

st.title("💼 Smart Investment Advisor")
st.markdown("""
Get personalized portfolio recommendations powered by AI:
- ✅ Fuzzy Logic for Risk Assessment  
- 🧬 Genetic Algorithm for Asset Allocation  
- 🤖 Natural-Language Investment Advice  
""")

# ------------------------
# 2. Input Form
# ------------------------
with st.form("user_profile"):
    age = st.number_input("Your Age", 18, 100, 30)
    income = st.number_input("Monthly Income ($)", 500, 20000, 4000)
    tolerance = st.radio("Risk Tolerance", ["Low", "Medium", "High"])
    submitted = st.form_submit_button("💡 Get Investment Plan")

# ------------------------
# 3. Results
# ------------------------
if submitted:
    with st.spinner("🔍 Analyzing your profile..."):
        # Risk Profile
        risk_level = assess_risk(age, income, tolerance)
        st.success(f"📌 **Assessed Risk Level:** `{risk_level}`")

        # Market Data
        returns, penalties = fetch_asset_data()

        # Portfolio Optimization
        allocation = optimize_portfolio(returns, penalties, list(ASSETS.keys()))

        # Portfolio Display
        st.subheader("📊 Portfolio Allocation")
        st.json(allocation)

        import matplotlib.pyplot as plt

    def plot_enhanced_pie_chart(portfolio: dict):
        labels = []
        sizes = []
        explode = []
        colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff9999']  # Pastel tones

        for asset, percent_str in portfolio.items():
            percent = int(percent_str.strip('%'))
            if percent > 0:
               labels.append(asset)
               sizes.append(percent)
               explode.append(0.05)  # Slight explosion for all slices
            else:
              continue  # Skip 0% allocations

        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors[:len(sizes)],
        autopct='%1.1f%%',
        startangle=140,
        shadow=True,
        textprops=dict(color="black", fontsize=12)
        )

        ax.axis('equal')  # Keep circle aspect ratio
        plt.setp(autotexts, size=13, weight="bold")
        plt.title("Portfolio Allocation", fontsize=16, weight="bold")

        return fig


    # Agent Advice
    # Pie Chart
    st.subheader("📈 Portfolio Breakdown")
    st.pyplot(plot_enhanced_pie_chart(allocation))

    st.info(agent_advice(risk_level))

    st.markdown("---")
    st.caption("🔁 Powered by AI, Fuzzy Logic, and Genetic Algorithms")
