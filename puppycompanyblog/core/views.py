from flask import render_template,request,Blueprint
from puppycompanyblog.models import BlogPost
from puppycompanyblog import weather

core = Blueprint('core',__name__)

@core.route('/')
def index():

    weatherApi = weather.weatherApi()
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    context={'blog_posts':blog_posts,'weather':weatherApi}
    return render_template('index.html',data=context)


@core.route('/info')
def info():

    return render_template('info.html')
