
        var otp=document.getElementById('otp')
        otp.addEventListener('click',sendotp);
        function sendotp() {
            console.log('user is authenticated, sending data')
            var email="{{ email }}";
            var rollno="{{ rollno }}";
            var url = '/otpapi/';

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({'rollno': rollno, 'email': email})
            })
            .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('Data:', data)
        });
        }
