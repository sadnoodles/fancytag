function fancytag_static(id_name, tag_list) {
    (function($) {
        $(document).ready(function() {
            $(id_name).select2({
                width: "element",
                maximumInputLength: 50,
                tokenSeparators: [",", " "],
                tags: tag_list
            });
        });
    }(django.jQuery));
};

function fancytag(id_name, api_url) {
    (function($) {
        $(document).ready(function() {
            $(id_name).select2({
                tags: true,
                tokenSeparators: [','],
                createSearchChoice: function(term) {
                    return {
                        id: $.trim(term),
                        text: $.trim(term) + ' (new tag)'
                    };
                },
                ajax: {
                    url: api_url,
                    dataType: 'json',
                    data: function(term, page) {
                        return {
                            q: term
                        };
                    },
                    results: function(data, page) {
                        return {
                            results: data
                        };
                    },
                    cache: true
                },

                // Take default tags from the input value
                initSelection: function(element, callback) {
                    var data = [];

                    function splitVal(string, separator) {
                        var val, i, l;
                        if (string === null || string.length < 1) return [];
                        val = string.split(separator);
                        for (i = 0, l = val.length; i < l; i = i + 1) val[i] = $.trim(val[i]);
                        return val;
                    }

                    $(splitVal(element.val(), ",")).each(function() {
                        data.push({
                            id: this,
                            text: this
                        });
                    });


                    callback(data);
                },

                // Some nice improvements:

                // max tags is 50
                maximumSelectionSize: 50,

                // override message for max tags
                formatSelectionTooBig: function(limit) {
                    return "Max tags is only " + limit;
                }
            });
        });
    }(django.jQuery));

};