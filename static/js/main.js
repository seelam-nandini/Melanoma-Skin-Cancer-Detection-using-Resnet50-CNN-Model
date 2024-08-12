$(document).ready(function () {
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();
    $('#message').hide();  // Hide message initially
    
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    } 
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        $('#message').hide(); 
        readURL(this);
    });

    $('#btn-predict').click(function () {
        if ($('#imageUpload').val() === '') {
            // Show message if no image is uploaded
            $('#message').text('To proceed with the prediction, upload an image first !!!').show();

            return;
        }
        var form_data = new FormData($('#upload-file')[0]);

        $(this).hide();
        $('.loader').show();

        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').text('Result: ' + data);
                console.log('Success!');
            },
        });
    });
});