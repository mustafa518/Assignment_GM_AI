import streamlit as st
import pandas as pd

# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="GM Fast Food",
    page_icon="🍔",
    layout="wide"
)

# -------------------------
# Menu Data
# -------------------------

menu = pd.DataFrame({
    "Item": [
        "Sandwich 🥪",
        "Burger 🍔",
        "Pizza 🍕 (Small)",
        "Pizza 🍕 (Medium)",
        "Pizza 🍕 (Large)",
        "Chicken Roll 🍗"
    ],
    "Category": [
        "Fast Food",
        "Fast Food",
        "Pizza",
        "Pizza",
        "Pizza",
        "Fast Food"
    ],
    "Price": [
        350,
        550,
        800,
        1200,
        1800,
        400
    ]
})

# -------------------------
# Cart
# -------------------------

if "cart" not in st.session_state:
    st.session_state.cart = []

# -------------------------
# Sidebar
# -------------------------

with st.sidebar:

    st.title("🛒 Your Cart")

    if len(st.session_state.cart) == 0:
        st.info("Cart is Empty")

    else:

        total = 0

        for item in st.session_state.cart:
            st.write(f"✅ {item['Item']} - PKR {item['Price']}")
            total += item["Price"]

        st.divider()
        st.subheader(f"💰 Total: PKR {total}")

        if st.button("🗑 Clear Cart"):
            st.session_state.cart = []
            st.rerun()

# -------------------------
# Main Dashboard
# -------------------------

st.title("🍔 GM Fast Food")
st.write("### Welcome to GM Fast Food - Fresh, Delicious & Affordable Meals")

cols = st.columns(3)

for i, row in menu.iterrows():

    with cols[i % 3]:

        with st.container(border=True):

            st.subheader(row["Item"])
            st.write(f"Category: {row['Category']}")
            st.write(f"Price: PKR {row['Price']}")

            if st.button("Add to Cart", key=i):

                st.session_state.cart.append({
                    "Item": row["Item"],
                    "Price": row["Price"]
                })

                st.success(f"✅ {row['Item']} Added to Cart!")

# -------------------------
# Checkout
# -------------------------

st.divider()
st.header("🧾 Checkout")

if len(st.session_state.cart) > 0:

    total = sum(item["Price"] for item in st.session_state.cart)

    st.subheader(f"Total Bill: PKR {total}")

    with st.form("checkout"):

        name = st.text_input("👤 Customer Name")
        address = st.text_area("🏠 Delivery Address")
        phone = st.text_input("📞 Contact Number")

        st.info("💵 Payment Method: Cash on Delivery")

        order = st.form_submit_button("✅ Place Order")

        if order:

            if name and address and phone:

                st.success("🎉 Order Placed Successfully!")
                st.balloons()

                st.markdown(f"""
                ## 🍔 Thank You for Choosing GM Fast Food!

                Dear **{name}**,

                Your order has been successfully confirmed and our kitchen team has started preparing your meal.

                ### 📦 Order Details
                - Customer: **{name}**
                - Contact: **{phone}**
                - Delivery Address: **{address}**
                - Total Bill: **PKR {total}**

                ### 🚚 Delivery Information
                Estimated Delivery Time: **20-30 Minutes**

                We are committed to providing fresh, delicious, and high-quality food.

                ❤️ Thank you for trusting **GM Fast Food**.

                We hope you enjoy your meal and look forward to serving you again.

                **Best Regards,**  
                **GM Fast Food Team**
                """)

                st.write("### 🧾 Ordered Items")

                for item in st.session_state.cart:
                    st.write(f"🍽️ {item['Item']} - PKR {item['Price']}")

                st.info(
                    "🍟 Tip: Add a cold drink with your next order for a complete meal experience!"
                )

                st.session_state.cart = []

            else:
                st.error("⚠️ Please fill all required fields.")

else:
    st.info("🍔 Please add food items to your cart.")
