function isContain(str, substr) {
    return new RegExp(substr).test(str);
}

$('.navbar-nav').find('a').each(function () {
    if (!isContain(this.className, "btn")) {
        if (this.href == document.location.href || document.location.href.search(this.href) >= 0) {
            $('ul.nav > li').removeClass('active');
            $(this).parent().addClass('active'); // this.className = 'active';
        }
    }
});