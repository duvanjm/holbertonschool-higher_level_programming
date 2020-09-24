$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (film) {
  for (const filmm of film.results) {
    $('#list_movies').append('<li>' + filmm.title + '</li>');
  }
});
