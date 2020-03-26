if (localStorage.getItem('cart') == null){
    var cart = {};
}

    else{
        cart = JSON.parse(localStorage.getItem('cart'));
        document.getElementById('cart').innerHTML = Object.keys(cart).length;
        updateCart(cart);
    }

    $('.cart').click(function(){
    // console.log(idstr);
    var idstr = this.id.toString();
    if (cart[idstr] !== undefined){
        cart[idstr] = cart[idstr]+1;
    }
    else{
        cart[idstr] = 1;
    }
    updateCart(cart);
    // console.log(cart);
    // localStorage.setItem('cart', JSON.stringify(cart));
});

function updateCart(cart) {
    for(var item in cart){
        document.getElementById('div' + item).innerHTML = "<button id ='minus"+item + "'class='btn btn-primary minus'>-</button><span id='val" + item + "'>" +cart[item] + "</span> <button id='plus" +item+ "' class='btn btn-primary plus'> +</button>";
    }
    localStorage.setItem('cart',JSON.stringify(cart));
    console.log(cart);
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
}
$('.divcart').on("click", "button.minus", function () {
    a = this.id.slice(5, );
    cart[a] = cart[a] -1;
    cart[a]=Math.max(0, cart[a]);
    document.getElementById('val'+a).innerHTML = cart[a];
    updateCart(cart);

});

$('.divcart').on("click", "button.plus", function () {
    a = this.id.slice(4, );
    cart[a] = cart[a] +1;
    document.getElementById('val'+a).innerHTML = cart[a];
    updateCart(cart);

});