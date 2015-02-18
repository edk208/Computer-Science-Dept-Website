from app import db, models
i = models.Image(image_type='Colloquium', alt_text='This is an image',
				image_extension='png',)
s = models.Sideview(content='Hello world! This is a content', title='Hello World!',
					category='Colloquium', active=1, image=i)
n = models.News(headline='this is some news', intro='here is some content')

a = models.Alert(content='this is some content', user_id=1, location='villanova', category='alertCat', post_date=1, start_date=2, end_date=2)

#db.session.add(i)
#db.session.add(s)
#db.session.add(n)
db.session.add(a)
db.session.commit()