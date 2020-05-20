class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  
  def __repr__(self):
    return '{artist}. "{title}". {year}, {medium}, {owner_name}, {owner_location}.'.format(artist =self.artist, title = self.title, year = self.year, medium = self.medium, owner_name = self.owner.name, owner_location = self.owner.location)

class Marketplace:
  def __init__(self, listings):
    self.listings = []
  
  def add_listings(self, new_listing):
    self.listings.append(new_listing)
  
  def remove_listings(self,new_listing):
    self.listings.remove(new_listing)

  def show_listings(self):
    for i in self.listings:
      print(i)

class Client:
  def __init__(self, name, location = "NA", is_museum = True):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listings(new_listing)
  
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listings(art_listing)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return '%s, %s' % (self.art.title, self.price)

# Defining marketplace veneer
veneer = Marketplace([])

# Defining private collector client
edytta = Client('Edyta Halpirt', 'Private Collection', is_museum = False)

# Defininf art
girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 'oil in canvas', 1910, edytta)

# Defining museum client
moma = Client('The MOMA', 'New York', True)

# Calling sell artwork method from client class and show listings method from Marketplace class
edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')
veneer.show_listings()

# Calling buy artwork method from client class and show listings method from Marketplace class
moma.buy_artwork(girl_with_mandolin)
veneer.show_listings()

# Printing art with new owner
print(girl_with_mandolin)