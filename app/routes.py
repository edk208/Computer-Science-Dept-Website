from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/carousel')
def carousel():
	return render_template('carousel.html')

@app.route('/article', methods=['POST', 'GET'])
def article():
	#e=request.args['articleNumber']

	#QUERY DATABASE HERE
	results = {}
	results['articleImage'] ='120003' 
	results['articleHeader']='There is some data'
	results['articleContent']='We have contempt for our content'

	return render_template('article.html', data=results)

@app.route('/getArticleNumber')
def getArticleNumber():
	return 12

@app.route('/general', methods=['POST', 'GET'])
def generalPage():
	e = request.args['content']
	return render_template('pageTemplate.html', content=e)

@app.route('/loadJson', methods=['POST', 'GET'])
def loadJson():
	return 12
#@app.route('/about')
#def aboutGeneral():
# #	return render_template('pageTemplate.html', content="about")

# @app.route('/academics')
# def aboutGeneral():
# 	return render_template('pageTemplate.html', content="academics")

