$(document).ready(function(){
    const form_mail = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
    const form_phone = /^[0-9-+]+$/;
    $("#Reset").click(function()
        {
          var password1 = $('#Sign_Up-Form input[name=New_Pass]').val();
          var password2 = $('#Sign_Up-Form input[name=Re]').val();
          if (password1 == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống email ",
               })
            return false;
          }
          if (password2 == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống số điện thoại ",
               })
            return false;
          }
          if (password2 != password1)
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Mời bạn nhập lại mật khẩu  ",
               })
            return false;
          }

        $.ajax({
            type:"POST",
            url: "chung/resetpass2",
            data: $('#Reset_Pass-Form').serialize(),
            success: function(data)
            {
                var result = JSON.parse(JSON.stringify(data));
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
                        title: 'Done',
                        text: 'Hãy vào gmail để xác nhận',
                        showConfirmButton: false,
                        timer: 3000
                    })
                };
             }
        });
    });
});
