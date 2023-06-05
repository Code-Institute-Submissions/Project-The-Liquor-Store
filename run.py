from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def display_menu():
    return render_template('pages/index.html')

def calculate_total(price, quantity):
    return price * quantity

@app.route('/order', methods=['POST'])
def place_order():
    continue_order = request.form.get('continue_order')
    if continue_order and continue_order.lower() == "yes":
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        id_number = request.form.get('id_number')

        selection = int(request.form.get('selection'))
        quantity = int(request.form.get('quantity'))
        total = 0

        if selection == 1:
            if quantity > 0:
                total = calculate_total(20, quantity)
                item_name = "Vodka 750ml"
        elif selection == 2:
            if quantity > 0:
                total = calculate_total(25, quantity)
                item_name = "Red Label 750ml"
        elif selection == 3:
            if quantity > 0:
                total = calculate_total(30, quantity)
                item_name = "Jack Daniels 750ml"
        elif selection == 4:
            if quantity > 0:
                total = calculate_total(30, quantity)
                item_name = "Cabernet Sauvignon"
        elif selection == 5:
            if quantity > 0:
                total = calculate_total(25, quantity)
                item_name = "Merlot"
        elif selection == 6:
            if quantity > 0:
                total = calculate_total(35, quantity)
                item_name = "Pinot Noir"
        elif selection == 7:
            if quantity > 0:
                total = calculate_total(30, quantity)
                item_name = "Chardonnay"
        elif selection == 8:
            if quantity > 0:
                total = calculate_total(25, quantity)
                item_name = "Sauvignon Blanc"
        elif selection == 9:
            if quantity > 0:
                total = calculate_total(35, quantity)
                item_name = "Riesling"
        elif selection == 10:
            if quantity > 0:
                total = calculate_total(10, quantity)
                item_name = "Carlsberg"
        elif selection == 11:
            if quantity > 0:
                total = calculate_total(8, quantity)
                item_name = "Heineken"
        elif selection == 12:
            if quantity > 0:
                total = calculate_total(5, quantity)
                item_name = "Corona"

        return render_template('order_confirmation.html', name=name, phone_number=phone_number, address=address,
                               id_number=id_number, item_name=item_name, quantity=quantity, total=total)
    else:
        return "Thank you for shopping with us. Goodbye!"

if __name__ == "__main__":
    app.run(debug=True)
