var login;
var create;
var change;
$( document ).ready(function() {
    login =function (account, pwd){
        query_string = 'select Password from User where Account = '+ "'"+ account+"'"
        $.post("/query",{query_string: query_string},
            function(data, status){
            returnPwd = data['data']['values']
            if(returnPwd == pwd){
                alert('Login Successfully')
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


    create =function (account, pwd, conPwd){
        if (pwd != conPwd){
            alert("Input different password")
            return False
        }
        $.post("/insert",{account: account, pwd:pwd},
            function(data, status){
                alert('Success')
        }, 'json')
    }

    $("#create").click(function () {
        var account = $("#createAccount").val();
        var pwd = $("#createPassword").val();
        var conPwd = $('#confirmPassword').val();
        create(account, pwd, conPwd);

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
    
    //
    // $("#search").click(function () {
    //     var resName = $("#resName").val();
    //     $.post("/searchR",{name: resName},
    //         function(data, status){
    //     },'json')
    // })
    
})
