import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings') 

import django 
django.setup() 
from rango.models import Category, Page

def populate(): 
	python_cat = add_cat('Python', 128, 64)
	
	add_page(cat=python_cat,
            title="Learn Python in 10 Minutes",
            url="https://www.stavros.io/tutorials/python/",
			views=128)

	add_page(cat=python_cat,
			title="How to Think like a Computer Scientist",
			url="http://openbookproject.net/thinkcs/python/english3e/",
			views=128)

	add_page(cat=python_cat,
            title="Official Python Tutorial",
            url="https://docs.python.org/3/tutorial/index.html",
			views=128)

	django_cat = add_cat('Django', 64, 32)

	add_page(cat=django_cat,
            title='How to Tango With Django',
            url="https://www.tangowithdjango.com/",
			views=64)

	add_page(cat=django_cat,
            title="Django Books",
            url="http://www.djangobooks.com/",
			views=64)
			
	add_page(cat=django_cat,
            title="Offical Django Tutorial",
            url="https://docs.djangoproject.com/en/2.1/intro/tutorial01/",
			views=64)

	otherframeworks_cat = add_cat('Other Frameworks', 32, 16)

	add_page(cat=otherframeworks_cat,
            title='Flask',
            url="http://flask.pocoo.org/",
			views=32)

	add_page(cat=otherframeworks_cat,
            title="Bottle",
            url="https://bottlepy.org/docs/dev/",
			views=32)
	
	for c in Category.objects.all(): 
		for p in Page.objects.filter(category=c): 
			print("- {0} - {1}".format(str(c), str(p))) 
		 
def add_page(cat, title, url, views):
	p = Page.objects.get_or_create(category=cat, title=title)[0] 
	p.url = url	 
	p.views = views
	p.save()
	return p
	
def add_cat(cat, views, likes):
	c = Category.objects.get_or_create(name=cat)[0]
	c.views = views
	c.likes = likes
	c.save()
	return c

#strat excution
if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()