$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (char) {
  $('#character').text(char.name);    
});
