$('document').ready(function () {
  const list_movies = $('#list_movies');
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (response) {
      const movies = response.results;
      movies.forEach(movie => {
        const title = movie.title;
        const listItem = $('<li>').text(title);
        list_movies.append(listItem);
      });
    },
    error: function (xhr, status, error) {
      console.error('something went wrong', error);
    }
  });
});
