import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
from datetime import datetime

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------
st.set_page_config(
    page_title="WorkWave One — Prototype",
    page_icon="🏢",
    layout="wide",  # wide gives more flexibility on mobile
)

# ---------------------------------------
# CUSTOM CSS for Mobile Responsiveness
# ---------------------------------------
st.markdown("""
<style>
/* General */
body, [class^="css"] {
    font-family: 'Inter', sans-serif;
}
@media (max-width: 768px) {
    section.main > div {
        padding: 0.8rem 0.6rem !important;
    }
    h1, h2, h3 {
        font-size: 1.1rem !important;
    }
    .stButton>button {
        width: 100% !important;
        font-size: 0.9rem !important;
    }
    .stDataFrame, .stTable {
        overflow-x: auto;
    }
    .stPlotlyChart {
        height: 300px !important;
    }
    .stMetric {
        font-size: 0.8rem !important;
    }
}
/* Compact sidebar for mobile */
[data-testid="stSidebar"] {
    width: 240px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# MOCK DATA
# ---------------------------------------
centers_df = pd.DataFrame({
    "city": ["Mumbai","Delhi","Bengaluru","Pune","Kolkata","Ahmedabad"],
    "occupancy": [72,66,78,85,63,60],
})
rev_df = pd.DataFrame({
    "year":[2024,2025,2026,2027],
    "revenue_cr":[540,620,780,1020]
})
enterprise_df = pd.DataFrame({
    "Client":["TechNova","FinSol","RetailWave"],
    "Seats":[120,80,60],
    "City":["Pune","Bengaluru","Mumbai"],
    "Status":["Active","Active","Pilot"]
})

# ---------------------------------------
# SIDEBAR MENU
# ---------------------------------------
st.sidebar.title("WorkWave One")
st.sidebar.caption("Hybrid Workspace Prototype")
with st.sidebar.expander("📍 Navigation", expanded=True):
    page = st.radio("", ["Dashboard", "Memberships", "Enterprise", "Analytics", "Partners"], label_visibility="collapsed")

st.sidebar.markdown("---")
st.sidebar.caption(f"Updated {datetime.now().strftime('%d %b %Y, %I:%M %p')}")

# ---------------------------------------
# PAGE 1: DASHBOARD
# ---------------------------------------
if page == "Dashboard":
    st.title("🏢 WorkWave One Dashboard")
    st.caption("Quick snapshot of performance metrics and occupancy trends")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Occupancy Rate", "68%", "Goal 80%")
    with col2:
        st.metric("Enterprise Clients", "3", "Target 10")

    col3, col4 = st.columns(2)
    with col3:
        st.metric("Cost Reduction", "₹40 Cr", "Saved FY24")
    with col4:
        st.metric("Revenue", "₹540 Cr", "Target ₹1000 Cr")

    st.markdown("---")
    st.subheader("📊 Occupancy by City")
    fig = px.bar(centers_df, x="city", y="occupancy", text="occupancy", height=340)
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("💹 Revenue Growth Forecast")
    fig2 = px.line(rev_df, x="year", y="revenue_cr", markers=True)
    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------
# PAGE 2: MEMBERSHIPS
# ---------------------------------------
elif page == "Memberships":
    st.title("🔗 WorkWave Connect Memberships")
    st.caption("Tiered virtual & hybrid plans")

    plans = [
        {"name":"Basic","price":"₹499 / mo","features":["Community Access","Monthly Events","Job Board"]},
        {"name":"Pro","price":"₹1299 / mo","features":["All Basic + Meeting Hours","On-Demand Rooms","Priority Support"]},
        {"name":"Enterprise","price":"Custom","features":["Corporate Billing","Analytics Dashboard","Custom SLAs"]},
    ]

    for plan in plans:
        with st.container():
            st.markdown(f"### {plan['name']} — {plan['price']}")
            st.write(", ".join(plan["features"]))
            st.button(f"Request Demo for {plan['name']}")

# ---------------------------------------
# PAGE 3: ENTERPRISE SOLUTIONS
# ---------------------------------------
elif page == "Enterprise":
    st.title("🏢 Enterprise Solutions")
    st.caption("Mock enterprise workspace overview")

    st.dataframe(enterprise_df, use_container_width=True, hide_index=True)

    selected = st.selectbox("Select Client", enterprise_df["Client"])
    row = enterprise_df[enterprise_df["Client"] == selected].iloc[0]
    st.metric("Seats", row["Seats"])
    st.metric("City", row["City"])
    st.metric("Status", row["Status"])

    usage = pd.DataFrame({"Month":["Apr","May","Jun","Jul"], "Utilization":[60,65,72,78]})
    st.subheader("Utilization Trend")
    fig = px.line(usage, x="Month", y="Utilization", markers=True)
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------
# PAGE 4: ANALYTICS
# ---------------------------------------
elif page == "Analytics":
    st.title("📈 Analytics & Simulator")

    st.subheader("Occupancy vs Revenue (Mock)")
    merged = pd.DataFrame({
        "Occupancy":[60,65,70,75,80,85],
        "Revenue":[480,540,620,700,820,1000]
    })
    fig = px.line(merged, x="Occupancy", y="Revenue", markers=True, height=340)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("What-if Simulator")
    occ = st.slider("Occupancy %", 50, 95, 68)
    revenue = 540 + (occ - 68) * 8
    st.metric("Simulated Revenue", f"₹{revenue:.0f} Cr")

# ---------------------------------------
# PAGE 5: PARTNER SERVICES
# ---------------------------------------
elif page == "Partners":
    st.title("🤝 Partner Integrations")
    st.caption("UI only — tap to explore categories")

    partners = ["HR Tech", "Facility Mgmt", "Wellness", "Local Retail", "Legal Advisory"]
    for p in partners:
        st.button(f"Connect {p}")

# ---------------------------------------
# FOOTER
# ---------------------------------------
st.markdown("---")
st.caption("© 2025 WorkWave Spaces — Non-functional UI Prototype for demonstration. Optimized for mobile view.")
