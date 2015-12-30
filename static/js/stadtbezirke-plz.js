$("select[name='0-plz']").change(function() {
    map = {
        "80331": ["Lochhausen", "Lehel"],
        "80333": ["Allach"],
        "80335": ["Lehel"],
    };
    
    $el = $("select[name='0-stadtbezirk']");
    $el.empty();
    map[$(this).val()].forEach(function(stadtbezirk) {
        $el.append($('<option></option>').attr("value", stadtbezirk).text(stadtbezirk));
    });
});
