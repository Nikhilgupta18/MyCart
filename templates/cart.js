// console.log('hi');
if (localStorage.getItem('cart') == null){
    var cart = {};
}

    else{
        cart = JSON.parse(localStorage.getItem('cart'));
        document.getElementById('cart').innerHTML = Object.keys(cart).length;
    }

    $('.cart').click(function(){
    // console.log(idstr);
    var idstr = this.id.toString();
    if (cart[idstr] != undefined){
        cart[idstr] = cart[idstr]+1;
    }
    else{
        cart[idstr] = 1;
    }
    console.log(cart);
    localStorage.setItem('cart', JSON.stringify(cart));
});