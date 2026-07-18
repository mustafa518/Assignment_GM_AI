import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Fast Food Ordering System",
    page_icon="🍔",
    layout="wide"
)

# -----------------------------
# Menu Data
# -----------------------------
if "menu" not in st.session_state:
    st.session_state.menu = pd.DataFrame({
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
            5.00,
            7.00,
            8.00,
            12.00,
            16.00,
            6.00
        ]
    })

# -----------------------------
# Cart Initialization
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# -----------------------------
# Sidebar Cart
# -----------------------------
with st.sidebar:
    st.header("🛒 Your Cart")

    if st.session_state.cart:

        for item in st.session_state.cart:
            st.write(f"✅ {item['Item']} - ${item['Price']:.2f}")

        st.divider()

        total = sum(item["Price"] for item in st.session_state.cart)

        st.subheader(f"💰 Total: ${total:.2f}")

        if st.button("🗑️ Clear Cart"):
            st.session_state.cart = []
            st.rerun()

    else:
        st.info("Your cart is empty.")

# -----------------------------
# Main Dashboard
# -----------------------------
st.title("🍔 Fast Food Ordering System")
st.markdown("### Welcome! Select your favorite food and place your order.")

cols = st.columns(3)

for index, row in st.session_state.menu.iterrows():

    with cols[index % 3]:

        with st.container(border=True):

            st.subheader(row["Item"])
            st.write(f"**Category:** {row['Category']}")
            st.write(f"**Price:** ${row['Price']:.2f}")

            if st.button("Add to Cart", key=index):
                st.session_state.cart.append({
                    "Item": row["Item"],
                    "Price": row["Price"]
                })
                st.toast(f"{row['Item']} Added to Cart!")

# -----------------------------
# Checkout
# -----------------------------
st.divider()
st.header("🧾 Checkout")

if st.session_state.cart:

    total_amount = sum(item["Price"] for item in st.session_state.cart)

    st.subheader(f"Total Bill: ${total_amount:.2f}")

    with st.form("checkout_form"):

        name = st.text_input("👤 Customer Name")

        address = st.text_area("🏠 Delivery Address")

        phone = st.text_input("📞 Contact Number")

        st.info("💵 Payment Method: Cash on Delivery")

        submit = st.form_submit_button("✅ Place Order")

        if submit:

            if name and address and phone:

                st.success("🎉 Order Placed Successfully!")

                st.balloons()

                st.write(f"### Thank You, {name}!")

                st.write("#### 🛍️ Order Summary")

                for item in st.session_state.cart:
                    st.write(f"- {item['Item']} (${item['Price']:.2f})")

                st.write(f"### 💰 Total Bill: ${total_amount:.2f}")
                st.write(f"📍 Delivery Address: {address}")
                st.write(f"📞 Contact Number: {phone}")
                st.write("🚚 Your order will be delivered soon.")

                st.session_state.cart = []

            else:
                st.error("Please fill in all the required fields.")

else:
    st.info("Add food items to your cart before checkout.")
