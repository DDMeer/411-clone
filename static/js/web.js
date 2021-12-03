var login;
var create;
var change;
$( document ).ready(function() {
    login =function (account, pwd){
        query_string = 'select Password from User where Account = '+ "'"+ account+"'"
        $.post("/query",{query_string: query_string},
            function(data, status){
            returnPwd = data['data']['values'][0]
            // returnUser_id = data['data']['values'][1]
            if(returnPwd == pwd){
                alert('Login Successfully')
                 window.location.href="/permission/"+account ///+"/"+returnUser_id
            }else {
                alert('Incorrect Account or Passsword')
            }
        },'json')
    }

    $("#login").click(function () {
        var account = $("#account").val();
        var pwd = $("#pwd").val();
        login(account, pwd);
    })


    create =function (account,fav_class,gender,name, pwd, conPwd){
        if (pwd != conPwd){
            alert("Input different password")
            return False
        }
        $.post("/insert",{account: account, pwd:pwd, fav_class:fav_class, gender:gender,name:name},
            function(data, status){
                alert('Success')
        }, 'json')
    }

    $("#create").click(function () {
        var account = $("#createAccount").val();
        var fav_class = $("#Favoriate_class").val();
        var gender = $("#Gender").val();
        var name = $("#User_Name").val();
        var pwd = $("#createPassword").val();
        var conPwd = $('#confirmPassword').val();
        create(account,fav_class,gender,name, pwd, conPwd);

    })


    change = function (account, pwd, newPwd, cnewPwd){
        if (newPwd != cnewPwd){
            alert("Input different password")
            return false
        }
        query_string = 'select Password from User where Account = '+ "'"+ account+"'"
        $.post("/query",{query_string: query_string},
            function(data, status){
            returnPwd = data['data']['values']
            if(returnPwd != pwd){
                alert('Incorrect Account or Passsword')
                return false
            }else {
                $.post("/update",{account: account, pwd:newPwd},
                    function(data, status){
                    alert('Suc')
                }, 'json')

            }
        },'json')

    }

    $("#change").click(function (){
        var account = $("#changeAccount").val();
        var pwd = $("#oldPassword").val();
        var newPwd = $('#newPassword').val();
        var cnewPwd = $('#cnewPassword').val();
        change(account, pwd, newPwd, cnewPwd)
    })
    

    $("#twosearch").click(function () {
        var resName = $("#resName").val();
        $.post("/two",{name: resName},
            function(data, status){
        },'json')
    })

    // $("#call").click(function () {
    //     $.post("/call",{id:112233},
    //         function(data, status){
    //     },'json')
    // })
    
})
