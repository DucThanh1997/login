$(document).ready(function(){
    const form_mail = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
    const form_phone = /^[0-9-+]+$/;
    $("#Sign_Up").click(function()
        {
          var email1 = $('#Sign_Up-Form input[name=email]').val();

          var fullname = $('#Sign_Up-Form input[name=fullname]').val();
          var sdt = $('#Sign_Up-Form input[name=sdt]').val();
          var username = $('#Sign_Up-Form input[name=username]').val();
          var password1 = $('#Sign_Up-Form input[name=password1]').val();
          var password2 = $('#Sign_Up-Form input[name=password2]').val();
          var email2 = "thanh.tranduc@meditech.vn"
          var thanh = 'thanh123'
          if (email1 == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống email ",
               })
            return false;
          }
          if (sdt == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống số điện thoại ",
               })
            return false;
          }
          if (username == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống tên người dùng  ",
               })
            return false;
          }
          if (fullname == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống họ và tên ",
               })
            return false;
          }
          if (password1 == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống password ",
               })
            return false;
          }
          if (password2 == "")
          {
            Swal.fire({
               type: "error",
               title: "Lỗi",
               text: "Không được bỏ trống password ",
               })
            return false;
          }
          if (!form_mail.test(email1))
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
            url: "chung/signup2",
            data: $('#Sign_Up-Form').serialize(),
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
                        text: 'Hãy vào gmail kích hoạt tài khoản',
                        showConfirmButton: false,
                        timer: 3000
                    })
                };
             }
        });
    });
});
