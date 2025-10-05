from pyscript import document


prices = {
    "Ham and Cheese Sandwich": 100,
    "Croissant": 80,
    "Apple Tart": 95,
    "Cinnamon Pie": 120
}


def create_order(event):
    name = document.getElementById("cust_name").value.strip()
    address = document.getElementById("cust_address").value.strip()
    number = document.getElementById("cust_number").value.strip()

    selected = []
    total = 0

    for fid, item in {
        "food1": "Ham and Cheese Sandwich",
        "food2": "Croissant",
        "food3": "Apple Tart",
        "food4": "Cinnamon Pie"
    }.items():
        checkbox = document.getElementById(fid)
        if checkbox.checked:
            selected.append(item)
            total += prices[item]

    if not name or not address or not number:
        message = "⚠️ Please fill in all customer details."
    elif not selected:
        message = "⚠️ Please select at least one item."
    else:
        items_list = "\n".join(selected)
        message = f"""
Order for: {name}
Address: {address}
Contact Number: {number}

Items Ordered:
{items_list}

Total Amount: ₱{total}.00
Thank you for ordering at Breworries! ☕
        """

    document.getElementById("order-summary").innerHTML = f"<pre>{message}</pre>"



def send_message(event):
    name = document.getElementById("name").value.strip()
    email = document.getElementById("email").value.strip()
    msg = document.getElementById("message").value.strip()

    if not name or not email or not msg:
        response = "⚠️ Please fill out all fields before sending."
    else:
        response = f"""
Thank you, {name}! 💌

We’ve received your message:
"{msg}"

We'll reach out to you soon at: {email}
– Breworries Team ☕
        """

    document.getElementById("contact-result").innerHTML = f"<pre>{response}</pre>"
