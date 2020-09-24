$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (hi) {
  $('#hello').text(hi.hello);    
});
