from basic import db, Puppy


# Create 
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# Read
Puppy.query.all()


# Select
Puppy.query.get(1)

# Filters
frankie=Puppy.query.filter_by(name='Frankie')
print(frankie.all())

# Update
rufus = Puppy('Rufus', 5)
rufus.age = 6
db.session.add(rufus)
db.session.commit()

# delete
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

# Print all at the end
Puppy.query.all()
