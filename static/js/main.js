(function($) {

    var Main = {
        init: function() {
            Main.passwordValidation();
            Main.validateForm();
        },

        passwordValidation: function() {
            $.validator.addMethod("atLeastAlphanumeric", function (value) {
                return /^[a-z]+[0-9]/i.test(value);
            }, 'Must contain at least one letter and one number.');

            $.validator.addClassRules("password", {
                minlength: 8,
                atLeastAlphanumeric: true
            });
        },

        validateForm: function() {
            $('.form').each(function() {
                $(this).validate({
                    submitHandler: function(form) {
                        form.submit();
                    }
                });
            });
        }
    };

    $(function() {
        Main.init();
    });

})(jQuery);
