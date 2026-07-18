import streamlit as st

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="GM Fast Food",
    page_icon="🍔",
    layout="wide"
)

# ----------------------------------
# SESSION STATE
# ----------------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# ----------------------------------
# MENU ITEMS
# ----------------------------------
menu = [
    {"Item": "🍔 Zinger Burger", "Price": 650},
    {"Item": "🧀🍔 Cheese Burger", "Price": 750},
    {"Item": "🍟 French Fries", "Price": 300},
    {"Item": "🌯 Chicken Shawarma", "Price": 450},
    {"Item": "🥪🧀 Grilled Cheese Sandwich", "Price": 550},
    {"Item": "🍢 Reshmi Kabab", "Price": 700},
    {"Item": "🍗 Chicken Nuggets", "Price": 500},
    {"Item": "🍕 Pizza", "Price": 1200}
]

# ----------------------------------
# DEALS
# ----------------------------------
deals = [
    {
        "name": "🌯🍟🥤 Shawarma Starter Deal",
        "price": 999,
        "items": [
            "Chicken Shawarma 🌯",
            "French Fries 🍟",
            "1.5L Cold Drink 🥤"
        ]
    },
    {
        "name": "🍔🌯🥤 Burger Shawarma Deal",
        "price": 1299,
        "items": [
            "Zinger Burger 🍔",
            "Chicken Shawarma 🌯",
            "1.5L Cold Drink 🥤"
        ]
    },
    {
        "name": "🧀🍔🍟🥤 Burger Fries Deal",
        "price": 1099,
        "items": [
            "Cheese Burger 🧀🍔",
            "French Fries 🍟",
            "1.5L Cold Drink 🥤"
        ]
    }
]

# ----------------------------------
# SIDEBAR CART
# ----------------------------------
with st.sidebar:

    st.write("👨‍💼 Owner: Ghulam Mustafa")

    st.title("🛒 Your Cart")

    if len(st.session_state.cart) == 0:
        st.info("Cart is Empty")

    else:

        total = sum(item["Price"] for item in st.session_state.cart)

        for item in st.session_state.cart:
            st.write(f"✅ {item['Item']} - PKR {item['Price']}")

        st.divider()

        st.subheader(f"💰 Total: PKR {total}")

        if st.button("🗑 Clear Cart"):
            st.session_state.cart = []
            st.rerun()

# ----------------------------------
# HEADER
# ----------------------------------
st.title("🍔 GM FAST FOOD")

st.write("👨‍💼 Owner: Ghulam Mustafa")

st.markdown("""
### 😋 Welcome to GM Fast Food

Fresh Burgers • Crispy Fries • Delicious Shawarma • Hot Pizza

🚚 Fast Delivery | 💯 Quality Food | 💵 Cash On Delivery
""")

st.info("🔥 Today's Special: Buy Any Burger & Get 20% OFF on French Fries!")

# ----------------------------------
# MENU
# ----------------------------------
st.header("📋 Our Special Menu")

cols = st.columns(2)

for i, item in enumerate(menu):

    with cols[i % 2]:

        with st.container(border=True):

            st.subheader(item["Item"])
            st.write(f"💰 Price: PKR {item['Price']}")

            if st.button("➕ Add to Cart", key=f"menu_{i}"):

                st.session_state.cart.append({
                    "Item": item["Item"],
                    "Price": item["Price"]
                })

                st.success("Added Successfully!")

# ----------------------------------
# DEALS
# ----------------------------------
st.divider()

st.markdown("""
# 🎉 MEGA SAVING DEALS 🎉
### Save More • Eat More • Enjoy More ❤️
""")

deal_cols = st.columns(3)

for i, deal in enumerate(deals):

    with deal_cols[i]:

        with st.container(border=True):

            st.subheader(deal["name"])

            st.write("📦 Includes:")

            for item in deal["items"]:
                st.write(f"✅ {item}")

            st.success(f"💰 PKR {deal['price']}")

            if st.button("Add Deal", key=f"deal_{i}"):

                st.session_state.cart.append({
                    "Item": deal["name"],
                    "Price": deal["price"]
                })

                st.success("Deal Added!")

# ----------------------------------
# CHECKOUT
# ----------------------------------
st.divider()

st.header("🧾 Checkout")

if len(st.session_state.cart) > 0:

    total = sum(item["Price"] for item in st.session_state.cart)

    st.subheader(f"💰 Total Bill: PKR {total}")

    name = st.text_input("👤 Customer Name")
    address = st.text_area("🏠 Delivery Address")
    phone = st.text_input("📞 Contact Number")

    if st.button("✅ Place Order"):

        if not name or not address or not phone:

            st.error("⚠️ Please fill all fields.")

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

            st.markdown(f"""
### 🍔 Thank You For Choosing GM Fast Food!

Dear **{name}**,

✅ Your order has been successfully confirmed.

📞 Contact Number: **{phone}**

🏠 Delivery Address: **{address}**

💰 Total Bill: **PKR {total}**

🚚 Estimated Delivery Time: **20-30 Minutes**

👨‍🍳 Our team has started preparing your order.

❤️ Thank you for choosing GM Fast Food.

We hope you enjoy your meal and look forward to serving you again.
""")

            st.write("### 🛍️ Order Summary")

            for item in st.session_state.cart:
                st.write(f"✅ {item['Item']} - PKR {item['Price']}")

            st.session_state.cart = []

else:

    st.info("🍔 Please add food items or deals to your cart.")

# ----------------------------------
# FOOTER
# ----------------------------------
st.divider()

st.markdown("""
### ❤️ Thank You For Visiting GM Fast Food

📍 Fresh Food Everyday  
📞 Customer Support Available  
🚚 Fast & Reliable Delivery

**GM Fast Food Team**
""")
