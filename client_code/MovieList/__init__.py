from ._anvil_designer import MovieListTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..MovieEdit import MovieEdit

class MovieList(MovieListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.movies.search()
    self.repeating_panel_1.add_event_handler('x-edit_movie', self.edit_movie)

    # Any code you write here will run before the form opens.

  def add_movie_click(self, **event_args):
    item = {}
    editing_form = MovieEdit(item=item)
    if alert(cotent=editing_form, large=True):
      #add the movie to the data table
      anvil.server.call('add_movie', item)
      #refresh the DataGrid
      self.repeating_panel_1.item = app_tables.movies.search()

  def edit_movie(self, movie, **event_args):
    item = dict(movie)
    editing_form = MovieEdit(item=item)

    if alert(cotent=editing_form, large=True):
      anvil.server.call('update_movie', movie, item)
      self.repeating_panel_1.items = app_tables.movies.search()

