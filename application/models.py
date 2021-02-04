from application import db





class regions(db.Model):
    
    id = db.Column( db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    
    bases= db.relationship("bases", backref ='regions')
    map_id = db.relationship('maps', backref ='regions')





class bases(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)    
    name = db.Column(db.String(50), nullable=False)
    
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=False)




class cards(db.Model):
    
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    
    cmap = db.relationship('cmap', backref ='cards')





class maps(db.Model):
    
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=False)
    name = db.Column(db.String(50), unique=True ,nullable=False)
    base_tier = db.Column(db.Integer, nullable=False)
    max_tier= db.Column(db.Integer, nullable=False)
    Layout = db.Column(db.String(1), nullable=False)
    boss = db.Column(db.Integer, nullable=False)
    
    cmap = db.relationship("cmap", backref ='maps')



class cmap(db.Model):
    
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    map_id = db.Column(db.Integer, db.ForeignKey('maps.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False)
