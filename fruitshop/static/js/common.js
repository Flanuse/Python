function addgoods(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/cart/addtocart/',
        type: 'POST',
        headers: {'X-CSRFToken': csrf},
        data: {
            'goods_id': id,

        },
        dataType: 'json',
        success: function (data) {
                if(data.code==200){
                    $('#num_'+ id).val(data.c_num)
                    totalprice()
                }else{

                    alert(data.msg)
                }
        },
        error: function (data) {
            alert('请求失败')
        }


    })
}

function subgoods(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
        $.ajax({
            url: '/cart/subtocart/',
            type: 'POST',
            data: {'goods_id': id},
            dataType: 'json',
            headers: {'X-CSRFToken': csrf},
            success: function (data) {
                if(data.code==200){
                    $('#num_'+ id).val(data.c_num)
                    totalprice()
                }else{

                    alert(data.msg)
                }
            },
            error: function (data) {
                alert('请求失败')
            }
        })
}

// 加载商品详情时直接就能看见数量
$.get('/cart/goodsnum/', function (data) {
    if (data.code == 200){
        for(var i=0;i<data.carts.length;i++){
            $('#num_' + data.carts[i].goods_id).val(data.carts[i].c_num)
            // $('#price_' + data.carts[i].goods_id).text(data.carts[i].price)
        }
    }else{
        alert('用户未登录')
    }
});

// 获取总价
function totalprice() {
    $.get('/cart/totalprice/', function (data) {
        if(data.code =='200') {

            $('#totalprice').text(data.total_price)
            a = data.total_price
            b = a + 10
            $('#totalprice1').text(b)
            $('#amount_num').text(data.amount)
            // $('#changecart_' + id).prop('checked', false)
            for (var i = 0; i < data.price_list.length; i++) {
                $('#price_' + data.price_list[i].goods_id).text(data.price_list[i].price + '元')
                // $('#changecart_' + id).prop('checked', true)
            }
             for (var i = 0; i < data.price1_list.length; i++) {
                $('#price' + data.price1_list[i].goods_id).text(data.price1_list[i].price + '元')

            }
        }
    })
}
totalprice()


function delete_goods(id) {
    $.ajax({
        url: '/cart/deletegoods/',
        type: 'GET',
        dataType: 'json',
        data: {'goods_id': id},
        success: function(data){
            if(data.code == 200){
                $('#cart_list_' + id).remove()
                totalprice()
            }else{
                alert(data.msg)
            }
        },
        error: function(data){
            alert('请求失败')
        }
    });
}


function changestatus(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/cart/changestatus/',
        type: 'POST',
        dataType: 'json',
        data: {'goods_id': id},
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if(data.code == 200){
                if(data.cart_is_select == true){
                    $('#changecart_' + id).prop('checked', true)
                }else{
                    $('#changecart_' + id).prop('checked', false)
                }

            }
              totalprice()
        },
        error: function (data) {
            alert('请求失败')
        }
    })

}

function changeorder(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/order/orderchange/',
        type: 'POST',
        data: {'order_id': id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if(data.code == 200){
                // alert(data)
                location.href = '/user/my/'
            }
        },
        error: function (data) {
            alert('请求失败')
        }

    })
}

$(function () {
    $.ajax({
        url: '/order/amountprice/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
             if(data.code == 200){
                 // $('#amountpr').text(data.amount)
                 for (var i = 0; i < data.price_list.length; i++) {
                 $('#pre_' + data.price_list[i].order_id).text(data.price_list[i].price + '元')

                 }
             }

        },
        error: function (data) {
            alert("请求失败")
        }

    });
});