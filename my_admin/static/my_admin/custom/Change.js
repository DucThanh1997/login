$(document).ready(function(){
    const form_mail = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
    const form_phone = /^[0-9-+]+$/;
    $("#change").click(function()
        {
          var email = $('#change-form input[name=email]').val();
          var fullname = $('#change-form input[name=fullname]').val();
          var sdt = $('#change-form input[name=sđt]').val();


          if (email == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống email ",
               })
          }
          if (fullname == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống fullname ",
               });
               return false;
           }

          if (sdt == "")
          {
            Swal.fire(
            {
                type: "error",
                title: "Lỗi",
                text: "Không được bỏ trống số điện thoại",
            })
            return false;
           }
          if (!form_mail.test(email))
            {
            Swal.fire(
                {
                    type: "error",
                    title: "Lỗi",
                    text: "Thông tin email sai",
                })
            return false;
            }
           if (!form_phone.test(sdt))
           {
            Swal.fire(
                {
                    type: "error",
                    title: "Lỗi",
                    text: "Thông tin số điệnn thoại sai",
                })
            return false;
            }

        $.ajax({
            type:"POST",
            url: "/my_admin/saveinfo",
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
