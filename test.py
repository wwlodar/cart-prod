from main import cart_product


def test_cart_product():
    in_put = [{'name': '#x', 'words': ['x', 'xx']}, {'name': '#y', 'words': ['y', 'yy', '#x #y']}]
    out_put = [{'name': '#x', 'words': ['x', 'xx']}, {'name': '#y', 'words': ['y', 'yy', 'x y', 'x yy', 'xx y', 'xx yy']}]
    
    assert cart_product(in_put) == out_put
