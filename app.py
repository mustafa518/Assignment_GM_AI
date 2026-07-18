import streamlit as st
import pandas as pd

# ---------------------------
# Page Setup
# ---------------------------
st.set_page_config(page_title="GM Fast Food", page_icon="🍔")

st.title("🍔 GM Fast Food")
st.write("### Fresh • Delicious • Affordable")

# ---------------------------
# Menu
# ---------------------------
menu = pd.DataFrame({
    "Item": [
        "🍔 Zinger Burger",
        "🧀🍔 Cheese Burger",
        "🍟 French Fries",
        "🌯 Chicken Shawarma",
        "🥪🧀 Grilled Cheese Sandwich",
        "🍢 Reshmi Kabab",
        "🍗 Chicken Nuggets",
        "🍕 Pizza"
    ],
    "Price": [
        650,
        750,
        300,
        450,
        550,
        700,
        500,
        1200
    ]
})

# ---------------------------
# Deals
# ---------------------------
deals = pd.DataFrame({
    "Item": [
        "🌯🍟🥤 Shawarma Starter Deal",
        "🍔🌯🥤 Burger Shawarma Deal",
        "🧀🍔🍟🥤 Burger Fries Deal"
    ],
    "Price": [
        999,
        1299,
        1099
    ]
})

# ---------------------------
# Cart
# ---------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# Sidebar Cart
with st.sidebar:
    st.header("🛒 Your Cart")

    total = sum(item["Price"] for item in st.session_state.cart)

    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(f"✅ {item['Item']} - PKR {item['Price']}")

        st.subheader(f"💰 Total: PKR {total}")

        if st.button("🗑 Clear Cart"):
            st.session_state.cart = []
            st.rerun()
    else:
        st.info("Cart is Empty")

# ---------------------------
# Food Items
# ---------------------------
st.header("📋 Menu")

cols = st.columns(2)

for i, row in menu.iterrows():
    with cols[i % 2]:
        with st.container(border=True):
            st.subheader(row["Item"])
            st.write(f"💰 PKR {row['Price']}")

            if st.button("Add to Cart", key=f"food{i}"):
                st.session_state.cart.append({
                    "Item": row["Item"],
                    "Price": row["Price"]
                })
                st.success("Added!")

# ---------------------------
# Deals Section
# ---------------------------
st.divider()

st.markdown("## 🎉 MEGA SAVING DEALS 🎉")

cols = st.columns(3)

for i, row in deals.iterrows():
    with cols[i]:
        with st.container(border=True):
            st.subheader(row["Item"])
            st.write(f"💰 PKR {row['Price']}")

            if st.button("Add Deal", key=f"deal{i}"):
                st.session_state.cart.append({
                    "Item": row["Item"],
                    "Price": row["Price"]
                })
                st.success("Deal Added!")

# ---------------------------
# Checkout
# ---------------------------
st.divider()
st.header("🧾 Checkout")

if st.session_state.cart:

    total = sum(item["Price"] for item in st.session_state.cart)

    name = st.text_input("👤 Customer Name")
    address = st.text_area("🏠 Delivery Address")
    phone = st.text_input("📞 Contact Number")

    if st.button("✅ Place Order"):

        if not name or not address or not phone:
            st.error("Please fill all fields.")

        elif not (
            phone.startswith("03")
            and len(phone) == 11
            and phone.isdigit()
        ):
            st.error(
                "❌ Wrong Credentials! Phone number must start with 03 and contain 11 digits."
            )

        else:
            st.success("🎉 Order Placed Successfully!")
            st.balloons()

            st.write("### 🛍️ Order Summary")

            for item in st.session_state.cart:
                st.write(f"✅ {item['Item']} - PKR {item['Price']}")

            st.success(
                f"""
🍔 Thank you {name}!

Your order has been confirmed.

💰 Total Bill: PKR {total}

🚚 Estimated Delivery Time: 20-30 Minutes

❤️ Thank you for choosing GM Fast Food.
We look forward to serving you again!
                """
            )

            st.session_state.cart = []

else:
    st.info("Add food items or deals to your cart first.")
