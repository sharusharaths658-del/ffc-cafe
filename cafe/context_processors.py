def cart_count(request):
    cart = request.session.get('cart', {})
    count = len(cart)
    return {
        'cart_count': count
    }