// JS to fetches and replace character with URL
$.get('https://swapi.co/api/films/?format=json', function (data) {
  for (let index in data.results) {
    $('UL#list_movies').append('<li>' + data.results[index].title + '</li>');
  }
});
