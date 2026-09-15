
import streamlit as st

from agent import (
    create_plan,
    execute_plan,
    review_result,
    improve_result
)


st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Research Agent")

st.write(
    "Give the agent a goal and let it plan, execute, "
    "review, and improve the result."
)

goal = st.text_area(
    "Enter your goal",
    placeholder="Example: Create a 30-day plan to learn Machine Learning"
)


if st.button("🚀 Run Agent"):

    if not goal.strip():
        st.warning("Please enter a goal first.")

    else:

        # Step 1: Create a plan
        plan = create_plan(goal)

        # Step 2: Execute the plan
        result = execute_plan(goal, plan)

        # Step 3: Review the result internally
        feedback = review_result(goal, result)

        # Step 4: Improve the result internally
        final_result = improve_result(
            goal,
            result,
            feedback
        )

        # Show only the final useful result to the user
        st.subheader("📄 Final Result")

        st.write(final_result)

        st.success("Agent completed successfully! 🎉")

