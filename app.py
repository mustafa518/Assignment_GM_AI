st.divider()

st.markdown("""
# 🎉 MEGA SAVING DEALS 🎉
### Save More • Eat More • Enjoy More
""")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):

        st.subheader("🌯🍟🥤 Shawarma Starter Deal")

        st.write("📦 Includes:")
        st.write("✅ Chicken Shawarma 🌯")
        st.write("✅ French Fries 🍟")
        st.write("✅ 1.5L Cold Drink 🥤")

        st.success("💰 PKR 999")

        if st.button("Add Deal", key="deal1"):
            st.session_state.cart.append({
                "Item": "🌯🍟🥤 Shawarma Starter Deal",
                "Price": 999
            })
            st.success("Deal Added!")

with col2:
    with st.container(border=True):

        st.subheader("🍔🌯🥤 Burger Shawarma Deal")

        st.write("📦 Includes:")
        st.write("✅ Zinger Burger 🍔")
        st.write("✅ Chicken Shawarma 🌯")
        st.write("✅ 1.5L Cold Drink 🥤")

        st.success("💰 PKR 1299")

        if st.button("Add Deal", key="deal2"):
            st.session_state.cart.append({
                "Item": "🍔🌯🥤 Burger Shawarma Deal",
                "Price": 1299
            })
            st.success("Deal Added!")

with col3:
    with st.container(border=True):

        st.subheader("🧀🍔🍟🥤 Burger Fries Deal")

        st.write("📦 Includes:")
        st.write("✅ Cheese Burger 🧀🍔")
        st.write("✅ French Fries 🍟")
        st.write("✅ 1.5L Cold Drink 🥤")

        st.success("💰 PKR 1099")

        if st.button("Add Deal", key="deal3"):
            st.session_state.cart.append({
                "Item": "🧀🍔🍟🥤 Burger Fries Deal",
                "Price": 1099
            })
            st.success("Deal Added!")
