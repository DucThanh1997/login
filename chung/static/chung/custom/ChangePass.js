$(document).ready(function(){
    const form_mail = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
    const form_phone = /^[0-9-+]+$/;
    $("#change").click(function()
        {
          var old_pass = $('#change-form input[name=Old_Pass]').val();
          var new_pass = $('#change-form input[name=New_Pass]').val();
          var re = $('#change-form input[name=Re]').val();


          if (old_pass == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống  ",
               })
          }
          if (new_pass == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống fullname ",
               });
               return false;
           }

          if (re == "")
          {
            Swal.fire(
            {
                type: "error",
                title: "Lỗi",
                text: "Không được bỏ trống số điện thoại",
            })
            return false;
           }

           if (re != new_pass)
          {
            Swal.fire(
            {
                type: "error",
                title: "Lỗi",
                text: "Không khớp",
            })
            return false;
           }

        $.ajax({
            type:"POST",
            url: "/user/savepass",
            data: $('#change-form').serialize(),
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
                        title: 'Thành công',
                        text: 'Sửa thành công',
                        showConfirmButton: false,
                        timer: 1000
                    }).then(() =>{
                        location.replace(result.messages)
                        });
                };
             }
        });
    });
});
