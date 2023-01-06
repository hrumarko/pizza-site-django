let cards = document.querySelectorAll(".col-4");
let main_amount = parseInt( $('.main-amount').text().split(" ")[0] );
let open_cart = document.querySelector(".open-cart");
let close_cart = document.querySelector(".cart-close-btn");
let card_cart;
let cart_cards = document.querySelector('.myrow');
cart_cards = Array.from(cart_cards.children);
// card_cart = Array.from(card_cart.children);
// let card_cart = document.querySelector(".myrow");

function updateForOne(card){
    
  let name = card.querySelector(".cart-name").textContent;
  let radius = card.querySelector('.cart-radius').textContent;
  let d = card.querySelector('.cart-dough').textContent;
  let price = card.querySelector(".cart-price").textContent;
  let count = parseInt(card.querySelector('.cart-count').textContent);
// cart-price, main-amount, count
  let dct = {
    name: name,
    radius: radius,
    dough: d,
    price: price,
    count: count,
    price_cart: $('.main-amount').text()
  }
  let add_case = JSON.stringify(dct)
  $.post("update-cart/",
    {
      "csrfmiddlewaretoken": getCookie("csrftoken"),
      add_case,
    },
    console.log(add_case)
  );
}

// +1 позиция в корзинео
cart_cards.forEach(function(card){
    if(card.classList[1] != 'hide'){
        
        // -1
        let buttons = card.querySelector(".cart-choose-count");
        btn_incr = buttons.querySelector(".btn-incr");
        btn_incr.addEventListener("click", function(){
          let cnt = parseInt(
            card.querySelector(".cart-count").textContent
          );
          if (cnt > 1) {
            card.querySelector(".cart-count").textContent = cnt - 1;
            let price = parseInt(
              card.querySelector(".cart-main-price").textContent
            );
            let now_price = parseInt(
                card.querySelector('.cart-price').textContent.split(" ")[0]
            )
            main_amount -= price;
            document.querySelector(".main-amount").textContent = main_amount + " ₴";
            let fin_price = ( now_price - price ) + " ₴"
            card.querySelector(".cart-price").textContent = fin_price;
            main_am = $('.main-amount').text()
            console.log(main_am)
            
              updateForOne(card)
              
            // document.querySelector(".main-amount").textContent = main_amount + " ₴";
          }
        })
        
        //+1
        btn_dcr = card.querySelector(".btn-decr");
        btn_dcr.addEventListener("click", function(){
          let cnt = parseInt(
            card.querySelector(".cart-count").textContent
          );
          if (cnt > 0) {
            card.querySelector(".cart-count").textContent = cnt + 1;
            let price = parseInt(
              card.querySelector(".cart-main-price").textContent
            );
            let now_price = parseInt(
                card.querySelector('.cart-price').textContent.split(" ")[0]
            )
            main_amount += price;
            document.querySelector(".main-amount").textContent = main_amount + " ₴";
            let fin_price = ( price + now_price ) + " ₴"
            card.querySelector(".cart-price").textContent = fin_price;
            main_am = $('.main-amount').text()
            console.log(main_am)
            updateForOne(card);
          }
        })
    }
})




function getCookie(name) {
    // get csrftoken
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// покупка(отправка данных на сервер)
let i = 0; 
$('.buy-btn').click(function(){
  var dct = {
  }

  let c = Array.from(document.querySelector('.myrow').children)
  c.forEach(function(card){
    if (card.classList == 'mycol-6'){
        name = card.querySelector('.cart-name').textContent;
        radius = card.querySelector('.cart-radius').textContent;
        dough = card.querySelector('.cart-dough').textContent;
        count = card.querySelector('.cart-count').textContent;
        price = card.querySelector('.cart-price').textContent;
        // dct['pizza' + i] = name + " " + radius + " " + dough + " " + count + " " + price;
        dct['pizza' + i] = {
          name: name,
          radius: radius,
          dough: dough,
          count: count,
          price: price,
        };
        
        i += 1
    }
  })
  mp = document.querySelector('.main-amount').textContent;
  dct['main_price'] = mp;
  let order = JSON.stringify(dct);

  $.post("res/",
    {
      "csrfmiddlewaretoken": getCookie("csrftoken"),
      order,
    },
    
    console.log(order)
    );
  i = 0;
  // window.location.replace("order/");
})

open_cart.addEventListener("click", function () {
    
  let cart = document.querySelector(".cart-popup.disactive");
  cart.classList.remove("disactive");
  let card_cart = document.querySelector(".myrow");
  card_cart = Array.from(card_cart.children);
    
  card_cart.forEach(function(card){
    let clear = card.querySelector(
      ".cart-delete"
    );
    clear.addEventListener("click", function(){
      let amount = card.querySelector(
        ".cart-price"
      ).textContent.split(" ")[0];
      main_amount -= amount;
      document.querySelector(".main-amount").textContent = main_amount + " ₴";
      deleteCase(card); 
      card.remove();
    })
  });
});

close_cart.addEventListener("click", function () {
  let cart = document.querySelector(".cart-popup");
  cart.classList.add("disactive");
});

cards.forEach(function (card) {
  let price = card
    .querySelector(".card-title.pricing-card-title")
    .textContent.split(" ")[0];
  let btns1 = card.querySelector(".options-radius");
  btns1 = Array.from(btns1.children);
  btns1.forEach(function (br) {
    if (price == br.getAttribute("data-price")) {
      br.classList.add("active");
    }
  });
});

cards.forEach(function (card) {
  var main_price = parseInt(
    card
      .querySelector(".card-title.pricing-card-title")
      .textContent.split(" ")[0]
  );
  let el = card.querySelector(".doughs");
  var add_price = parseInt(el.value);

  el.addEventListener("click", function () {
    add_price = parseInt(el.value);
    let res = add_price + main_price;
    card.querySelector(
      ".card-title.pricing-card-title"
    ).textContent = res + " ₴";
  });

  child = Array.from(card.children);
  child.forEach(function (ch) {
    buttons1 = ch.querySelector(".options-radius");
    buttons = Array.from(buttons1.children);
    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        let parentButtons = Array.from(button.parentNode.children);
        parentButtons.forEach(function (button) {
          button.classList.remove("active");
        });
        button.classList.add("active");
        main_price = parseInt(button.getAttribute("data-price"));
        let final_price = main_price + add_price;
        card.querySelector(
          ".card-title.pricing-card-title"
        ).textContent = final_price + " ₴";
      });
    });
  });
});

function addElementInCart(card) {
  let div = document.querySelector(".mycol-6");
  let p = div.cloneNode(true);

  let name = card.querySelector(".my-0").textContent;
  let radius = card.querySelector(".btn-radius.active").textContent;
  let dough = card.querySelector(".doughs");
  let d = dough.options[dough.selectedIndex].text;
  let price = card.querySelector(".card-title").textContent;
  let img = card.querySelector(".img-pizza").src;
  
  let card_cart = document.querySelector(".myrow");
  card_cart = Array.from(card_cart.children);
  let is_in_cart = false;
  if (card_cart.length > 1){
      card_cart.forEach(function(card){
        
        let card_name = card.querySelector(".cart-name").textContent;
        let card_dough = card.querySelector(".cart-dough").textContent;
        let card_radius = card.querySelector(".cart-radius").textContent;
        if (name == card_name && radius == card_radius && d == card_dough){
          let p = card.querySelector(".cart-count").textContent; 
          card.querySelector(".cart-count").textContent = parseInt(p) + 1;
          let cnt = parseInt(card.querySelector(".cart-count").textContent);
          let price = parseInt(card.querySelector(".cart-main-price").textContent);
          card.querySelector(".cart-price").textContent = (cnt) * price + " ₴";
          main_amount = parseInt($(".main-amount").text().split(" ")[0])
          main_amount += price;
          document.querySelector(".main-amount").textContent = main_amount + " ₴";
          is_in_cart = true;
            
          let dct = {
            name: name,
            radius: radius,
            dough: d,
            count: cnt,
            price: cnt * price + " ₴",
            price_cart: $('.main-amount').text()
          }
          let add_case = JSON.stringify(dct)
          console.log(add_case, $('.main-amount').text())
          $.post("update-cart/",
            {
              "csrfmiddlewaretoken": getCookie("csrftoken"),
              add_case,
            },
            console.log(add_case)
          );
        }
      });
  };
  

  if (is_in_cart == false) {
    p.querySelector(".cart-name").textContent = name;
    p.querySelector(".cart-radius").textContent = radius;
    let sel_dough = dough.options[dough.selectedIndex].text;
    p.querySelector(".cart-dough").textContent = sel_dough;
    p.querySelector(".cart-price").textContent = price;
    p.querySelector(".cart-img").src = img;
    p.querySelector(".cart-main-price.hide").textContent = price.split(" ")[0];
    main_amount = parseInt($(".main-amount").text().split(" ")[0])
    main_amount += parseInt(price.split(" ")[0]);
    document.querySelector(".main-amount").textContent = main_amount + " ₴";
    p.classList.remove("hide");
    let row = document.querySelector(".myrow");
    
    let dct1 = {
      name: name,
      radius: radius,
      dough: sel_dough,
      price: price,
      img: img,
      main_price: price.split(" ")[0],
      price_cart: $('.main-amount').text()
    };
    let cas = JSON.stringify(dct1);
      console.log(cas,$('.main-amount').text())
    $.post("cart/",
      {
        "csrfmiddlewaretoken": getCookie("csrftoken"),
        cas,
      },
      console.log(cas)
    );
    row.append(p);
  }
  card_cart = document.querySelector(".myrow");
  card_cart = Array.from(card_cart.children);
  
}


cards.forEach(function(card){
  let btn = card.querySelector(".btn");
  btn.addEventListener('click', function(){
    addElementInCart(card);
  })
})

function deleteCase(card){

  let name = card.querySelector(".cart-name").textContent;
  let radius = card.querySelector('.cart-radius').textContent;
  let d = card.querySelector('.cart-dough').textContent;
// cart-price, main-amount, count
  let dct = {
    name: name,
    radius: radius,
    dough: d,
    price_cart: $('.main-amount').text()
  }
  let add_case = JSON.stringify(dct)
    console.log(add_case)
  $.post("delete-cart/",
    {
      "csrfmiddlewaretoken": getCookie("csrftoken"),
      add_case,
    },
    console.log(add_case)
  );
    
}
