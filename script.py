class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  
  def __repr__(self):
    return "{artist}. \"{title}\". {year}, {medium}, {owner}, {location}".format(artist=self.artist, title = self.title, year = self.year, medium = self.medium, owner = self.owner.name, location = self.owner.location)
  


class Marketplace:
  def __init__(self):
    self.listings = []
    
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    
  
  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)
    
  
  def show_listings(self):
    for listing in self.listings:
      print(listing)
      


class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  
  
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
 

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
          
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)
    
    
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  
  def __repr__(self):
    return "{name}:{price}".format(name = self.art.title, price = self.price)
  
  
veneer = Marketplace()

edytta = Client("Edytta halppirt", None, False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()
