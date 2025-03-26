@app.route('/admin/add-product', methods=['GET','POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        # Database mein add karo
    return render_template('admin/add_product.html')