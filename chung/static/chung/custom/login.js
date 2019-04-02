$(document).ready(function(){
    $("#login").click(function()
        {
          var name = $('input[name=ten]').val();
          var pass = $('input[name=password]').val();

          if (name == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống",
               });
               return false;
           }
          if (pass == "")
          {
            Swal.fire(
            {
                type: "error",
                title: "Lỗi",
                text: "Không được bỏ trống",
            })
            return false;
           }
        $.ajax({
            type:"POST",
            url: location.href,
            data: $('#login-form').serialize(),
            success: function(data){
                var result = data;
                if(result.status == 'False'){
                    Swal.fire({
                        type: 'error',
                        title: 'Lỗi',
                        text: result.messages,
                    });
                }
                else{
                    Swal.fire({
                        type: 'success',
                        title: 'Thành công',
                        text: 'Đăng nhập thành công',
                        showConfirmButton: false,
                        timer: 1000
                    }).then(() =>{
                        location.replace(result.messages)
                    })
                };
             }
        });
    });
});
