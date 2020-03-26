let cart = document.querySelectorAll('.cart');
console.log('hi');

for(let i=0; i<cart.length; i++){
    cart[i].addEventListener('click', () => {
       cartNumber();

    });
}
function onLoad() {
        let productno = localStorage.getItem('cart');
        if(productno) {
            document.querySelector('#cart').textContent  = productno;

        }

}
function cartNumber(){
    let productno = localStorage.getItem('cart');

    productno = parseInt(productno);

    if(productno){
      localStorage.setItem('cart',productno + 1);
      document.querySelector( '#cart').textContent=productno+1;

    } else{
        localStorage.setItem('cart',1);
        document.querySelector('#cart').textContent=1;
    }


}
onLoad();
