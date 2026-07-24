import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Organizational Cognition Engine", layout="wide")

st.title("Serverless Organizational Cognition Pipeline")
st.caption("Real-Time NLP Analysis: ESG Backlash & Ecosystem Orchestration")

st.sidebar.header("Data Ingestion Configuration")
selected_ecosystem = st.sidebar.selectbox("Target Corporate Ecosystem", ["Global Energy Sector", "European Financial Markets", "Transnational Supply Chains"])
backlash_severity = st.sidebar.slider("Simulate ESG Backlash Intensity", 1.0, 5.0, 3.5)
run_simulation = st.sidebar.button("Initialize NLP Cloud Engine")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: Corporate API Text Ingestion -> LLM Sentiment Vectorization")

if run_simulation:
    st.subheader(f"Active Ecosystem Orchestration Monitor: {selected_ecosystem}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_volume = col1.empty()
    metric_backlash = col2.empty()
    metric_orchestration = col3.empty()
    metric_status = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(2027)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    backlash_indices = []
    orchestration_scores = []
    
    base_backlash = 20.0 
    base_orchestration = 85.0
    
    for i in range(100):
        velocity = int(np.random.uniform(5000, 15000))
        
        if i < 35:
            current_backlash = base_backlash + np.random.uniform(-2.0, 2.0)
            current_orchestration = base_orchestration + np.random.uniform(-1.0, 1.0)
            status = "STABLE REGULATORY ENVIRONMENT"
        elif i >= 35 and i < 65:
            current_backlash = base_backlash + (i - 35) * (1.5 * backlash_severity) + np.random.uniform(-5.0, 5.0)
            current_orchestration = base_orchestration - (i - 35) * (0.8 * backlash_severity) + np.random.uniform(-2.0, 2.0)
            status = "ESG BACKLASH DETECTED"
        else:
            current_backlash = current_backlash - np.random.uniform(0.5, 2.0)
            current_orchestration = current_orchestration + np.random.uniform(1.0, 3.0)
            status = "STRATEGIC DECOUPLING ACTIVE"
            
        current_orchestration = max(0.0, current_orchestration)
            
        backlash_indices.append(current_backlash)
        orchestration_scores.append(current_orchestration)
        
        metric_volume.metric("Textual Nodes Ingested", f"{velocity:,} / sec")
        metric_backlash.metric("ESG Backlash Exposure Index", f"{current_backlash:.1f} pts", f"+{(current_backlash - base_backlash):.1f} Risk")
        metric_orchestration.metric("Ecosystem Orchestration Efficiency", f"{current_orchestration:.1f}%")
        
        if status == "ESG BACKLASH DETECTED":
            metric_status.metric("Managerial Cognition State", status, "High Institutional Friction")
        elif status == "STRATEGIC DECOUPLING ACTIVE":
            metric_status.metric("Managerial Cognition State", status, "Adapting Narrative")
        else:
            metric_status.metric("Managerial Cognition State", status, "Normal")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=backlash_indices, mode='lines', name='ESG Backlash Index', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=orchestration_scores, mode='lines', name='Orchestration Efficiency (%)', yaxis='y2', line=dict(color='blue', dash='dot')))
        
        fig.update_layout(
            title="Organizational Cognition: Regulatory Backlash vs Ecosystem Orchestration",
            xaxis=dict(title="High-Frequency API Timeline"),
            yaxis=dict(title="Backlash Index (Pts)"),
            yaxis2=dict(title="Orchestration Efficiency (%)", overlaying='y', side='right', range=[0, 100]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if status == "ESG BACKLASH DETECTED" and i == 35:
            log_placeholder.error(f"INSTITUTIONAL ALERT: Severe spike in anti-ESG sentiment detected across social and regulatory APIs at {time_steps[i].strftime('%H:%M:%S')}. NLP engine mapping sudden degradation in supply chain orchestration efficiency.")
        elif status == "STRATEGIC DECOUPLING ACTIVE" and i == 65:
            log_placeholder.warning(f"COGNITION SHIFT: Cloud middleware detects corporate communications pivoting. Managerial rhetoric adjusting to mitigate regulatory exposure. Efficiency recovering.")
        elif status == "STABLE REGULATORY ENVIRONMENT" and i % 5 == 0:
            log_placeholder.success(f"Log: Telemetry tick {i} ingested. Automated qualitative coding executing via AWS Lambda with zero latency.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. The serverless NLP pipeline successfully quantified qualitative organizational shifts in real-time.")
else:
    st.info("Click 'Initialize NLP Cloud Engine' in the sidebar to simulate high-frequency text ingestion.")