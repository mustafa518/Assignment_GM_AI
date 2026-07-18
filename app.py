import streamlit as st
import pandas as pd

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Fast Food Ordering System",
    page_icon="🍔",
    layout="wide"
)

# -------------------------
# Menu Data (Always Fresh)
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
        5.00,
        7.00,
        8.00,
        12.00,
        16.00,
        6.00
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
            st.write(f"✅ {item['Item']} - ${item['Price']:.2f}")
            total += item["Price"]

        st.divider()
        st.subheader(f"💰 Total: ${total:.2f}")

        if st.button("🗑 Clear Cart"):
            st.session_state.cart = []
            st.rerun()

# -------------------------
# Main Dashboard
# -------------------------
st.title("🍔 Fast Food Ordering System")
st.write("### Choose your favorite food")

cols = st.columns(3)

for i, row in menu.iterrows():

    with cols[i % 3]:

        with st.container(border=True):

            st.subheader(row["Item"])
            st.write(f"Category: {row['Category']}")
            st.write(f"Price: ${row['Price']:.2f}")

            if st.button("Add to Cart", key=i):
                st.session_state.cart.append({
                    "Item": row["Item"],
                    "Price": row["Price"]
                })
                st.success(f"{row['Item']} Added!")

# -------------------------
# Checkout
# -------------------------
st.divider()
st.header("🧾 Checkout")

if len(st.session_state.cart) > 0:

    total = sum(item["Price"] for item in st.session_state.cart)

    st.subheader(f"Total Bill: ${total:.2f}")

    with st.form("checkout"):

        name = st.text_input("👤 Customer Name")

        address = st.text_area("🏠 Delivery Address")

        phone = st.text_input("📞 Contact Number")

        st.info("Payment Method: Cash on Delivery")

        order = st.form_submit_button("✅ Place Order")

        if order:

            if name and address and phone:

                st.success("🎉 Order Placed Successfully!")
                st.balloons()

                st.write("## Order Summary")

                for item in st.session_state.cart:
                    st.write(f"- {item['Item']} (${item['Price']:.2f})")

                st.write(f"### Total Bill: ${total:.2f}")
                st.write(f"👤 Customer: {name}")
                st.write(f"🏠 Address: {address}")
                st.write(f"📞 Phone: {phone}")

                st.session_state.cart = []

            else:
                st.error("Please fill all fields.")

else:
    st.info("Please add food items to your cart.")
