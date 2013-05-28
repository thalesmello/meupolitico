jq(document).ready(function() {
    jq('#subject_keywords').parent().hide();
	jq('#allowDiscussion').parent().hide();
    jq('#conteudoPrincipal').css('width','765px');
});

$(document).ready(function() {
    if ((!$('#MenuLateralDireito')[0])) {
        $("#conteudoPrincipal").css("width", "985px");
    }
});