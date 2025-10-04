
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="💸 Personal Expense Tracker", layout="centered")

st.title("💸 Personal Expense Tracker")
st.write("Track your **Daily, Weekly, and Monthly** expenses with breakdowns & charts.")

# ---------------- Personal Info ----------------
st.header("👤 Personal Information")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=1, max_value=100, step=1)
with col2:
    gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
    profession = st.selectbox("Profession", ["Student", "Employee", "Freelancer", "Other"])

# Display profile card if name is entered
if name:
    st.success(f"Hello **{name}** 👋 | {age} yrs | {gender} | {profession}")

st.markdown("---")

# ---------------- Daily ----------------
st.header("📅 Daily Expenses")
with st.expander("Enter Daily Expenses"):
    d_food = st.number_input("Food (₹/day)", min_value=0.0, step=10.0)
    d_travel = st.number_input("Travel (₹/day)", min_value=0.0, step=10.0)
    d_shopping = st.number_input("Shopping (₹/day)", min_value=0.0, step=10.0)
    d_grocery = st.number_input("Grocery (₹/day)", min_value=0.0, step=10.0)
    d_other_name = st.text_input("Other (name)")
    d_other_amt = st.number_input("Other (₹/day)", min_value=0.0, step=10.0)

daily = {
    "Food": d_food,
    "Travel": d_travel,
    "Shopping": d_shopping,
    "Grocery": d_grocery,
}
if d_other_name and d_other_amt > 0:
    daily[f"Other: {d_other_name}"] = d_other_amt
daily_total = sum(daily.values())

# ---------------- Weekly ----------------
st.header("📆 Weekly Expenses")
with st.expander("Enter Weekly Expenses"):
    w_food = st.number_input("Food (₹/week)", min_value=0.0, step=50.0)
    w_travel = st.number_input("Travel (₹/week)", min_value=0.0, step=50.0)
    w_shopping = st.number_input("Shopping (₹/week)", min_value=0.0, step=50.0)
    w_grocery = st.number_input("Grocery (₹/week)", min_value=0.0, step=50.0)
    w_other_name = st.text_input("Other (name, weekly)")
    w_other_amt = st.number_input("Other (₹/week)", min_value=0.0, step=50.0)

weekly = {
    "Food": w_food,
    "Travel": w_travel,
    "Shopping": w_shopping,
    "Grocery": w_grocery,
}
if w_other_name and w_other_amt > 0:
    weekly[f"Other: {w_other_name}"] = w_other_amt
weekly_total = sum(weekly.values())

# ---------------- Monthly ----------------
st.header("📅 Monthly Expenses")
with st.expander("Enter Monthly Expenses"):
    m_mobile = st.number_input("Mobile Recharge (₹/month)", min_value=0.0, step=100.0)
    m_wifi = st.number_input("WiFi Recharge (₹/month)", min_value=0.0, step=100.0)
    m_rent = st.number_input("Rent (₹/month)", min_value=0.0, step=500.0)
    m_grocery = st.number_input("Grocery (₹/month)", min_value=0.0, step=100.0)
    m_entertainment = st.number_input("Entertainment (movies, etc.) (₹/month)", min_value=0.0, step=100.0)
    m_gym = st.number_input("Gym Membership (₹/month)", min_value=0.0, step=100.0)
    m_shopping = st.number_input("Shopping (₹/month)", min_value=0.0, step=100.0)

    st.markdown("**OTT Subscriptions (monthly)**")
    ott_entries = st.text_area("Enter as name,amount (one per line)", placeholder="Netflix,500\nPrime,200")
    ott_dict = {}
    for line in ott_entries.splitlines():
        if "," in line:
            n, a = [p.strip() for p in line.split(",", 1)]
            try:
                ott_dict[f"OTT:{n}"] = float(a)
            except:
                pass

    st.markdown("**Food Delivery Orders**")
    m_food_orders = st.number_input("Food Delivery Orders (₹/month)", min_value=0.0, step=100.0)
    sub = st.radio("Do you have subscription?", ["No", "Yes"])
    fd_dict = {"Orders": m_food_orders}
    if sub == "Yes":
        fd_dict["Subscription"] = st.number_input("Subscription cost (₹/month)", min_value=0.0, step=50.0)

    m_other_name = st.text_input("Other Monthly Expense (name)")
    m_other_amt = st.number_input("Other Monthly (₹/month)", min_value=0.0, step=100.0)

monthly = {
    "Mobile Recharge": m_mobile,
    "WiFi Recharge": m_wifi,
    "Rent": m_rent,
    "Grocery": m_grocery,
    "Entertainment": m_entertainment,
    "Gym": m_gym,
    "Shopping": m_shopping,
    **ott_dict,
    **{f"Food Delivery {k}": v for k, v in fd_dict.items()},
}
if m_other_name and m_other_amt > 0:
    monthly[f"Other: {m_other_name}"] = m_other_amt
monthly_total = sum(monthly.values())

# ---------------- Results ----------------
st.subheader("📊 Summary of Expenses")
col1, col2, col3 = st.columns(3)
col1.metric("Daily Total", f"₹{daily_total:.2f}")
col2.metric("Weekly Total", f"₹{weekly_total:.2f}")
col3.metric("Monthly Total", f"₹{monthly_total:.2f}")

# Combine all into dataframe
records = []
for k, v in daily.items():
    records.append({"Category": k, "Frequency": "Daily", "Amount": v})
for k, v in weekly.items():
    records.append({"Category": k, "Frequency": "Weekly", "Amount": v})
for k, v in monthly.items():
    records.append({"Category": k, "Frequency": "Monthly", "Amount": v})

df = pd.DataFrame(records)

if not df.empty:
    st.write("### Detailed Breakdown")
    st.dataframe(df)

    # Pie chart (monthly only)
    st.write("### Monthly Expense Distribution (Pie Chart)")
    monthly_df = df[df["Frequency"] == "Monthly"]
    if not monthly_df.empty:
        fig, ax = plt.subplots()
        ax.pie(monthly_df["Amount"], labels=monthly_df["Category"], autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

    # Bar chart (all categories)
    st.write("### Expenses by Frequency (Bar Chart)")
    fig2, ax2 = plt.subplots()
    df.groupby("Frequency")["Amount"].sum().plot(kind="bar", ax=ax2, color=["#4CAF50", "#2196F3", "#FF9800"])
    ax2.set_ylabel("₹ Amount")
    st.pyplot(fig2)

    # Histogram
    st.write("### Expense Spread (Histogram)")
    fig3, ax3 = plt.subplots()
    ax3.hist(df["Amount"], bins=10, color="#9C27B0", edgecolor="white")
    ax3.set_xlabel("₹ Expense Amount")
    ax3.set_ylabel("Frequency")
    st.pyplot(fig3)

    # Download button
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download CSV", csv, "expenses.csv", "text/csv")
